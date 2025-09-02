---
layout: post
title: "Ingénierie des Modèles 2006 (IDM, Lille)"
categories:
  - talk
tags:
  - talk
  - acceleo
  - transformation
  - ecore
excerpt: "Talk at Ingénierie des Modèles 2006—slides and context."
---

For researchers and practitioners in the early days of MDE adoption. This talk presents a global vision of a complete reverse-engineering toolchain. It illustrates how legacy programs written in C or COBOL can be automatically analyzed using reverse-engineering techniques to produce an intermediate model (C-COBOL). From this model, transformations and generators allow organizations to derive new assets such as cartographies, documentation, or modernized source code. By leveraging Obeo’s technologies (Reverse, Transformation, Acceleo), the approach bridges old and new worlds, enabling a structured modernization path for legacy applications while preserving their semantics and opening them to future evolutions.


### Key Takeaways

* **Reverse Engineering**: Programs in C and COBOL are parsed into structured models using Obeo Reverse, based on dedicated metamodels.
* **Intermediate Model (C-COBOL)**: A central pivot model integrates information from both languages to enable consistent transformations.
* **Transformations**: The model can be transformed into higher-level representations, aligned with a cartography metamodel.
* **Outputs**:

  * **Graphical cartography** for system visualization.
  * **HTML documentation** for accessible knowledge transfer.
  * **Java programs** generated from legacy logic.
* **End-to-end Chain**: The process illustrates a complete modernization workflow, from legacy source code to up-to-date documentation and re-implemented applications.
* **Value**: Demonstrates how Obeo tools create a bridge between legacy systems and modern architectures, ensuring continuity and reducing risks in modernization projects.

[![]({{ site.url }}images/blog/2006/idm.png)]({{ site.url }}/talks/IDM06/Obeo.pdf)


## Context
- Event: IDM 2006, Lille
- Date: 2006
- Slides: {{ site.url }}/talks/IDM06/Obeo.pdf
