---
layout: page
title: "Understanding Capella, Arcadia, and their place in MBSE"
seoTitle: "Capella and Arcadia: a practical guide to method-led MBSE"
description: "Understand how the Arcadia method and Eclipse Capella work together, how they differ from SysML, and how to evaluate them for an industrial MBSE practice."
permalink: /capella-arcadia/
canonical: https://cedric.brun.io/capella-arcadia/
lang: en
translation_fr: /fr/capella-arcadia/
tags:
  - capella
  - mbse
  - obeo
  - sirius-web
cluster: capella-arcadia
intent: "Understand Arcadia and Capella, then assess whether method-led MBSE fits an engineering organization"
primaryQuery: "Capella Arcadia MBSE"
secondaryQueries:
  - "what is Arcadia method"
  - "what is Eclipse Capella"
  - "Capella vs SysML"
  - "Arcadia and SysML v2"
  - "Capella web collaboration"
audience: "Systems engineering leaders, system architects, MBSE practitioners, tool teams, and organizations evaluating Capella or Arcadia"
maturityStage: "understanding and evaluation"
pagePromise: "Separate method, language, tool, and platform choices, then provide a practical path for adopting Capella and Arcadia"
proof:
  - "industrial deployments of Arcadia and Capella across complex engineering domains"
  - "experience contributing to Capella, Sirius, and the surrounding ecosystem"
  - "community feedback through Capella Days, training, and integration projects"
businessGoal: "Establish a stable reference point for the Capella, Arcadia, and method-led MBSE content cluster"
nextStep:
  - "/modeling/rising-adoption-of-MBSE-capella/"
  - "/modeling/capella-days-2024/"
  - "/mbse/ai-for-capella-agentic-ai-as-a-first-step/"
  - "/syson/"
image:
  thumb: blog/2026/capella-arcadia/arcadia-engineering-perspectives.webp
---

Capella and Arcadia are often named together, which can make them sound like two versions of the same thing. They are not.

