---
layout: page
title: "Designing a modeling platform for your domain"
seoTitle: "Custom web modeling platforms: build, buy, or configure?"
description: "A practical guide to choosing, designing, integrating, and operating a web modeling platform adapted to your domain, users, models, and engineering workflows."
permalink: /modeling-platforms/
canonical: https://cedric.brun.io/modeling-platforms/
lang: en
translation_fr: /fr/modeling-platforms/
tags:
  - sirius-web
  - ecore
  - mbse
  - obeo
cluster: modeling-platforms
intent: "Decide whether to buy a modeling tool, configure a platform, or build a domain-specific solution"
primaryQuery: "custom modeling platform"
secondaryQueries:
  - "web modeling platform"
  - "build or buy modeling tool"
  - "graphical DSL editor"
  - "collaborative modeling architecture"
audience: "Engineering leaders, tool architects, domain experts, and teams responsible for modeling infrastructure"
maturityStage: "problem framing and evaluation"
pagePromise: "Provide a decision framework and architecture for a modeling platform that fits a real engineering practice"
proof:
  - "experience building domain-specific modeling tools"
  - "open-source Eclipse modeling technologies"
  - "desktop-to-web platform migration"
businessGoal: "Establish a stable reference point for the modeling platforms and Sirius Web content cluster"
nextStep:
  - "/modeling/solutions-to-build-graphical-modeler/"
  - "/modeling/sirius-web-resfull-api-proto/"
  - "/syson/"
image:
  thumb: blog/2026/modeling-platforms/sirius-web-modeling-platform.webp
---

A modeling platform is not simply a diagram editor. It is the technical and experiential foundation on which an organization captures domain knowledge, guides users through a method, presents several views of the same information, enforces rules, and connects models to the rest of the engineering system.

That distinction changes the first question. The decision is rarely just, "Should we build or buy a tool?" A more useful question is: **which parts of our modeling practice are standard, which parts are specific to our domain, and which parts create a real advantage?**

For some organizations, an existing product is the right answer. Others need to configure a platform around a dedicated language and workflow. A smaller number have requirements that justify building core technology themselves. The cost and risk are very different in each case.

This page offers a framework for making that decision and for designing a web-based modeling platform when configuration or custom development is justified.

<figure>
    <a href="{{ site.url }}/images/blog/2026/modeling-platforms/sirius-web-modeling-platform.webp">
      <img src="{{ site.url }}/images/blog/2026/modeling-platforms/sirius-web-modeling-platform.webp" alt="Custom Sirius Web modeling platform showing a domain model explorer, value-chain diagram, and contextual properties">
    </a>
    <figcaption>A modeling platform brings domain concepts, dedicated representations, editing tools, and contextual information into one coherent experience.</figcaption>
</figure>

## What is a modeling platform?

A modeling tool lets users manipulate models. A modeling platform provides reusable capabilities for creating one or several such tools.

The platform usually includes several layers:

- a **semantic foundation** for defining and storing domain concepts and relationships;
- **commands and rules** that control how the model can change;
- **representations** such as diagrams, trees, tables, forms, matrices, dashboards, or documents;
- **navigation and guidance** that help each role find the right information and perform the right task;
- **collaboration and persistence** services for sharing, reviewing, versioning, and governing models;
- **integration boundaries** for requirements, PLM, ALM, simulation, data science, reporting, automation, and AI;
- **operational capabilities** for identity, permissions, deployment, monitoring, backups, upgrades, and support.

A product may package all these concerns for a particular language or method. A platform exposes enough of them to let a tool-building team create an experience for its own domain.

This is why a platform should not be evaluated only by the quality of its diagram component. Diagramming is visible and important, but model consistency, extensibility, operations, and integration determine whether the result can become durable infrastructure.

## Start from the practice, not the editor

Teams often begin a modeling initiative by listing shapes, menus, and properties. That is understandable: those are the parts everyone can see. It is also a reliable way to reproduce an existing tool without questioning the work it supports.

Start instead from the decisions and interactions the platform must improve:

- Which questions should the model answer?
- Who creates, reviews, approves, and consumes each kind of information?
- Which concepts must have a precise shared meaning?
- Which views help each role without exposing the whole model?
- Which rules should prevent an invalid change, and which should merely warn?
- Where does information originate, and which system remains authoritative for it?
- Which deliverables, analyses, or downstream actions must the model produce?
- What must remain understandable and maintainable in ten years?

These questions define the semantic model, the workflows, and the integration boundaries. The editor follows from them.

A good domain-specific tool does not merely offer fewer buttons than a generic tool. It uses the vocabulary of its users, makes useful paths obvious, and embodies enough of the practice to help people make consistent decisions.

## Buy, configure, or build?

There are three broad strategies. Most real projects combine them, but one should remain dominant.

