---
layout: page
title: "Understanding SysML v2 and what it changes for MBSE"
seoTitle: "SysML v2: what changes for MBSE"
description: "SysML v2 is now a formal OMG standard. Understand its semantics, textual and graphical syntax, API, tooling, and practical path to MBSE adoption."
permalink: /sysml-v2/
canonical: https://cedric.brun.io/sysml-v2/
lang: en
translation_fr: /fr/sysml-v2/
tags:
  - mbse
  - sysmlv2
  - syson
  - sirius-web
  - capella
  - obeo
cluster: sysml-v2
intent: "Understand what SysML v2 changes and how to approach its adoption"
primaryQuery: "what is SysML v2"
secondaryQueries:
  - "SysML v1 vs SysML v2"
  - "SysML v2 API"
  - "KerML"
  - "SysML v2 tools"
audience: "MBSE leaders, system architects, and systems engineers"
maturityStage: "awareness and evaluation"
pagePromise: "Explain the standard, its practical impact, and a credible adoption path"
proof:
  - "formal OMG specifications"
  - "open-source SysML v2 tooling"
  - "experience building industrial modeling platforms"
businessGoal: "Establish a stable reference point for the SysML v2 content cluster"
nextStep:
  - "/syson/"
  - "/modeling/models2024/"
  - "/talk/IEEE-ISSE25/"
image:
  thumb: blog/2026/sysml-v2/sysml-v2-language.webp
---

SysML v2 is not a cosmetic update to SysML v1. It is a redesign of the language around a more precise semantic foundation, standard textual and graphical notations, reusable libraries, and a standard API for accessing models.

The practical change is larger than a new set of diagrams. SysML v2 makes the system model easier to treat as engineering data: something people can navigate through different views, tools can query and transform, and other services can connect to through a shared interface.