**Arcadia is a model-based engineering method. [Eclipse Capella](https://mbse-capella.org/) is the open-source workbench that implements and supports that method.** The method structures the questions engineers ask, the perspectives they build, and the reasoning that connects operational needs to a physical architecture. The tool provides the language, views, guidance, validation, and engineering environment needed to put that approach into practice.

This distinction is more than vocabulary. A modeling language can define what may be expressed without explaining when to express it, in which order to investigate a problem, or how several engineering roles should work together. A tool can draw diagrams without creating a coherent practice. Arcadia and Capella were designed so that method, language, and tool reinforce one another.

That approach has been deployed in demanding industrial contexts for years. It also raises new questions as SysML v2, web-based modeling, digital threads, and AI-assisted engineering mature. Should an organization adopt Capella, a SysML tool, or both? Can Arcadia be used with SysML v2? How should a desktop modeling practice evolve toward more connected and collaborative environments?

This page provides a framework for answering those questions without confusing a method, a standard, and a product.

<figure>
    <a href="{{ site.url }}/images/blog/2026/capella-arcadia/arcadia-engineering-perspectives.webp">
      <img src="{{ site.url }}/images/blog/2026/capella-arcadia/arcadia-engineering-perspectives.webp" alt="Arcadia engineering perspectives connecting operational analysis, system need analysis, logical architecture, and physical architecture through requirements and viewpoints">
    </a>
    <figcaption>Arcadia connects the understanding of operational needs to logical and physical architecture, while requirements and engineering viewpoints cut across the whole reasoning process.</figcaption>
</figure>

## Start by separating method, language, tool, and practice

Four concepts are usually mixed together in MBSE discussions.

A **method** organizes engineering reasoning. It identifies the questions to answer, the relationships to preserve, the perspectives to build, and the checks that help teams move from a need to a justified architecture.

A **modeling language** defines concepts and semantics: functions, components, exchanges, interfaces, capabilities, states, requirements, and the relationships between them. It determines what a model can express.

A **tool** lets engineers create, navigate, validate, transform, and communicate those models. Its user experience can either reinforce the method or leave users alone in front of a generic metamodel.

An **engineering practice** is what an organization actually does: roles, reviews, decision rights, model governance, integration with other disciplines, training, configuration management, and expected deliverables.

Arcadia is primarily the method, together with the concepts needed to apply it. Capella is the tool and dedicated modeling environment. Neither removes the need to define an organizational practice.

This is why buying or downloading an MBSE tool does not amount to adopting MBSE. The lasting change occurs when teams share a way to formulate needs, compare architectural choices, justify decisions, and connect the model to the rest of engineering.

## What is Arcadia?

[Arcadia](https://mbse-capella.org/arcadia.html) stands for Architecture Analysis and Design Integrated Approach. It is a model-based method for engineering systems, hardware, and software architectures. It was created from industrial systems engineering experience at Thales and later made available as part of the Capella ecosystem.

Arcadia structures architecture reasoning through complementary perspectives:

1. **Operational Analysis:** what do the users and other operational actors need to accomplish, in which situations and under which constraints?
2. **System Need Analysis:** what must the system do for those actors, which services and functions must it provide, and where is its boundary?
3. **Logical Architecture:** how can the system work independently of final implementation choices, and how should responsibilities be organized logically?
4. **Physical Architecture:** how will the system be developed and built through hardware, software, people, facilities, and other physical resources?
5. **Building strategy:** how should the architecture be organized into configuration items and implementation or integration units?

These perspectives are often presented in sequence because each one provides useful input to the next. Arcadia is not a mandatory waterfall. Its [official questions and answers](https://mbse-capella.org/arcadia-qna.html) explicitly allow iterative, incremental, reuse-driven, bottom-up, and middle-out approaches while preserving the logical dependencies between engineering concerns.

Requirements do not form an isolated phase beside this progression. Operational needs, functional and non-functional expectations, architecture choices, and requirements inform one another. The purpose is to confront requirements with an architecture early enough to assess feasibility and robustness, rather than treating the model as an illustration produced after the decisions.

## Why the perspectives matter

The perspectives create deliberate changes of question.

Operational Analysis resists the temptation to define the system too early. It asks what actors are trying to achieve before assigning behavior to a proposed solution.

System Need Analysis identifies the expected contribution of the system and its interactions with users and external systems. It clarifies what belongs inside and outside the system boundary.

Logical Architecture explores how functions and responsibilities could be organized without prematurely committing to technologies or implementation components. It creates space for architectural trade-offs.

Physical Architecture then allocates behavior and interfaces to concrete implementation elements. The links between perspectives make it possible to follow why a physical component exists and which needs its functions support.

This progression gives teams a common vocabulary for reviews. Instead of debating whether a box belongs on a diagram, they can ask whether an operational activity has been turned into the right system capability, whether a logical responsibility is justified, or whether a physical allocation satisfies the relevant constraints.

The model can then become more than a deliverable. **The model becomes the common table.** People with different roles can navigate from an operational need to a function, component, interface, scenario, or requirement and discuss the same engineering object rather than comparing disconnected slides.

## Viewpoints connect specialist concerns to architecture

Architecture is shaped by concerns that cannot be reduced to one hierarchy: safety, security, performance, cost, mass, timing, maintainability, product-line variability, integration, and many others.

Arcadia is viewpoint-driven. A viewpoint formalizes how one such concern is evaluated against the architecture. This keeps specialist analysis connected to the shared system model while preserving the concepts and calculations needed by that discipline.

The objective is not to put every piece of engineering information into one enormous metamodel. It is to define controlled connections:

- which architecture elements a specialist concern depends on;
- which additional properties or concepts are required;
- which analyses and rules can be executed;
- which results influence an architectural choice;
- how that reasoning remains traceable during change.

This is an important part of tailoring Arcadia. The core method provides a strong structure, but every organization has domain constraints, lifecycle standards, review gates, and engineering specialties that need to be integrated deliberately.

## What is Eclipse Capella?

[Eclipse Capella](https://projects.eclipse.org/projects/polarsys.capella) is the open-source graphical modeling workbench that implements Arcadia. The Eclipse Foundation classifies it as a mature project. Its source code, releases, project governance, contribution process, and Eclipse Public License 2.0 licensing are public.

Capella provides a dedicated language and user experience for systems architecture rather than exposing a generic modeling canvas. Its [add-ons and extensions](https://mbse-capella.org/addons.html) broaden that ecosystem beyond the core workbench. Its capabilities include:

- an embedded methodological browser and guidance through Arcadia perspectives;
- semantic model navigation and contextual properties;
- architecture, dataflow, functional-chain, sequence, state, class, interface, and tree representations;
- filters, layers, and computed simplifications for managing complex views;
- validation rules and transitions between engineering perspectives;
- patterns, libraries, reuse, and system-to-subsystem transition mechanisms;
- extension points for additional viewpoints, representations, rules, and integrations.

Capella is built as an Eclipse desktop application and relies on technologies including Eclipse Sirius for graphical modeling. [Capella Studio](https://mbse-capella.org/download.html) provides an SDK for developing extensions and specialized viewpoints.

The core project should be distinguished from the broader ecosystem. Open-source and commercial add-ons provide capabilities such as document generation, requirements management, collaboration, simulation, property management, scripting, and connections to other engineering systems. Organizations need to verify the license, maintenance, compatibility, and support model of each add-on separately from Capella itself.

## Mature, widely used, and still moving

Capella is not an emerging tool waiting for its first serious deployments. It has accumulated years of industrial use across aerospace, defense, transportation, energy, space, semiconductors, and other domains where architecture decisions have long consequences. The method is taught, documented, and discussed through books, training, webinars, case studies, a worldwide practitioner community, and Capella Days. This breadth matters: teams can learn not only from product documentation, but from organizations that have already confronted scale, integration, governance, and adoption.

Maturity should not be confused with immobility. Capella remains an active project with new releases, direct investment in its foundations, and work extending its place in the engineering ecosystem. In 2026, [Obeo strengthened its commitment to the future of Capella](https://blog.obeosoft.com/obeo-strengthens-its-commitment-to-the-future-of-capella) through several concrete initiatives:

- direct contributions to Capella 7.1 focused on robustness, security, maintainability, Java 21, and internationalization;
- an Arcadia library for SysML v2 developed with Thales as a first foundation for better interoperability;
- the joint open-sourcing of the Capella add-on for Simulink integration;
- continued work on controlled, agentic AI integration with Capella;
- preparation of the tenth edition of Capella Days, reflecting a community that continues to share experience and shape what comes next.

These are not the signals of a project entering maintenance-only mode. They connect the proven Capella workbench to current concerns: platform sustainability, international adoption, simulation, SysML v2, AI, and open collaboration.

**Capella is mature, widely used, still dynamic, and here to stay.** That does not mean its architecture or ecosystem will remain frozen. It means the accumulated method, models, skills, community, and industrial investment provide a durable base from which Capella can keep evolving.

## Why methodological guidance changes adoption

A general-purpose language gives flexibility. It can also give a new team too many valid ways to start.

Capella narrows that space. The explorer, diagrams, available actions, validation rules, and transitions reflect Arcadia concepts and perspectives. Users are not expected to invent a complete modeling organization before describing their first architecture.

This guidance has several benefits:

- newcomers can learn a recognizable progression rather than a catalogue of notation elements;
- models created by different teams are more likely to use compatible structures;
- reviews can follow engineering intent instead of diagram aesthetics;
- traceability is created as the architecture is developed, not reconstructed afterward;
- training and experience reports can be reused across organizations;
- extensions can focus on domain concerns while preserving a common architectural backbone.

Guidance is not the same as automation. Arcadia does not decide where the system boundary belongs, which logical architecture is best, or whether a safety argument is sufficient. It creates a disciplined space in which engineers can make and justify those decisions.

It also has to be tailored with care. Too little guidance leaves users with inconsistent models. Too much process can turn the model into a compliance exercise. A successful deployment identifies which Arcadia principles must remain common and where projects need freedom.

## Capella and SysML are not equivalent choices

SysML and Arcadia/Capella overlap, but they do not occupy the same category.

SysML is a general-purpose standard modeling language for systems engineering. It provides a broad semantic vocabulary and, with SysML v2, a modern textual and graphical notation, a KerML foundation, libraries, and a standardized API. It does not prescribe one systems engineering method.

Arcadia combines a focused architecture method with concepts adapted to that method. Capella implements those concepts in a dedicated workbench. It is not a SysML profile, even though its language and diagrams have been strongly influenced by UML, SysML, and architecture frameworks. The official [Capella and SysML comparison](https://mbse-capella.org/arcadia_capella_sysml_tool.html) describes how Arcadia simplifies, specializes, or enriches concepts to stay close to systems architecture practice.

This produces a practical trade-off:

| Question | SysML | Arcadia and Capella |
|---|---|---|
| Primary role | Standard, general-purpose systems modeling language | Method-led system architecture engineering |
| Method | No mandatory method | Arcadia provides explicit perspectives and guidance |
| Scope | Broad modeling and interoperability foundation | Focused operational analysis and architecture definition |
| Tool experience | Depends on the selected implementation and configuration | Capella embodies Arcadia in its vocabulary, views, and actions |
| Interoperability | Standard language and API are central objectives | Integrations and transformations depend on the required boundary |
| Tailoring | Profiles, libraries, viewpoints, and tool extensions | Arcadia tailoring, Capella viewpoints, add-ons, and integrations |

The decision should therefore not be reduced to counting diagram types. Ask whether the priority is a standardized semantic and integration foundation, a proven method-led architecture practice, or a deliberate combination of both.

## Arcadia and SysML v2 can be complementary

SysML v2 does not make the need for methods disappear. A standard language can improve semantic consistency and interoperability while leaving organizations free to define how engineers should use it.

Arcadia contributes exactly that missing dimension: an architecture reasoning process, a progression of perspectives, dedicated views, and a practice that has accumulated industrial experience.

Several forms of complementarity are possible:

- use Capella and Arcadia for architecture work while exchanging selected information with a wider SysML ecosystem;
- keep Capella as an authoritative environment for established programs and introduce SysML v2 for new collaboration or integration boundaries;
- map specific Arcadia concepts to SysML v2 where there is a clear engineering and semantic purpose;
- build an Arcadia-oriented experience on top of a SysML v2 platform, using libraries, specialized views, actions, and vocabulary;
- connect the environments through services rather than attempting a complete model conversion.

None of these options is automatic. Similar-looking concepts do not guarantee lossless equivalence. Identity, decomposition, behavioral semantics, viewpoint data, graphical intent, extensions, and configuration history all need explicit treatment.

The right architecture begins with a use case: which teams must collaborate, which information must cross the boundary, which system remains authoritative, and which decisions must remain traceable?

For the language and standard side of this decision, see [What SysML v2 changes for MBSE]({{ site.url }}/sysml-v2/).

## Where SysON and the web fit

[Eclipse SysON]({{ site.url }}/syson/) is an open-source, web-based SysML v2 modeling environment built on Sirius Web. Capella is a mature, desktop-based Arcadia environment. One is not currently a drop-in web replacement for the other.

The interesting long-term question is how to preserve the methodological value learned through Capella while taking advantage of a standard SysML v2 foundation and web-based collaboration.

Our experiments around Sirius Web and SysON show one possible direction: provide an Arcadia-oriented library and customize the explorer, views, actions, and vocabulary presented to users, while keeping a SysML v2 semantic model underneath. This can offer a method-aware experience without forcing users to start from a generic standard tool.

That work should be understood as exploration, not a claim that existing Capella models can already move transparently to SysON. Production adoption requires explicit answers about semantic coverage, migration, model scale, collaboration, extensions, configuration management, and long-term support.

For organizations with a successful Capella deployment, the sensible strategy is usually progressive:

1. protect the current engineering practice and model assets;
2. identify collaboration or integration problems that the web can solve;
3. test a bounded exchange or method-specific view;
4. measure semantic loss, user effort, and operational constraints;
5. expand only where the new boundary creates real value.

The future does not have to be a forced choice between a useful method and an open standard. The value can move upward into methods, domain viewpoints, integrations, analysis, and user experience while the common modeling substrate becomes more interoperable.

## Connecting Capella to the engineering ecosystem

A Capella model becomes more valuable when it participates in engineering work beyond the architecture team.

Common integration concerns include:

- requirements repositories and traceability;
- PLM and product-structure management;
- simulation and trade-off analysis;
- safety, cybersecurity, performance, and specialty engineering;
- software and hardware development environments;
- document and report generation;
- model review, baselines, and multi-user collaboration;
- automation through scripts and services;
- data access for dashboards, analytics, and AI assistants.

For each connection, define which system owns the data, how identifiers remain stable, how changes are synchronized, and what happens when an integration fails. Avoid turning the Capella model into an uncontrolled copy of every external repository.

The 2018 [Siemens and Obeo partnership]({{ site.url }}/obeo/siemens-obeo-partnership/) already illustrated the strategic objective: use architecture models throughout the product lifecycle rather than leaving them as isolated documents. At [Capella Days 2024]({{ site.url }}/modeling/capella-days-2024/), this had become much more concrete through digital threads, co-engineering, diagnostics, simulation, and operational use cases.

## Collaboration is a practice before it is a feature

Sharing a model repository does not automatically produce collaboration.

Teams need explicit answers about:

- model ownership and write authority;
- decomposition between teams, suppliers, and subsystems;
- review, approval, baseline, and release workflows;
- conflict resolution and change impact;
- confidentiality and access control;
- compatibility between Capella, add-ons, and model versions;
- recovery, auditability, and long-term archiving;
- how non-modelers consume and comment on architecture information.

The [Capella Days 2025 program]({{ site.url }}/modeling/capella-days-2025/) showed how the ecosystem is moving from isolated tool adoption toward an enterprise backbone: integrations across disciplines, model reuse, product lines, safety and cybersecurity loops, and knowledge made accessible to non-specialists.

The tool can support those workflows, but the organization must define them. A small architecture team, a multi-company defense program, and a product-line organization require different collaboration models.

## AI benefits from a method-aware model

Structured models give AI systems better context than a collection of disconnected documents. Arcadia adds another useful layer: the model contains not only entities and relationships, but an engineering progression and vocabulary that help interpret why information exists.

This creates useful assistance scenarios: navigating dependencies, finding architecture context, preparing queries, drafting documentation, checking consistency, or proposing bounded changes.

It does not make AI a systems engineer. Decisions about needs, architecture, safety, trade-offs, and acceptance remain human responsibilities. Any AI integration must preserve access control, traceability, review, and explicit limits on what an agent can read or change.

Our work on [Agentic AI as a first step for Capella]({{ site.url }}/mbse/ai-for-capella-agentic-ai-as-a-first-step/) follows this principle: expose selected capabilities through controlled services, let engineers validate outcomes, and build trust from useful bounded interactions.

## A practical adoption path

Arcadia and Capella adoption should be managed as a change in engineering practice, not a software rollout.

1. **Choose a decision problem.** Select an architecture question where better shared reasoning can create measurable value.
2. **Define the modeling objectives.** State what the model must help teams understand, decide, verify, or produce.
3. **Scope the Arcadia perspectives.** Decide which operational, system, logical, and physical concerns are needed for the first use case.
4. **Establish conventions.** Define naming, decomposition, diagram purpose, review rules, and required traceability.
5. **Train through a representative model.** Teach the method and tool together using domain-relevant work, not notation exercises alone.
6. **Prove one integration.** Connect a downstream analysis, requirement source, report, or collaboration workflow that demonstrates the model's operational value.
7. **Plan governance and support.** Assign ownership for templates, add-ons, versions, validation rules, migrations, and user assistance.
8. **Measure decisions and flow.** Track review quality, discovered inconsistencies, rework, onboarding, and reuse rather than the number of diagrams produced.
9. **Scale from evidence.** Extend to more teams and specialties only after the first practice survives real changes and reviews.

This path makes the initial scope manageable without reducing it to a disposable demonstration.

## How to evaluate Capella for your organization

Before selecting Capella, evaluate the whole intended solution.

### Method fit

- Does Arcadia's focus on operational needs and architecture match your engineering objectives?
- Which parts of the method need tailoring, and which should remain common?
- Can engineering leaders support the reviews and organizational changes required?

### Tool and model fit

- Can representative models be navigated, edited, validated, and reviewed with acceptable performance?
- Do the core representations cover the required architecture concerns?
- Which add-ons, viewpoints, scripts, or integrations are essential?

### Lifecycle fit

- How will models be decomposed, versioned, baselined, migrated, and archived?
- How will requirements, PLM, simulation, safety, software, and hardware work connect to them?
- Can non-Capella users access the architecture information they need?

### Operating model

- Who maintains the method configuration, templates, extensions, and integrations?
- Which components are open source, commercial, or organization-specific?
- What support, training, and migration commitments are available?

### Future options

- Which data must remain portable or accessible through stable interfaces?
- Where could SysML v2 improve interoperability without disrupting the current practice?
- Which web or AI-assisted workflows solve a real problem rather than following a technology trend?

The answer may be to adopt Capella broadly, use it for a bounded architecture scope, combine it with other modeling environments, or retain an existing practice. The important thing is to make the method and lifecycle choices explicit.

## The method is what survives the tool

Capella matters because it made Arcadia concrete, teachable, and usable at industrial scale. Arcadia matters because it gives engineers more than a vocabulary: it gives them a progression for turning operational needs into justified architecture.

Around them, an ecosystem of training, books, extensions, integrations, case studies, events, maintainers, and professional services carries the practice from one team to another. This transmission is as important as the metamodel.

When adoption works, people eventually stop discussing the tool itself. They use the shared language to compare options, ask questions, and make decisions together.

Capella has reached the point where maturity and renewal reinforce one another: industrial experience stabilizes the foundations, while new contributors, integrations, standards, and forms of interaction keep the ecosystem relevant. Its future is not based on preserving a desktop application unchanged; it is based on carrying forward a proven method and a living body of engineering knowledge.

That is the durable place of Capella and Arcadia in MBSE: not as an isolated notation or a diagram factory, but as a method-aware environment for building architecture as a shared engineering asset.
