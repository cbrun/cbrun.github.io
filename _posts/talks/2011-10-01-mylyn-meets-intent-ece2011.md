---
layout: post
title: "Mylyn meets Intent: Documentation made fun and useful (EclipseCon Europe 2011)"
categories:
  - talk
tags:
  - talk
  - ecore
  - intent
  - documentation
  - literate-modeling
excerpt: "Bringing documentation into the development loop—Mylyn and Intent integration patterns."
draft: true
---


[![]({{ site.url }}/images/blog/2011/intent.png)]( {{ site.url }}/talks/EclipseConEurope2011/Intent.pdf)

At EclipseCon 2011, we (Obeo, France) introduced a new way of thinking about software documentation: **Mylyn Intent**, an open-source project designed to make documentation both **fun** and **useful**. Our talk explored how developers can integrate documentation seamlessly with their models, code, and tools to keep everything up-to-date and engaging.

## Why We Need Better Documentation

We all know the situation: Alice, a team member, questions why a design looks so complex. Bob responds by pointing her to a three-year-old design document. While existing docs may help, they are often outdated, hard to navigate, and not visually appealing. What developers really want is documentation that is **easy to access, simple to maintain, and pleasant to read**.

## The Concept of Literate Modeling

Inspired by Donald Knuth’s *Literate Programming*, our approach leverages **Literate Modeling**: mixing documentation and model fragments in one place. Instead of separating explanations from technical details, we embed executable model snippets directly in the docs. This ensures that the documentation stays synchronized with the code and architecture while remaining understandable to humans.

## How It Works

* **Integrated workflow**: Multiple editors (Eclipse, web, or custom tools) connect to a shared repository (CDO, Workspace, JGit, ECR). Any change triggers updates across clients in real time.
* **Client-based architecture**: Documentation editors, compilers, and browsers all act as clients consuming and reacting to model fragments.
* **Executable snippets**: For example, EMF Compare’s “match” package can be documented with embedded Ecore definitions and URI-based resource references, keeping the docs live and relevant.

## Benefits for Developers

With Mylyn Intent, developers can:

* Keep documentation aligned with evolving code and models.
* Reduce duplication and inconsistencies across guides, API references, and design docs.
* Improve collaboration by connecting multiple editors and contributors in one workflow.
* Make documentation aesthetically pleasing and engaging, not just a burden.

## Roadmap and Vision

Back in 2011, Intent was just starting under the Mylyn umbrella, aligned with Eclipse Indigo (3.7). Our milestones included early adoption by June, a 0.7.0 release in Q3, and features like a functional workspace backend, Eclipse IDE textual client, and model synchronization. The long-term mission remains the same: **bridge the gap between documentation and development artifacts** so teams can build, extend, and test products more effectively.

## Context
- Event: EclipseCon Europe, Ludwigsburg
- Date: 2011
- [Slides]({{ site.url }}/talks/EclipseConEurope2011/Intent.pdf)
