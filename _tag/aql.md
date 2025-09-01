---
title: "aql"
tag: "aql"
description: "Posts related to the Acceleo Query Language."
---
# AQL (Acceleo Query Language)

## What is AQL?

TL;DR: AQL is a small, fast, EMF-native query language. You use it to navigate and filter models in tools like Eclipse Sirius and M2Doc—typically with expressions that start with aql:. It’s OCL-ish in spirit, but simpler and tuned for modeling tool builders. 

## Why AQL exists

From Acceleo 2.x with its XPath-like syntax, to a language inheriting from OCL (MTL) to check constraints, to then executing queries and constraints as part of the interpretation of a live environment (Sirius), we’ve been through a lot of distinct query languages and implementations across Obeo’s history. AQL is the culmination of everything we wanted after we’d been through hell and back with the others. Fast. Simple. Fast. Extensible. Fast. Strongly typed. Fast. Forgiving runtime. Fast. Small and embeddable. Fast.

> It’s a small gem; there isn’t much out there besides the code. On this page I’ve gathered the posts related to AQL.

## Where you’ll meet AQL

* **Eclipse Sirius**: used across the `VSM` (conditions, labels, tools). New VSMs are preconfigured for AQL; you can also try expressions live in the *Interpreter* view. 
* **M2Doc**: template expressions that pull data from EMF models are evaluated with AQL; there’s even a Word add-in that gives you completion for AQL while editing templates.
* **Eclipse Sirius Web**: AQL is at the core of the `View` model principle.
* **Acceleo4 Templates**: Coming soon...

## Want to go deeper?

* **[AQL reference (syntax + standard services)](https://eclipse.dev/acceleo/documentation/aql.html)** — the canonical doc.
* **[Sirius “Writing Queries](https://eclipse.dev/sirius/doc/specifier/general/Writing_Queries.html)”** — how AQL plugs into VSMs, key differences, and setup.
* **[What’s new in Sirius 3.0](https://eclipse.dev/sirius/whatsnew/whatsnew3.html)** — background on why AQL was introduced.