| Strategy | Best fit | Main advantage | Main risk |
|---|---|---|---|
| Buy a product | The language, method, and workflows are mostly standard | Fastest path to established capabilities and support | Forcing a specific practice into a product that cannot express it well |
| Configure a platform | The domain and views are specific, but infrastructure needs are common | Focus investment on semantics and user experience | Underestimating extensions, operations, and long-term ownership |
| Build core technology | The platform itself is differentiating or constrained in a way existing foundations cannot support | Maximum architectural control | Rebuilding years of interaction, collaboration, and maintenance work |

**Buy** when established products cover the language, method, scale, integrations, and deployment constraints with acceptable adaptation. Configuration may still be needed, but the product remains the center of gravity.

**Configure a platform** when your vocabulary, viewpoints, rules, or workflows are specific, while needs such as model persistence, diagrams, forms, tables, validation, collaboration, and web application infrastructure are not. This is the space in which model-driven tooling platforms are most valuable.

**Build from scratch** only when a critical requirement cannot credibly be met by an existing product, framework, or platform. A diagram library can make the first demonstration look easy. The hidden cost appears later in selection behavior, layout, undo and redo, copy and paste, accessibility, concurrency, migration, permissions, performance, testing, and upgrades.

The right decision minimizes the amount of undifferentiated infrastructure your organization has to own.

## Why move modeling to the web?

Putting an editor in a browser is not, by itself, a strategy. The web becomes valuable when it changes access, collaboration, integration, and delivery.

A web-based platform can provide:

- access through a URL instead of a workstation installation;
- links to a specific project, representation, or model element;
- one deployed version for a group of users;
- server-side control over persistence and shared services;
- easier participation for occasional users and reviewers;
- a natural boundary for APIs and integration with other web systems;
- faster delivery of improvements to every user;
- collaboration around the same model rather than exchanged files.

These benefits are not automatic. The architecture must handle latency, concurrent changes, long-running computations, partial loading, permissions, failures, and the operational cost of a shared service. A desktop application can hide many assumptions inside one process and one workspace. A web platform has to make them explicit.

The move is worthwhile when shared access and connected workflows matter more than preserving desktop assumptions. The [Sirius and Papyrus web transition presented at EclipseCon 2023]({{ site.url }}/modeling/sirius-papyrus-web-new-era-collaborative-engineering-tools/) illustrates how this shift reopens architecture, usability, collaboration, and interoperability decisions.

## The model and its views must remain separate

One of the most important architectural choices is to keep domain meaning separate from its representations.

The semantic model captures concepts, relationships, constraints, and identity. A diagram selects and arranges part of that model for a purpose. A table compares a set of elements. A form guides a focused edit. A dashboard computes an overview. They are different projections of the same engineering knowledge.

When a representation becomes the model, several problems appear:

- information that is not visible is difficult to manage;
- the same concept is duplicated between views;
- integrations depend on graphical details;
- consistency rules become tied to one editor;
- adding a new representation requires changing the underlying data.

A platform should let tool builders define which semantic elements a view exposes, how they appear, what operations users can perform, and how those operations modify the model. The same command and validation logic should remain usable from other views and APIs.

