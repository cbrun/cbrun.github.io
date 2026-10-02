# Your AI Agent Needs a Model

Cédric Brun · MODELS 2026 Industry Day · 18 minutes, followed by 2 minutes of Q&A.

## Present

Run `npm install` once, then `npm start` from this directory. Open
<http://localhost:8000/>. Fonts, logos, and video excerpts are local, so the talk
does not need an internet connection after installation.

- Arrow keys or Space: advance. Escape: overview. F: fullscreen. S: speaker view.
- Videos start on entry, stop on exit, and replay when revisited. Native controls
  allow pausing, seeking, and fullscreen playback. Narrate the silent recordings.
- Slides remain under the speaker's control; nothing advances automatically.
- Speaker notes contain the spoken transcript, section timings, delivery cues,
  and source references. The timing is a rehearsal budget, not a measured delivery.
- Read the plain paragraphs aloud. Bold brackets are delivery cues; `Talk` times
  refer to the whole presentation, while video cues start at 0:00 for each clip.
  Follow the visible event if playback differs from the approximate cue time.
  Small source and playback notes are reference material, not spoken text.
- The final slide stays on screen for Q&A. Reduced-motion preferences disable
  animations and transitions.

## Edit and verify

`index.html` is the deck, with notes beside each slide. `keynote.css` contains
the theme. Matching `data-auto-animate-id` and `data-id` attributes define six
animation sequences: semantics, reasoning, method, verification, the engineering
flow, and the model's limits.

```sh
npm run format:html
npm run format:html:check
npm run check:slides
```

The visual check starts its own temporary server and uses local Chrome. Set
`PUPPETEER_EXECUTABLE_PATH` if Chrome is installed elsewhere. Set
`SLIDE_SCREENSHOTS` to a directory to save one image of every slide.

## Video excerpts

Seven excerpts total approximately 5 minutes. They retain the timing
of the supplied recordings, which already contain accelerated work. Originals
in `../videos/` are untouched. Regenerate with `npm run prepare:media` (FFmpeg
required).

| Excerpt | Source recording | Source time |
| --- | --- | --- |
| Mission trace | 2 - Understanding a Model | 00:27–00:54 |
| Processor failure | 3-4 - Analysis - Consistency - Automation of the model | 00:54–01:23 |
| Decompression | Same | 01:24–01:56 |
| Mode consistency | Same | 01:57–02:26 |
| Arcadia discovery | 1 - Arcadia-Capella Discovery | 00:00–00:26, then 02:44–03:11 |
| AEB architecture and checks | 6 - Importing Data | Full recording, approximately 92 seconds |
| Capella for SysON | demo-syson-capella-extension | 01:20 to the end, approximately 39 seconds |

### Narration and handoffs

Introduce each question before advancing: the next slide starts playback
immediately. Narrate the selected points in the notes, leave space to watch,
then deliver the takeaway. For the three successive analysis clips, the
transition to the next question happens while holding the completed video.

| Excerpt | Audience focus | Where the argument continues |
| --- | --- | --- |
| Mission trace | Relationships connect a mission to equipment; gaps limit the answer. | The coverage slide reports a **separate** whole-model query, then returns to claim 1. |
| Processor failure | Dependencies reveal a possible single point of failure. | Hold the final frame, then introduce decompression. |
| Decompression | Follow a safety behavior until the modeled evidence stops. | Hold the final frame, then introduce consistency across levels. |
| Mode consistency | Similar modes can have different transitions. | The simplified comparison explains the finding; the review slide describes a correction sequence **outside** the excerpt. |
| Arcadia discovery | The method helps the user decide what to do next. | The clip jumps at 0:26; the following slide links guidance to the spreadsheet example. |
| AEB architecture and checks | First build a model, then use it to check design targets. | Read the results on the next slide; the latency slide frames the engineering decision. |
| Capella for SysON | An agent adds model relationships in a web environment. | Return to the limits: model access alone does not define good engineering. |

The Capella for SysON passage runs from 14:50 to 15:30, after the AEB synthesis.
It illustrates an agent adding exchanges in the web modeling environment.
The AEB introductions and result commentary have been shortened by 40 seconds
to preserve the 18-minute talk. Project positioning follows the
[launch article](https://blog.obeosoft.com/capella-for-syson): an early-stage
open-source modeling project bringing Arcadia to SysON and SysML v2. The demo
illustrates model operations; it does not establish parity with all preceding
analysis or verification scenarios, or the licensing of the AI integration.

The supplied conference banner provides the location and dates used on the
opening slide.

The architecture slide uses the supplied Capella wordmark and SVG symbols from
[Claude](https://claude.ai/favicon.svg), [OpenAI](https://openai.com/brand/), and
[Mistral](https://mistral.ai/favicon.svg). Copies in `assets/` keep the deck
self-contained.

Open Sans is bundled under its OFL license in `assets/fonts/OFL.txt`. Palette
and typography follow `../STYLE.md` and the supplied brand references.

---

## reveal.js upstream

<p align="center">
  <a href="https://revealjs.com">
  <img src="https://hakim-static.s3.amazonaws.com/reveal-js/logo/v1/reveal-black-text-sticker.png" alt="reveal.js" width="500">
  </a>
  <br><br>
  <a href="https://github.com/hakimel/reveal.js/actions"><img src="https://github.com/hakimel/reveal.js/actions/workflows/test.yml/badge.svg"></a>
  <a href="https://slides.com/"><img src="https://static.slid.es/images/slides-github-banner-320x40.png?1" alt="Slides" width="160" height="20"></a>
</p>

reveal.js is an open source HTML presentation framework. It enables anyone with a web browser to create beautiful presentations for free. Check out the live demo at [revealjs.com](https://revealjs.com/).

The framework comes with a powerful feature set including [nested slides](https://revealjs.com/vertical-slides/), [Markdown support](https://revealjs.com/markdown/), [Auto-Animate](https://revealjs.com/auto-animate/), [PDF export](https://revealjs.com/pdf-export/), [speaker notes](https://revealjs.com/speaker-view/), [LaTeX typesetting](https://revealjs.com/math/), [syntax highlighted code](https://revealjs.com/code/) and an [extensive API](https://revealjs.com/api/).

---

Want to create reveal.js presentation in a graphical editor? Try <https://slides.com>. It's made by the same people behind reveal.js.

---

### Getting started

- 🚀 [Install reveal.js](https://revealjs.com/installation)
- 👀 [View the demo presentation](https://revealjs.com/demo)
- 📖 [Read the documentation](https://revealjs.com/markup/)
- 🖌 [Try the visual editor for reveal.js at Slides.com](https://slides.com/)
- 🎬 [Watch the reveal.js video course (paid)](https://revealjs.com/course)

---

<div align="center">
  MIT licensed | Copyright © 2011-2026 Hakim El Hattab, https://hakim.se
</div>
