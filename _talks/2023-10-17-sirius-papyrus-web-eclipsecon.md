---
layout: post
title: "(Sirius + Papyrus) × Web — EclipseCon 2023, Ludwigsburg"
categories:
  - talk
tags:
  - talk
  - eclipse
  - sirius
  - papyrus
  - uml
  - MBSE
excerpt: "EclipseCon 2023 session: collaboration between Obeo and CEA on Sirius Web and Papyrus Web—slides, video, and who should care."
draft: true
---
## Collaborative Modeling: Obeo, CEA Join Forces in Eclipse

**Cedric Brun, CEO of Obeo, and Sebastian Gerard, from CEA, discuss a new partnership within the Eclipse Foundation focusing on Model-Based Systems Engineering (MBSE) technologies.**

### The Challenge of Increasing System Complexity

Modern systems are becoming increasingly complex, often exceeding human cognitive abilities to manage them effectively. To help engineers stay on top of this complexity, new methods and tools for systems engineering are required. This presents several challenges, including:

* **Sovereignty and Security:** Ensuring the security and sovereignty of tools used for critical systems.
* **User Experience:** Improving user experience for tasks like onboarding, accommodating unexpected usage scenarios, and collaborating at scale with multiple organizations.
* **Digital Thread:** Enabling a seamless flow of information across the entire system lifecycle, from requirements to design, implementation, and operation.
* **Augmented Engineering:** Integrating Artificial Intelligence (AI) technologies like chatbots, generative AI, and large language models into the software engineering landscape.
* **Knowledge Editing:** Introducing new ways to edit and manage knowledge, such as multi-modal user interfaces and the use of metaverse and virtual reality for collaboration.

### Obeo and CEA: Complementary Strengths in MBSE

Both Obeo and CEA have extensive experience in the MBSE field, with complementary areas of expertise.

* **CEA:** Heavily involved in standardization activities at the Object Management Group (OMG), contributing to the development of standards like UML, SysML, and the new SysMLv2. Also involved in the Eclipse Foundation, supporting projects like Papyrus.
* **Obeo:** A French company specializing in building MBSE tools within the Eclipse ecosystem. Known for contributions to projects like Eclipse Sirius, EMF Compare, and Capella.

### The Path to Collaboration: Four Key Steps

The collaboration between Obeo and CEA is focused on addressing the challenges mentioned above. The initial steps include:

1. **Sirius Web and Papyrus on Sirius Desktop:** Obeo's development of Sirius Web, enabling web-based modeling with Sirius, occurred in parallel with CEA's migration of Papyrus to Sirius Desktop.
2. **Papyrus on Sirius Desktop:** CEA decided to migrate Papyrus from the deprecated GMF tooling to Sirius Desktop after analyzing available technologies.
3. **Papyrus Web Editors:** Building upon Obeo's work on Sirius Web, CEA aims to eventually migrate Papyrus to a web-based technology, with Sirius Desktop serving as an intermediate step.
4. **SysMLv2:** Both organizations are collaborating to support SysMLv2, leveraging their combined expertise in standards development (CEA) and tooling implementation (Obeo).

### Papyrus Web Editors: Current Status and Underlying Technologies

The initial milestone for Papyrus Web Editors is complete, with 100% of the metamodel and basic editing facilities implemented. Import/export functionality for UML models and initial versions of editors for composite, package, class, and state machine diagrams are available.

Current development efforts focus on:

* **Profile and Application Concepts:** Enabling support for profiles within the web version of Papyrus.
* **Improved Property Editing and UI/Layout Enhancements:** Refining the user experience and interface.

The underlying technologies of Papyrus Web Editors include:

* **Spring Boot, React, and GraphQL:** Industry-standard web technologies for building modern and efficient applications.
* **Sirius Web:** A modular platform that defines components with backend and frontend capabilities, enabling integration into a single application.
* **Eclipse MDT UML Implementation:** Reused on the backend to ensure consistent behavior with the desktop version of Papyrus.
* **UML Services Component:** A shared component between desktop and web editors for maintaining consistent behavior.
* **View Model:** Describes all the tooling elements (diagram editors, forms, etc.) as a model, allowing for easy customization and adaptation.

### SysON: An Open-Source SysMLv2 Tooling Project

The collaboration also includes the creation of a new Eclipse project called SysON. SysON aims to provide open-source web-based modeling tools for editing SysMLv2 models conforming to OMG standards.

The project's main areas of interest are:

* **Capella Integration:** Enabling co-design of systems with parts designed as SysMLv2 in Capella and reused in Papyrus.
* **Structure Editing:** Focusing on graphical modeling, forms, tables, etc.
* **Interoperability:** Ensuring support for the textual syntax defined in the SysMLv2 standard for exchanging models with other tools.

SysON is currently in the proposal phase, with the initial contribution planned for the end of the year. The goal is to provide basic system modeling capabilities by the end of next year.

### Getting Involved and Next Steps

There are several ways to get involved in this exciting initiative:

* **Express Interest:** Contact Obeo and CEA to be listed as an interested party in the SysON project proposal.
* **R&D Projects:** Discuss potential R&D collaborations with Sebastian Gerard from CEA, particularly if you have industry use cases relevant to SysMLv2.
* **Sponsored Development:** Collaborate with Obeo to fund the development of specific features or adaptations of the tools for your needs.

## Context
- Event: EclipseCon 2023, Ludwigsburg, Germany.
- Date: October 2023
- Program: [Link](https://www.eclipsecon.org/2023/sessions/sirius-papyrus-%C3%97-web-new-era-collaborative-engineering-tools)

## Related Blog Posts
- [(Sirius + Papyrus) × Web: a new Era for Collaborative Engineering tools]({{ site.url }}/eclipsecon2023/)