This separation is central to [Eclipse Sirius](https://eclipse.dev/sirius/): a modeler definition describes how domain data is projected into representations and how users can interact with it. [Sirius Web](https://eclipse.dev/sirius/sirius-web.html) carries those principles into a web stack; its [source repository](https://github.com/eclipse-sirius/sirius-web) is the place to inspect the implementation and contribute code.

## Collaboration is more than simultaneous editing

Real-time co-editing is visible and impressive, but it is only one collaboration concern.

Engineering teams also need to know:

- who can see or modify each scope;
- how a change is reviewed and explained;
- whether two changes conflict semantically, not only technically;
- how baselines, branches, or releases are represented;
- how suppliers exchange bounded parts of a model;
- how comments, decisions, and evidence remain connected to model elements;
- how users recover from mistakes or service failures;
- which notifications help without creating noise.

The right collaboration model depends on the organization. A small internal team and a multi-company program do not need the same isolation, approval, or configuration-management mechanisms.

Treat these workflows as domain requirements. Do not assume that adding WebSockets or a shared database settles them.

## Integration defines the platform boundary

A useful model rarely lives alone. It exchanges information with requirements repositories, source control, PLM, ALM, simulation, test management, document generation, data platforms, and increasingly AI-assisted services.

For each connection, decide:

1. which system owns the information;
2. whether the interaction is synchronous, asynchronous, or file-based;
3. how identity is preserved across systems;
4. which changes can flow in each direction;
5. how failures and partial updates are detected;
6. what users can inspect when an automated action changes the model.

APIs are necessary, but an API inventory is not an integration architecture. Stable identifiers, transactions, permissions, event semantics, and error handling matter just as much.

The [Sirius Web REST API prototype]({{ site.url }}/modeling/sirius-web-resfull-api-proto/) explored how [EMF](https://eclipse.dev/emf/) models could be exposed to familiar clients and formats. The [Sirius Web and Jupyter demonstration]({{ site.url }}/modeling/sirius-web-jupyter-notebook/) illustrates the larger objective: connect design, simulation, and analysis without turning each exchange into manual file handling.

## Performance is part of trust

Large models expose architecture problems, but raw model size is not the only useful metric. A platform should be tested with representative workflows:

- opening a project and the first useful view;
- navigating from search results to a model element;
- expanding a tree with deep or wide structures;
- rendering and editing dense diagrams;
- running validation or impact analysis;
- applying a change that affects several representations;
- serving several concurrent users;
- importing, exporting, or migrating realistic data.

Predictability matters. An operation that sometimes takes one second and sometimes thirty creates hesitation even if its average looks acceptable. Users need feedback for long operations and confidence that repeating a command will not make the situation worse.

Performance therefore belongs in the user experience, data architecture, and observability strategy from the beginning. It cannot be delegated to a final optimization phase.

## Migrating a desktop tool requires product decisions

A desktop-to-web migration should not begin as a screen-by-screen rewrite.

Inventory the existing tool in four groups:

- **domain assets:** metamodels, libraries, rules, transformations, generators, and queries;
- **practice assets:** viewpoints, workflows, review conventions, templates, and training;
- **integration assets:** file formats, APIs, connectors, reports, and automation;
- **desktop assumptions:** workspace mechanics, local state, menus, preferences, and extension points.

The first three groups often carry lasting value. The fourth deserves scrutiny. Some desktop concepts remain useful; others only exist because of the platform on which the original tool was built.

Plan a vertical slice that proves one complete workflow: load representative data, navigate it, edit it through a dedicated view, validate the result, connect one external service, and deploy it under realistic security constraints. This reveals architectural gaps earlier than a broad but shallow port.

## Where Sirius Web fits

[Eclipse Sirius Web](https://eclipse.dev/sirius/sirius-web.html) is an open-source framework for building and deploying web-based modeling studios. Its [source repository](https://github.com/eclipse-sirius/sirius-web) provides reusable Spring Boot backend components and React frontend components, along with a sample application.

It is relevant when an organization needs a dedicated modeling experience rather than a fixed general-purpose editor. The platform provides building blocks for model exploration, diagrams, forms, tables, details views, validation, editing operations, and extensibility. Tool builders concentrate on the domain model, views, behavior, and integrations instead of implementing every interaction from first principles.

The approach preserves an important lesson from Sirius Desktop: define modeling experiences at a higher level and shorten the feedback loop between a tool definition and its use. I described those principles in [Building Graphical Modeling Tools: Approaches to Reducing Complexity]({{ site.url }}/modeling/solutions-to-build-graphical-modeler/).

Sirius Web is not a finished solution for every organization. A production platform still needs decisions about packaging, identity, permissions, persistence, deployment, monitoring, upgrades, migration, support, and the method presented to users. Depending on the project, those capabilities may come from an application built on the framework or from a supported distribution such as [Obeo Enterprise for Sirius](https://www.obeosoft.com/en/products/obeo-enterprise-for-sirius/).

[Eclipse SysON]({{ site.url }}/syson/) is a concrete example: it uses Sirius Web to provide a SysML v2 modeling environment. The [official SysON website](https://mbse-syson.org/) describes the project, while SysON adds the language, libraries, views, rules, workflows, and interoperability concerns of systems engineering.

## A pragmatic delivery path

Treat the platform as a product, even when its users are internal.

1. **Frame the practice.** Identify users, decisions, concepts, views, and authoritative systems.
2. **Choose the dominant strategy.** Buy, configure, or build, with explicit reasons for every custom layer.
3. **Prove a vertical slice.** Deliver one valuable workflow through semantics, UI, persistence, integration, and deployment.
4. **Test with domain experts early.** Validate vocabulary, navigation, guidance, and feedback before expanding language coverage.
5. **Define extension boundaries.** Separate configuration, supported APIs, dedicated code, and forks.
6. **Design operations with the application.** Include security, observability, backups, migration, and upgrades in acceptance criteria.
7. **Measure actual work.** Track task completion, errors, review time, integration reliability, and learning effort, not only feature counts.
8. **Grow from evidence.** Add roles, views, and domains after the architecture and practice survive real use.

This path keeps the first release small without reducing it to a disposable prototype. The objective is not to demonstrate that a diagram can be drawn. It is to demonstrate that the organization can own and evolve a modeling practice.

## The lasting asset is the practice

Technology choices matter. A weak foundation can make every feature expensive. But a platform succeeds when people can use it to share meaning, make decisions, and connect their work.

The semantic model preserves the domain. Views make it understandable. Rules make it dependable. Integrations make it useful beyond the editor. Operations make it available. Governance and training make it durable.

That is why the goal should not be to build a custom modeling tool for its own sake. The goal is to create the smallest platform that can make a valuable modeling practice live, while relying on maintained foundations for everything that does not differentiate the organization.
