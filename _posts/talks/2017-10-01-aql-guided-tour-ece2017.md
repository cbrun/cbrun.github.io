---
layout: post
title: "Eclipse Modeling Guided Tour — AQL (EclipseCon Europe 2017)"
categories:
  - talk
tags:
  - talk
  - ecore
  - acceleo
  - aql
  - eclipsecon
excerpt: "AQL in practice: writing fast, readable queries for EMF models—tips from EclipseCon Europe 2017."
---

Here’s a draft you could use as a short, SEO-friendly introduction article written in the first person:

---

[![]({{ site.url }}/talks/EclipseConEU2017/aql_thumbnail.png)]({{ site.url }}/talks/EclipseConEU2017/EclipseModelingGuidedTour-aql.pdf)

In October 2017, at EclipseCon Europe, I had the opportunity to present a talk titled **“A Guided Tour of Eclipse Modeling.”** The focus was on introducing the **Acceleo Query Language (AQL)**—a small, fast, and powerful tool designed to make life easier for anyone working with models in the Eclipse ecosystem.

I like to describe AQL as a *sidekick* rather than a replacement. It integrates smoothly with existing tools like **Eclipse Sirius**, **M2Doc**, and **ALE**, and has been shipped as part of the **Acceleo project since 2015**. Its mission is simple: make querying, generating, and documenting models faster, more reliable, and easier to understand.

## Why a Query Language for Sirius?

When building modeling tools with Sirius, querying the model is at the heart of everything. Whether you want to filter elements, generate documentation with **M2Doc**, or add behaviors with **ALE**, you need a language that is **expressive, safe, and well-integrated**. AQL was designed specifically for this purpose.

## How it Works in Practice

AQL borrows a syntax familiar to users of **OCL (Object Constraint Language)** but simplifies it:

* It avoids unnecessary verbosity (variables are optional).
* It infers types automatically, while still being **statically typed** for safety.
* It supports lists and sets with stable ordering.
* It comes with smart validation and fast runtime evaluation.

To put it simply: you can navigate and filter model elements without worrying about nested collections, endless casting, or cryptic errors.

## Performance and Extensibility

During the presentation, I shared performance comparisons with other approaches like **IncQuery (EIQ)**. The results showed AQL to be both **efficient in memory** and **fast in evaluation**, especially when working with large models. And because it’s extensible, you can easily add your own Java methods, operators, or domain-specific services.

## What’s Inside the Language

AQL is more than just syntax. It is built on four pillars:

1. **Syntax** – simple, OCL-inspired, and extensible.
2. **Semantics** – statically typed but forgiving.
3. **Tooling** – embeddable with advanced type inference.
4. **Runtime** – small, interpreted, and optimized for speed.

Behind the scenes, the runtime is built with EMF, Guava, ANTLR, and about 13,000 lines of carefully written Java code.

## Where to Learn More

If you are curious, you can explore the official documentation (linked directly from the slides). Since 2015, AQL has been part of the Eclipse release train and is already powering **Sirius diagrams**, **M2Doc document generation**, and **ALE behaviors**.


For engineers writing constraints, derived features, and UI logic on EMF models. AQL provides concise, performant queries that integrate well across Sirius and tooling.

## Context
- Event: EclipseCon Europe 2017, Ludwigsburg, Germany
- Date: October 2017
- Slides: [PDF]({{ site.url }}/talks/EclipseConEU2017/EclipseModelingGuidedTour-aql.pdf)
- [Video](https://www.youtube.com/watch?v=a271YFtNX6M)
