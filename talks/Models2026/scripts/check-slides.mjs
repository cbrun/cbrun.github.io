import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { join } from 'node:path';
import puppeteer from 'puppeteer';
import { createServer } from 'vite';

const server = await createServer({ configFile: false, root: process.cwd(), optimizeDeps: { noDiscovery: true }, server: { host: '127.0.0.1', port: 0 } });
await server.listen();
const browser = await puppeteer.launch({
  executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || '/usr/bin/google-chrome',
  headless: true,
  args: ['--no-sandbox'],
});
try {
  const page = await browser.newPage();
  await page.setViewport({ width: 1600, height: 900 });
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('response', response => { if (response.status() >= 400) errors.push(`${response.status()} ${response.url()}`); });
  await page.goto(server.resolvedUrls.local[0]);
  await page.waitForFunction(() => window.Reveal?.isReady());
  await page.evaluate(() => document.fonts.ready);
  const slides = await page.evaluate(() => Reveal.getSlides().map(s => ({
    id: s.id,
    budget: Number(s.dataset.timing),
    notes: s.querySelector('aside.notes')?.textContent.trim(),
    group: s.dataset.autoAnimateId,
  })));
  assert.equal(slides.reduce((total, s) => total + s.budget, 0), 1080);
  assert.equal(new Set(slides.map(s => s.id)).size, slides.length);
  assert(slides.every(s => s.notes), 'Every slide needs its spoken transcript.');
  const screenshots = process.env.SLIDE_SCREENSHOTS;
  if (screenshots) await mkdir(screenshots, { recursive: true });
  let animations = 0;
  let videos = 0;
  for (const [index, slide] of slides.entries()) {
    await page.evaluate(index => Reveal.slide(index), index);
    if (slide.group && slide.group === slides[index - 1]?.group) {
      await page.waitForFunction(() => Reveal.getCurrentSlide().dataset.autoAnimate === 'running');
      animations++;
    }
    // Wait for reveal's actual transition duration before measuring or capturing.
    await new Promise(resolve => setTimeout(resolve, 850));
    const overflow = await page.evaluate(() => {
      const slide = Reveal.getCurrentSlide();
      const frame = slide.getBoundingClientRect();
      return [...slide.querySelectorAll('h1,h2,p,img,video,small,strong')].filter(el => {
        if (el.closest('aside')) return false;
        const r = el.getBoundingClientRect();
        return r.width > 0 && (r.left < frame.left - 2 || r.right > frame.right + 2 || r.top < frame.top - 2 || r.bottom > frame.bottom + 2 || el.scrollWidth > el.clientWidth + 2);
      }).map(el => el.textContent || el.tagName);
    });
    assert.deepEqual(overflow, [], `${slide.id}: content exceeds its bounds`);
    if (await page.$('section.present video')) {
      videos++;
      await page.waitForFunction(() => {
        const video = Reveal.getCurrentSlide().querySelector('video');
        return video.readyState >= 2 && video.currentTime > 0 && !video.paused;
      });
      const duration = await page.$eval('section.present video', video => video.duration);
      assert(duration <= slide.budget, `${slide.id}: video exceeds slide budget`);
      await page.$eval('section.present video', video => { video.pause(); video.currentTime = Math.min(8, video.duration / 2); });
      await page.waitForFunction(() => !Reveal.getCurrentSlide().querySelector('video').seeking);
    }
    if (screenshots) await page.screenshot({ path: join(screenshots, `${String(index + 1).padStart(2, '0')}-${slide.id}.png`) });
  }
  assert.equal(videos, 7);
  assert.equal(animations, 6);
  await page.evaluate(() => Reveal.slide(Reveal.getSlides().findIndex(s => s.id === 'trace-demo')));
  await page.waitForFunction(() => Reveal.getCurrentSlide().querySelector('video').currentTime > 0);
  await page.evaluate(() => Reveal.next());
  assert(await page.$eval('#trace-demo video', video => video.paused), 'Video must pause when leaving its slide.');
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
  await page.reload();
  await page.waitForFunction(() => window.Reveal?.isReady());
  assert.equal(await page.evaluate(() => Reveal.getConfig().autoAnimate), false);
  assert.deepEqual(errors, [], 'Browser errors or missing assets');
  console.log(`${slides.length} slides: bounds, notes, 18-minute budget, ${animations} animation pairs, ${videos} videos, and reduced motion checked.`);
} finally {
  await browser.close();
  await server.close();
}
