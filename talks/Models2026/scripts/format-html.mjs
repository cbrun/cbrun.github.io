import { readFile, writeFile } from 'node:fs/promises';
import assert from 'node:assert/strict';
import prettier from 'prettier';

// Keep plain transcript paragraphs readable in the source and speaker view.
function formatNotes(html) {
  return html.replace(/(<aside class="notes">)([\s\S]*?)(<\/aside>)/g, (_, open, body, close) => {
    const paragraphs = body.includes('<p>')
      ? body.match(/<p>[\s\S]*?<\/p>/g)
      : body.trim().split(/\n\s*\n/).map(text => `<p>${text}</p>`);
    return `${open}\n${paragraphs.map(p => p.replace(/\s+/g, ' ').trim()).join('\n')}\n${close}`;
  });
}

assert.equal(
  formatNotes('<aside class="notes">First\n sentence.\n\nSecond.</aside>'),
  '<aside class="notes">\n<p>First sentence.</p>\n<p>Second.</p>\n</aside>'
);
assert.equal(
  formatNotes('<aside class="notes"><p>First\n sentence.</p>\n<p>Second.</p></aside>'),
  '<aside class="notes">\n<p>First sentence.</p>\n<p>Second.</p>\n</aside>'
);

const input = await readFile('index.html', 'utf8');
const output = await prettier.format(formatNotes(input), {
  ...await prettier.resolveConfig('index.html'),
  filepath: 'index.html',
});
if (process.argv.includes('--check')) {
  assert.equal(input, output, 'Run npm run format:html to format the HTML and speaker notes.');
  console.log('HTML and speaker notes are formatted.');
} else {
  await writeFile('index.html', output);
  console.log('Formatted HTML and speaker notes.');
}
