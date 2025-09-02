---
layout: post
title: "Acceleo, un générateur open source pour des développements dirigés par les modèles (Solutions Linux 2007)"
categories:
  - talk
tags:
  - talk
  - ecore
  - acceleo
  - java
  - uml
excerpt: "Acceleo for model‑driven development—slides from Solutions Linux 2007."
---

This presentation introduces **Acceleo**, an open-source model-to-text code generator, in the context of model-driven development (MDD). It balances theory with practice, showing how models such as UML can be transformed into executable artifacts (J2EE code, HTML documentation) through Acceleo templates. The talk highlights both the benefits of MDD—automation, consistency, and efficiency—and its pitfalls, such as over-modeling or tooling complexity. Using pragmatic examples (like generating a J2EE application), the presentation demonstrates Acceleo’s strengths: openness, standards compliance, community support, and seamless integration into Eclipse, while emphasizing a practical, iterative approach to applying MDD in real-world software projects.

### Key Takeaways
* **Acceleo’s role**: Open-source, template-based generator that turns models (UML, DSLs) into code and documentation.
* **MDD principles**: Separation of concerns, model-to-meta-model conformity, and the Y-cycle process from modeling to implementation.
* **Practical example**: Generating a J2EE application from UML models, with clear mapping from design (entities, screens, workflows) to code artifacts (JSPs, DAOs, DTOs, configs).
* **Benefits**: Faster development, enforcement of best practices, technology independence, improved quality and maintainability.
* **Pitfalls**: Risks of over-modeling, rigid tooling, lack of iterative adaptation—mitigated by pragmatism and incremental generation.
* **Usability**: Eclipse integration with editors, syntax highlighting, instant preview, and user-code preservation during regeneration.
* **Openness & Standards**: Full support for UML, XMI, EMF, and extensibility toward multiple target technologies.
* **Conclusion**: Acceleo and MDD enable productivity and modernization but require a pragmatic, balanced application.

[![]({{ site.url }}/images/blog/2007/sol-linux.png)]({{ site.url }}/talks/SolutionsLinux2007/SolutionsLinux2007-Acceleo.pdf)


## Context
- Event: Solutions Linux, Paris
- Date: 2007
- Slides: {{ site.url }}/talks/SolutionsLinux2007/SolutionsLinux2007-Acceleo.pdf
