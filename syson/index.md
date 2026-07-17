---
layout: page
title: "Eclipse SysON: an open-source SysML v2 modeling environment"
seoTitle: "Eclipse SysON: open-source SysML v2 modeling"
description: "Understand what Eclipse SysON is, how its web-based SysML v2 environment works, what is open source, and how to evaluate it for industrial MBSE."
permalink: /syson/
canonical: https://cedric.brun.io/syson/
lang: en
tags:
  - mbse
  - sysmlv2
  - syson
  - sirius-web
  - capella
  - obeo
cluster: syson
intent: "Understand what Eclipse SysON provides and whether it fits a SysML v2 initiative"
primaryQuery: "Eclipse SysON"
secondaryQueries:
  - "open source SysML v2 tool"
  - "web based SysML v2 modeling"
  - "SysON features"
  - "SysON and Capella"
audience: "MBSE leaders, system architects, systems engineers, and modeling platform teams"
maturityStage: "evaluation"
pagePromise: "Separate the open-source project, its current capabilities, its architecture, and the industrial services available around it"
proof:
  - "Eclipse Foundation project and governance"
  - "public source code, documentation, releases, and issue tracker"
  - "experience building SysON and Sirius Web"
businessGoal: "Establish a stable reference point for the Eclipse SysON content cluster"
nextStep:
  - "/sysml-v2/"
  - "/modeling/models2024/"
  - "/talk/IEEE-ISSE25/"
image:
  thumb: blog/2026/syson/syson-modeling-environment.webp
draft: true
noindex: true
sitemap: false
---

Eclipse SysON is an open-source, web-based modeling environment for creating, editing, and visualizing SysML v2 models. It is built on Eclipse Sirius Web and developed as an Eclipse Foundation project, with public source code, documentation, releases, discussions, and governance.

That short definition matters because several different questions are often mixed together. SysON is an implementation of a modeling environment, not the SysML v2 standard itself. It is an open-source project, not a method. And while organizations can use and extend the project directly, they can also obtain productization, deployment, customization, and support from companies involved in its development.

If you are first trying to understand the language rather than evaluating a tool, start with [what SysML v2 changes for MBSE]({{ site.url }}/sysml-v2/). This page focuses on SysON: why it exists, how it works, what it already enables, and what to verify before adopting it.

<figure>
    <a href="{{ site.url }}/images/blog/2026/syson/syson-modeling-environment.webp">
      <img src="{{ site.url }}/images/blog/2026/syson/syson-modeling-environment.webp" alt="Eclipse SysON web interface showing a SysML v2 model explorer, graphical view, and properties panel">
    </a>
    <figcaption>A SysML v2 model in Eclipse SysON, with the model explorer, a graphical representation, and contextual properties visible in the same web environment.</figcaption>
</figure>

## Why Eclipse SysON exists

SysML v2 changes more than the symbols available in a diagram. Its KerML foundation, textual and graphical notations, standard libraries, and Systems Modeling API create the basis for models that can be exposed through several views and connected to a wider engineering system.

That opportunity needs an implementation people can inspect, test, adapt, and improve together. Obeo and CEA initiated SysON to provide an open-source implementation for the MBSE community. CEA brought its experience with Papyrus and standards; Obeo brought its experience with Sirius, Capella, and web-based modeling platforms. The project now lives under Eclipse Foundation governance.

The goal is not simply to reproduce a desktop diagram editor in a browser. A web environment can reduce installation friction, give teams a shared point of access, and support collaboration around the same model repository. It also creates an architectural foundation for specialized views, integrations, and organization-specific experiences.

