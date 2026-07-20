---
layout: post
title: "We built the languages. That was the easy part."
categories:
  - talk
tags:
  - talk
  - modeling
  - dsl
  - ecore
  - sirius
  - sirius-web
  - capella
  - mbse
  - syson
  - obeo
permalink: /talks/sle-2026-we-built-the-languages/
excerpt: "A reflection from my SLE 2026 keynote on how each generation of language engineering moved the problem: from metamodels and editors to platforms, communities, practices, and human-agent collaboration."
---

Last week I had the pleasure of giving the keynote at [SLE 2026](https://conf.researchr.org/home/sle-2026#Keynote) in Rennes. The title was:

> **We built the languages. That was the easy part.**

<figure>
    <a href="{{ site.url }}/talks/SLE2026/">
      <img src="{{ site.url }}/images/blog/2026/sle-we_built_the_language.png" alt="SLE 2026 keynote title slide: We built the languages. That was the easy part.">
    </a>
    <figcaption><a href="{{ site.url }}/talks/SLE2026/">Slides: We built the languages. That was the easy part.</a></figcaption>
</figure>

It was a special moment for me. Rennes is not far from Nantes, where Obeo was founded almost twenty years ago. I joined Obeo as an intern in 2006, right after discovering modeling and model-driven technologies through Jean Bezivin's classes. Since then, most of my professional life has revolved around languages: modeling languages, domain-specific languages, the tools to define them, and the platforms to make them usable.

The keynote was not meant as a retrospective for nostalgia's sake. It was a way to make one progression visible.

Each generation of language engineering moved the problem.

First, we had to build metamodels. Then editors. Then platforms. Then communities around those platforms. Then real practices inside organizations. And now, probably, forms of collaboration where humans, tools, and agents work on the same models.

That is the thread I wanted to pull:

- from building a metamodel;
- to building an editor;
- to building a platform;
- to building a community;
- to building a practice;
- to building human-agent collaboration.

The keynote was really about this shift:

**What happens when the hard part is no longer defining the language, but making it live?**

## We learned how to build languages

For years, the modeling and language engineering communities were told that modeling languages would not really work. Not at scale. Not in real organizations. Not outside expert circles.

And yet, collectively, we built a remarkable ecosystem.

[Eclipse Modeling Framework](https://eclipse.dev/emf/) gave us a shared substrate: Ecore, reflection, serialization, generation, a runtime, and a way to make model-based infrastructure reusable. Acceleo showed that models could produce real artifacts: code, XML, documentation, whatever the project needed. GMF industrialized graphical modeling enough to make dedicated modelers viable outside large tool vendors. Xtext brought textual syntax, parsing, validation, completion, navigation, and IDE-grade tooling to DSLs.

Then [Sirius](https://eclipse.dev/sirius/) changed the shape of the problem again. It was no longer only about one editor for one language, but about a complete modeling workbench: diagrams, tables, forms, viewpoints, multiple representations for the same language, and fast iteration over the user experience.

That trajectory matters because it changed the question. We spent years making languages more formal, more expressive, better tooled, more interoperable, more versionable, more collaborative. All of that was necessary.

But it was not the end of the story.

## The metamodel is only the beginning

[Capella](https://mbse-capella.org/) made this lesson very concrete for me.

Capella is not only a modeling tool. It carries the [Arcadia method](https://mbse-capella.org/arcadia.html). It uses the vocabulary of systems engineers. It gives people an opinionated way to work. It is also used widely enough that organizational questions become visible.

When a language leaves the lab, the first enthusiastic team, or the first research prototype, the problem changes. It is no longer only a technical problem. It becomes an organizational one.

Who is going to use the language? How do they learn it? Who is allowed to change it? How do teams collaborate around it? How does the language survive not for six months, but for ten or fifteen years?

I have seen many meetings where the discussion started with slides, documents, and diagrams, then slowly drifted because everyone had a slightly different mental model of the system. Then someone opened the Capella model, and the discussion changed. We were no longer arguing around a frozen picture. We could navigate from an operational need to functions, components, interfaces, and constraints.

> The model became the common table.

<figure>
    <a href="{{ site.url }}/talks/SLE2026/images/from%20many%20views%20to%20a%20model%20being%20the%20common%20table.png">
      <img src="{{ site.url }}/talks/SLE2026/images/from%20many%20views%20to%20a%20model%20being%20the%20common%20table.png" alt="Many stakeholder views converging around a model as the common table">
    </a>
    <figcaption>A model is useful when it becomes a shared table for discussion, not just a deliverable.</figcaption>
</figure>

This is where the problem moves again. The metamodel was necessary, and the editor was necessary, but neither was sufficient. At scale, a language needs training, documentation, tutorials, books, webinars, case studies, reviews, versioning, governance, integration with other practices, and trust.

Adoption is not only a product problem. It is a transmission problem.

When that transmission works, something important happens:

> People stop talking about the tool. They talk through the language.

## We confused expressivity with usability

The next lesson is less comfortable.

We were right to make languages expressive. Industrial engineering needs precision, coverage, extensibility, and tooling power. But adoption at scale exposes a different problem: many users are not asking for more expressive power first. They are asking for help.

Help me understand what to do. Help me find the right thing. Help me trust that the tool is responding. Help me collaborate without having to understand the whole technical environment.

Sirius Desktop inherited the richness of the Eclipse workbench. Perspectives, views, editors, properties, commands, builders, validators, problems, preferences. Most of these concepts are useful. But for a domain expert, or even for many engineers, the experience can feel like an aircraft cockpit.

In several customer projects, part of the work was to hide Eclipse: the workspace, the perspectives, the menus, the mechanics that were powerful but not meaningful for the user's task. The goal was not to deny the richness underneath. The goal was to stop asking every user to understand it before they could do useful work.

That distinction matters. Usefulness does not automatically create usability.

## The Web changed the assumptions

Around 2015, it was already clear that the Web was becoming a serious platform for serious applications. By 2019, this had become a public decision for us with [Sirius Web](https://eclipse.dev/sirius/sirius-web.html).

The question was not only "can we put diagrams in a browser?" The harder question was: **which assumptions about modeling tools do we need to rebuild?**

Desktop modeling tools could leave many things implicit. The Web makes them visible. What lives on the client? What lives on the server? What is persistent? What is computed on demand? What is shared? What must remain fast despite latency?

Even something as simple as a URL changes the social life of a model. You no longer say: open this project, find this diagram, and look in this corner. You say: look exactly here. That changes reviews, support, documentation, and decision making.

<figure>
    <a href="{{ site.url }}/talks/SLE2026/images/siriusweb-paper.png">
      <img src="{{ site.url }}/talks/SLE2026/images/siriusweb-paper.png" alt="Sirius Web experience report">
    </a>
    <figcaption>The Sirius Web experience report was not only about architecture; it documented why we reopened decisions inherited from desktop tooling.</figcaption>
</figure>

Performance is part of that experience too. In modeling tools, performance is often treated as an architecture topic. Of course it is. But it is also a trust topic. If an action is instant on a small model, then takes eight seconds, then thirty seconds, users do not only see latency. They wonder whether they did something wrong, whether the tool is frozen, or whether they should avoid that command.

This is why Sirius Web is not just a rebuild of Sirius Desktop in the browser. It is a platform for modeling experiences: language definition, diagrams, trees, tables, forms, details views, collaboration, APIs, publication, extension points, and workflows that let an organization capitalize on what it has learned.

That is another displacement of the problem. Once we know how to build a modeling editor, we have to build the platform that lets people share, extend, integrate, and evolve the modeling experience.

## SysML v2 is a rare moment of openness

The next twenty years will not need less language. I think they will need more language, but language that is easier to practice, easier to share, easier to integrate, and easier to evolve.

[SysML v2](https://www.omg.org/sysml/sysmlv2/) is important in that context. It is not only a new version of SysML. It is one of the largest opportunities for renewed adoption that modeling languages have seen in a long time. The standard evolves. Tools have to be rethought. Organizations that hesitated with MBSE can start again from a more modern base.

For the SLE community, SysML v2 brings language engineering questions back to the center: explicit semantics, textual and graphical syntax, APIs, interoperability, analysis, transformation, automation, and extension mechanisms.

This is also why we started [SysON](https://mbse-syson.org/) with CEA. The goal is not only to have one more SysML v2 tool. The goal is to make sure that a durable, supported, extensible, open-source platform exists for SysML v2 while the ecosystem is still being formed.

<figure>
    <a href="{{ site.url }}/talks/SLE2026/images/syson-screenshot.png">
      <img src="{{ site.url }}/talks/SLE2026/images/syson-screenshot.png" alt="SysON web-based SysML v2 modeling environment">
    </a>
    <figcaption>SysON aims to make a modern, Web-based, extensible, open-source SysML v2 modeler available while practices are still forming.</figcaption>
</figure>

That timing matters. When a new standard appears, the ecosystem is not stabilized yet. People are learning what the language means in practice. Organizations are deciding how they want to use it. Tool vendors are deciding what kind of experience they want to provide. This moment does not last forever. Formats, training material, habits, extensions, and procurement decisions eventually harden.

Open source has a role to play before that happens.

It can raise the baseline. If the common ability to model in SysML v2 is available as an open platform, then value moves upward: methods, domain extensions, integration, analysis, collaboration, deployment, certification, support, and expertise.

## The model becomes a contract

The last part of the keynote brought AI into the story, not as a separate topic, but as a consequence of the same argument.

I do not see AI as a threat to modeling tools. I see it as one more reason to have formal, shared, tooled languages.

Without a model, an AI system can produce a convincing answer that is hard to verify. With a model, it acts on an object we can inspect, validate, compare, and correct. The model anchors the agent. It gives the agent structured context, explicit concepts, relationships, constraints, and a shared artifact with the engineer.

> The model becomes a contract.

Not in a legal sense, but in an engineering sense. It carries human intent in a formal structure. That structure gives tools something precise to compute on, and agents something precise to act on.

If an agent proposes a change, the result should not only be text. It should be a modification of an object we can inspect. We can compare it. We can validate it. We can reject it. We can ask why.

This is very different from a purely conversational interaction. It is also why the method matters. If the agent uses the same guided environment as the engineer, the method is not lost. It remains part of the interaction.

## Making languages live

The sentence I wanted to leave with the SLE audience was this:

> A language is not finished when it is defined. It is finished when people can practice it.

That is true for organizations. It is true for open-source communities. It will probably be true for agents as well.

We built the languages. That was a real achievement. But each success moved the problem forward. The metamodel led to the editor. The editor led to the platform. The platform led to the community. The community led to practice. And practice now has to include agents without losing human responsibility.

That is where I think the next twenty years of language engineering will be. Not only in defining languages, but in making them practicable, durable, and shared.
