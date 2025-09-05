---
layout: post
title: "EcoreTools 2.0 — The Making Of (EclipseCon Europe 2013)"
categories:
  - talk
tags:
  - talk
  - ecore
excerpt: "How EcoreTools 2.0 was built—decisions, trade‑offs, and what it enables for modelers."
draft: true
---

In this talk I open the hood on **EcoreTools 2.0** - the “making-of” of a modeling workbench. I start from the Ecore metamodel itself (EClass, EAttribute, EReference, …) and show how those foundations drive the UX: personas, semi-synchronized class diagrams, documentation/validation layers, smarter palettes and editing, and a revamped look. I then connect the dots in the Eclipse stack (Sirius, GMF/GEF, EMF, Acceleo, EEF) and explain how viewpoints, diagram definitions, and styles map cleanly back to your `.ecore` and model instances.

From there, I get practical: synchronization policies, low-coupling queries, a simple action language for tooling, concise label-editing syntax, and an extensible documentation layer. I close with the engineering side of the house, consistency tests, profiling before optimizing, build/test metrics, and the release cadence, plus a nod to community sessions around Sirius/Luna. It’s the full arc: from metamodel anatomy to the habits and tooling that keep a modeling product fast, usable, and shippable.

[![]({{ site.url }}/talks/EclipseConEU2013/EcoreTools2.thumb.png)]( {{ site.url }}/talks/EclipseConEU2013/EcoreTools2.pdf)

### Key points

* **Theme:** “The Making Of” EcoreTools 2.0—behind-the-scenes design and engineering choices.
* **Foundations:** Deep dive into the **Ecore** metamodel and why its structure shapes the tool’s UX.
* **Personas & UX:** Customer-driven prototyping; focused diagrams; strong documentation and collaborative reviews.
* **Demo highlights:** Semi-synchronized class diagrams, documentation & validation layers, per-element import, redesigned visuals, shortcuts, smarter palette/editing, documentation tables.
* **Architecture:** EcoreTools 2.0 on **Sirius** atop EMF/GEF/GMF/Acceleo/EEF within the Eclipse IDE.
* **Viewpoints & diagrams:** Clear linkage from domain models (`.ecore`) → viewpoints → diagram definitions → model instances (`.xmi`).
* **Styling system:** Conditional styles (containers, shapes, images) for consistent visual semantics.
* **Synchronization:** Per-mapping policies; query-based (OCL/Acceleo/Java) low coupling to semantic models.
* **Tooling language:** Declarative actions (create/update/delete, reconnect, DnD, edit, popup) and variables/conditions at runtime.
* **Label editing:** Compact syntax to change name, type, cardinality, derivation, and default values—wired to programmatic edits.
* **Documentation layer:** Extensible mappings, tools, and styles to enrich model documentation.
* **Quality & performance:** Parameterized tests to enforce consistency; profile first, then optimize queries and updates.
* **Build & releases:** Tycho builds, JUnit/SWTBot tests, codebase metrics; iterative Luna milestones and Sirius integration.
* **Community:** BOF/booth sessions to gather feedback and keep the loop tight between users and maintainers.


## Context
- Event: EclipseCon Europe 2013, Ludwigsburg, Germany
- Date: 2013
- Program: [https://www.eclipsecon.org/europe2013/ecoretools-20-making](https://www.eclipsecon.org/europe2013/ecoretools-20-making)
- Video: [https://www.youtube.com/watch?v=XSP-oAmmS_E](https://www.youtube.com/watch?v=XSP-oAmmS_E)
- Slides: [{{ site.url }}talks/EclipseConEU2013/EcoreTools2.pdf]({{ site.url }}/talks/EclipseConEU2013/EcoreTools2.pdf)