The [Eclipse SysON project page](https://projects.eclipse.org/projects/modeling.syson) is the reference for governance, project status, participants, releases, and licensing. The [source code and issue tracker](https://github.com/eclipse-syson/syson) are public on GitHub.

## SysON is built on Sirius Web

SysON uses [Eclipse Sirius Web](https://eclipse.dev/sirius/sirius-web.html) as its modeling platform. Sirius Web supplies reusable capabilities for model exploration, graphical representations, properties, forms, tables, validation, editing operations, and a web application architecture.

SysON adds the systems engineering language and experience on top: the SysML v2 metamodel, standard concepts, libraries, views, creation tools, domain rules, and workflows needed to manipulate system models.

This separation is important for extensibility. A team does not have to fork every part of the application to introduce a focused representation or domain-specific behavior. The platform is designed so that model-based applications can provide different experiences over structured semantic data.

It also means SysON benefits from capabilities developed for a broader family of modeling applications. Conversely, requirements discovered while implementing SysML v2 can strengthen Sirius Web as a platform.

## What can you do with SysON?

SysON provides a project and model environment in which engineers can create SysML v2 elements, navigate their semantic structure, edit properties, and work through graphical and structured representations.

The [SysON user documentation](https://doc.mbse-syson.org/syson/v2026.5.0/user-manual/index.html) describes views for complementary engineering concerns, including general structure, interconnections, action flows, state transitions, sequences, geometry, grids, and hierarchical browsing. Coverage and maturity vary by view and release, so this list should not be read as a claim that every SysML v2 concept is implemented equally.

The practical capabilities to evaluate include:

- creating and organizing SysML v2 projects and model elements;
- navigating definitions, usages, relationships, and containment;
- editing through graphical views and contextual property panels;
- using tables, grids, forms, and other structured representations where available;
- executing validation rules and inspecting model issues;
- importing and exporting supported SysML v2 textual or interchange formats;
- sharing access to a web-hosted modeling environment;
- extending views and workflows for a particular engineering context.

SysON is released frequently. For an exact statement of support, use the documentation matching the version you plan to deploy and test it with a representative model. A generic "supports SysML v2" label is not precise enough for an engineering decision.

## Graphical and textual modeling are complementary

SysML v2 defines both graphical and textual notations. SysON's current strength is an integrated web experience with graphical and structured editors. It also supports parts of the textual syntax in direct editing and exchange workflows, while deeper textual editing capabilities continue to evolve.

This is not a reason to select one notation and exclude the other. Text is useful for precise examples, automation, review, generation, and version-oriented workflows. Diagrams reveal architecture and relationships. Forms and tables focus attention on a bounded question. The value comes from keeping these representations aligned with the same semantic model.

When evaluating SysON, test the transitions between representations. Can an engineer find the semantic element behind a diagram node? Does an edit appear consistently elsewhere? Can a validation result lead back to the relevant element? These workflows matter more than a long inventory of notation symbols.

## What about the standard SysML v2 API?

The Systems Modeling API and Services specification is strategically important to SysON. It defines a standard boundary for accessing model repositories and connecting them with analysis, simulation, requirements, PLM, ALM, reporting, and automation services.

The project is implementing this standard progressively. The [SysON API documentation](https://doc.mbse-syson.org/syson/v2026.5.0/developer-guide/api/api.html) distinguishes the standard REST API work from the GraphQL APIs inherited from the application platform. They should not be treated as interchangeable: one targets interoperability across the SysML v2 ecosystem, while the other supports application and extension needs in the SysON stack.

Before planning an integration, verify the exact API services supported by the release you intend to use. If a required standard service is not available yet, textual exchange or a dedicated integration may still provide a viable boundary, but that choice should be explicit.

## Is SysON really open source?

Yes. SysON is developed in public as an Eclipse project. Its source code, issues, discussions, contribution guide, release history, and licenses are accessible without a commercial agreement. The project is distributed primarily under the Eclipse Public License 2.0, with license details maintained in the repository.

Open source does not mean that deployment, operation, security, integration, migration, or support happen automatically. It means the common modeling foundation can be inspected and changed, and that organizations can collaborate without making one vendor the sole owner of the model editor.

This distinction is central to the project's purpose. SysML v2 promises stronger interoperability and a more connected digital engineering environment. An open implementation gives the community a shared place to test those promises and improve the common ground.

## Eclipse project and commercial offerings are different things

The Eclipse project is the authoritative place for source code, governance, releases, contribution, and community discussions. It should be the first link for anyone who wants to understand or participate in SysON itself.

Organizations often need additional work around that project: packaged distributions, controlled deployments, identity and access integration, monitoring, backups, upgrades, support commitments, method-specific viewpoints, migration, or connections to the rest of the engineering system.

[Obeo presents its services and offerings around SysON](https://www.obeosoft.com/en/products/syson/) for those industrial concerns. Other organizations can also build services on top of the open-source project. The existence of commercial value around SysON does not change the governance or availability of the Eclipse codebase.

## How SysON relates to Capella and Papyrus

SysON is not intended to make every existing MBSE environment obsolete overnight.

Papyrus brings a long history of support for OMG modeling standards and an ecosystem of engineering extensions. Capella combines the Arcadia method with a focused workbench and has demonstrated that language, method, and tool need to reinforce one another in industrial deployments.

SysON creates opportunities to connect those ecosystems with SysML v2 rather than treating migration as a single replacement event. The project scope explicitly includes integration with Papyrus and Capella. The exact approach depends on the engineering objective: exchange models, co-design across languages, reuse method concepts, expose specialized views, or integrate through services.

In our [Open Source MBSE at Scale presentation]({{ site.url }}/talk/IEEE-ISSE25/), Asma Charfi and I described this progression from proven open-source MBSE tools to web-native SysML v2 environments. The [MODELS 2024 demonstrations]({{ site.url }}/modeling/models2024/) provide a more concrete view of Sirius Web and SysON in action.

## How to evaluate SysON

Start with a bounded engineering question, not a generic product tour.

1. **Choose a representative model.** Include the definitions, usages, relationships, behaviors, and requirements that matter to your practice.
2. **List the required views.** Identify which roles need diagrams, forms, tables, text, or focused dashboards.
3. **Check language coverage.** Use the documentation for the release under evaluation and verify important concepts directly.
4. **Test collaborative workflows.** Explore onboarding, concurrent access, review, validation, permissions, and recovery expectations.
5. **Exercise interchange and APIs.** Prove the integrations needed for requirements, analysis, simulation, PLM, ALM, and reporting.
6. **Assess extensibility.** Prototype one organization-specific viewpoint or rule instead of assuming customization will be straightforward.
7. **Plan operations.** Decide who owns deployment, upgrades, observability, backups, security fixes, and user support.
8. **Separate project maturity from solution maturity.** A supported and integrated deployment can have different operational characteristics from a raw project build.

This approach reveals whether SysON fits the actual practice you want to establish. It also produces useful feedback for the open-source project when something is missing.

Consider that we are releasing a new version every 8 weeks, so this project moves fast and something which is not yet there can appear quickly. By the way you can also make it happen through [sponsored development and open innovation](https://www.obeosoft.com/en/company/open-innovation/)

## How to get started and contribute

Use the official resources according to what you need:

- the [Eclipse project page](https://projects.eclipse.org/projects/modeling.syson) for governance and project identity;
- the [SysON website](https://mbse-syson.org/) for the project entry point;
- the [user and developer documentation](https://doc.mbse-syson.org/syson/v2026.5.0/) for installation, features, APIs, and extension guidance;
- the [GitHub repository](https://github.com/eclipse-syson/syson) for source code, releases, issues, and discussions;
- the [Obeo SysON page](https://www.obeosoft.com/en/products/syson/) for professional support and industrial offerings.

You can begin as a user, report an issue with a reproducible example, discuss a use case, improve documentation, or contribute code. In an emerging ecosystem, precise feedback about real engineering workflows is as valuable as another isolated feature request.

## The larger purpose

SysON is one part of a broader transition. Systems engineering tools are moving from isolated desktop applications toward shared modeling platforms connected to the digital engineering environment. SysML v2 provides a new language and interoperability foundation; SysON explores what an open, web-based implementation of that foundation can become.

Its value should not be judged only by how many diagram elements it can draw today. The larger test is whether teams can build trustworthy practices around it: usable views, controlled collaboration, transparent interoperability, explicit methods, and integrations that keep the model connected to engineering decisions.

That work is still progressing. The fact that it happens in the open is precisely what makes SysON strategically interesting.