The [OMG published SysML 2.0 as a formal specification in September 2025](https://www.omg.org/spec/SysML/2.0), together with [KerML 1.0](https://www.omg.org/spec/KerML/1.0) and the [Systems Modeling API and Services 1.0](https://www.omg.org/spec/SystemsModelingAPI/1.0). The standard is ready to read and implement. The surrounding tools and industrial practices, however, are still maturing. That distinction matters when planning an adoption.

<figure>
    <a href="{{ site.url }}/images/blog/2026/sysml-v2/sysml-v2-language.webp">
      <img src="{{ site.url }}/images/blog/2026/sysml-v2/sysml-v2-language.webp" alt="Hand-drawn SysML v2 lettering used to introduce the new systems modeling standard">
    </a>
    <figcaption>SysML v2 is a new foundation for systems modeling, not simply another notation revision.</figcaption>
</figure>

## What is SysML v2?

SysML v2 is the second major generation of the OMG Systems Modeling Language. It is intended for specifying, designing, analyzing, and verifying complex systems across requirements, structure, behavior, interfaces, analysis, and verification concerns.

Its purpose is familiar to anyone already practicing Model-Based Systems Engineering: create a coherent model that connects engineering decisions instead of scattering them across documents and disconnected diagrams. What changes is the language architecture underneath that goal.

SysML v1 was defined as a profile of UML. SysML v2 is built on **KerML**, a modeling language with an application-independent semantic foundation. SysML v2 specializes that foundation for systems engineering and adds domain concepts, notations, and standard libraries.

This matters because the meaning of the model is not owned by a particular diagram or vendor interface. A diagram, a textual editor, a table, a form, an analysis service, or an API client can expose different parts of the same semantic model.

## SysML v1 and SysML v2 are different generations

SysML v2 retains the systems engineering ambition of SysML v1, but it does not preserve every concept or modeling habit unchanged.

| Concern | SysML v1 | SysML v2 |
|---|---|---|
| Foundation | A UML profile | A language built on KerML |
| Semantics | Defined through UML extension mechanisms and SysML constraints | Grounded in the KerML semantic model |
| Notation | Primarily standardized graphical notation | Standard graphical and textual notations |
| Core modeling style | UML-inspired concepts and stereotypes | Consistent definition and usage concepts |
| Reuse | Profiles, model libraries, and tool-specific mechanisms | Language-level specialization, imports, and standard libraries |
| Interoperability | Mostly exchange formats and vendor integrations | A standard Systems Modeling API and Services specification |
| Migration | Tool- and organization-specific | A normative SysML v1-to-v2 transformation specification exists |

The table makes the change look clean. Real models are not. Organizations have profiles, conventions, validation rules, document generators, integrations, training material, and years of accumulated practice. A standard transformation specification helps establish mappings, but migration is not a push-button replacement for understanding those decisions.

The right question is therefore not only, "Can this model be converted?" It is also, "Which parts of our current modeling practice should survive, and how should they be expressed in the new language?"

## KerML gives the language its semantic foundation

[KerML](https://www.omg.org/spec/KerML/1.0) is the Kernel Modeling Language underneath SysML v2. It provides application-independent constructs for classification, relationships, behavior, structure, namespaces, and other recurring modeling needs.

Most systems engineers do not need to start by learning every KerML concept. They do need to understand why it exists.

KerML separates the reusable semantic foundation from the systems engineering vocabulary built on top of it. This gives SysML v2 a more coherent architecture and creates room for domain-specific languages and libraries that remain connected to the same foundation.

One visible consequence is the distinction between **definitions** and **usages**. A definition describes a reusable type of thing; a usage represents how that thing is used in a particular context. The distinction applies consistently across parts, actions, states, requirements, and other concepts. It is powerful, but it can require a shift in habits for teams coming from SysML v1.

## Textual and graphical syntax serve the same model

The standard textual notation is one of the most visible additions in SysML v2. It makes models easier to create, review, compare, generate, and process with familiar text-oriented infrastructure. The graphical notation remains essential for understanding architecture, behavior, and relationships at a glance.

This should not become a contest between text and diagrams. Different representations support different work:

- text is efficient for precise editing, automation, examples, and version-oriented workflows;
- diagrams reveal structure, context, and relationships;
- tables help compare sets of elements;
- forms guide focused editing;
- dedicated views can embody a method or answer a particular engineering question.

The important point is that these representations should operate on the same model. In practice, tool quality will depend as much on navigation, synchronization, validation, and usability as on the number of SysML v2 concepts implemented.

## The standard API changes the integration story

The [Systems Modeling API and Services specification](https://www.omg.org/spec/SystemsModelingAPI/1.0) defines a platform-independent service model and technology-specific bindings. It gives tools a shared basis for exposing projects, commits, model elements, relationships, queries, and related services.

This does not make interoperability automatic. Two tools can implement different subsets, support different workflows, or attach different operational constraints to the API. But it creates something the SysML ecosystem badly needed: a standard boundary for connecting modeling repositories to analysis, simulation, requirements, PLM, ALM, reporting, and automation services.

The API also matters for AI-assisted engineering. An agent is more useful when it operates on explicit model elements through controlled services than when it only produces plausible text. The model gives the interaction a structure that engineers can inspect, compare, validate, and reject. I discuss this broader shift in [my SLE 2026 keynote, "We built the languages. That was the easy part."]({{ site.url }}/talks/sle-2026-we-built-the-languages/).

## What SysML v2 does not solve by itself

A standard language is necessary infrastructure. It is not a method, an adoption plan, or a guarantee of useful models.

SysML v2 does not decide:

- which engineering questions your models must answer;
- which concepts and viewpoints different roles should use;
- how model quality is reviewed and governed;
- how responsibilities are divided across teams and suppliers;
- how existing SysML v1, Capella, requirements, simulation, and PLM assets should connect;
- how much of the language each practitioner needs to learn;
- which tool experience will make the practice usable at scale.

This is why I remain convinced that **language, method, and tool must be considered together**. Capella and Arcadia have repeatedly shown the value of methodological guidance in industrial MBSE. SysML v2 creates new possibilities for expressing and integrating such guidance, but it does not remove the need for it.

The [Capella and Arcadia guide]({{ site.url }}/capella-arcadia/) explains this distinction in depth and presents several ways a proven method-led practice can complement a SysML v2 foundation.

## Is SysML v2 ready for industrial use?

The standard is formal. Industrial readiness is a separate, contextual question.

A team can start a meaningful SysML v2 pilot today. A large organization should still evaluate the maturity of the complete environment it needs: language coverage, model persistence, graphical and textual editing, APIs, access control, collaboration, performance, validation, migration, reporting, deployment, support, and long-term governance.

Be wary of a single "SysML v2 compliant" checkbox. Conformance has several dimensions, and useful coverage depends on your engineering scope. Ask which language concepts, standard libraries, notations, API services, and interchange scenarios are supported, then test them with representative models.

The [official SysML v2 release repository](https://github.com/Systems-Modeling/SysML-v2-Release) provides specification material, examples, libraries, and reference implementation resources. It is a useful complement to the normative OMG pages when evaluating concrete behavior.

## A pragmatic adoption path

I would approach adoption as an engineering change, not as a file conversion project.

1. **Start from decisions and pain points.** Identify what must become more consistent, traceable, collaborative, or automatable.
2. **Choose a bounded pilot.** Use a representative subsystem and a real engineering question, while keeping the organizational blast radius manageable.
3. **Map the existing practice.** Inventory profiles, libraries, viewpoints, validation rules, integrations, and deliverables before discussing migration tooling.
4. **Evaluate language and tool coverage together.** Test the SysML v2 concepts and workflows that the pilot actually needs.
5. **Design the integration boundary.** Decide where the standard API, textual exchange, or dedicated connectors fit into the engineering system.
6. **Capture the method.** Define guidance, viewpoints, examples, reviews, and ownership instead of exposing the whole language to every user.
7. **Scale from evidence.** Measure usability, model quality, interoperability, and learning effort before expanding the scope.

This path also allows SysML v1, Capella, and SysML v2 practices to coexist during a transition. Replacing everything at once is rarely the only credible strategy.

## Why an open-source SysML v2 tool matters

A new standard creates a short period during which tools, practices, libraries, and integrations are still taking shape. Open source makes the implementation inspectable and gives organizations a way to collaborate on the common foundation before those choices harden behind proprietary boundaries.

[Eclipse SysON]({{ site.url }}/syson/) is an open-source, web-based SysML v2 modeling project initiated by Obeo and CEA and built on Sirius Web. Its goal is broader than drawing SysML v2 diagrams: graphical, textual, form-based, and tabular editors operate on the model, with extensibility and the standard API as first-class concerns.

For the project, governance, source code, releases, and contribution paths, the [Eclipse SysON project](https://eclipse.dev/syson/) is the reference. For organizations evaluating customization, deployment, support, or an industrial engagement, [Obeo presents its SysON offerings and open-innovation approach](https://www.obeosoft.com/en/products/syson/).

This distinction is deliberate. Eclipse is where the open-source project lives. Obeo is one of the places where an organization can obtain productization and engineering support around it.

Our goal at Obeo is to provide a strong, fully open-source platform for SysML v2 because we believe its promises of interoperability and a continuous digital thread cannot be fulfilled without one. Modeling itself should be free and accessible: common ground and a level playing field for every tool. It is up to vendors to provide value on top of it, and there are plenty of opportunities to do so.

The journey is documented in several talks and articles on this site:

- [the original Obeo and CEA collaboration around Sirius Web, Papyrus, and SysON]({{ site.url }}/modeling/sirius-papyrus-web-new-era-collaborative-engineering-tools/);
- [the MODELS 2024 demonstrations of Sirius Web and SysON]({{ site.url }}/modeling/models2024/);
- [Open Source MBSE at Scale, from industry-proven tools to web-native SysML v2]({{ site.url }}/talk/IEEE-ISSE25/);
- [the SLE 2026 reflection on languages, platforms, practices, and agents]({{ site.url }}/talks/sle-2026-we-built-the-languages/).

## The point is not to adopt a language in isolation

SysML v2 gives systems engineering a modern language foundation, a standard textual notation, a graphical notation, reusable libraries, and a standard API. Those are substantial advances.

The value will come from what organizations build around them: focused methods, usable views, trusted integrations, collaborative practices, and models that support real decisions.

The standard is now formal. The next phase is not waiting for SysML v2 to exist. It is learning how to practice it well.
