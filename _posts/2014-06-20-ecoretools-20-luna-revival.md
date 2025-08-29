---
layout: post
title: "EcoreTools 2.0 - The Luna Revival"
date: '2014-06-20T01:49:00.000-07:00'
categories: [modeling]
tags:
  - emf
  - ecore
  - sirius
modified_time: '2014-06-20T01:49:13.830-07:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-4092639446544312147
blogger_orig_url: https://model-driven-blogging.blogspot.com/2014/06/ecoretools-20-luna-revival.html
permalink: /ecoretools-20-luna-revival/
---

With Eclipse Luna comes a complete re-implementation of [EcoreTools](https://www.eclipse.dev/ecoretools), the diagram editor for Ecore. This matters because EcoreTools is often the first step our adopters have to go through; users expect a diagram editor to design a domain model.

Why the revival? After years of minimal maintenance, the availability of [Sirius](https://www.eclipse.dev/sirius) made it possible to rebuild EcoreTools efficiently and focus on user experience. The goal: assist you in designing a good Ecore model easily.

Highlights

- Ecore support beyond classes/references: dedicated layers and editors for documentation, constraints, generics, and package dependencies.
- Productivity: keyboard shortcuts for multiplicities and types; easy reconnection; full-screen friendly; GenModel kept in sync.
- Clarity and design: improved visuals and notations (e.g., bidirectional references) to avoid getting in your way.

Documentation

![Doc note]({{ site.url }}/images/blog/2014/ecoretools-doc-note.png) ![Doc table]({{ site.url }}/images/blog/2014/ecoretools-doc-table.png)

Bi-directional references

![EOpposites]({{ site.url }}/images/blog/2014/ecoretools-eopposite.png)

Constraints

![Constraints]({{ site.url }}/images/blog/2014/ecoretools-constraints.png)

Generics

![Generics]({{ site.url }}/images/blog/2014/2634caf68113d7bd3b1e85e1df5c4aff.png)

Package Dependencies

![Deps]({{ site.url }}/images/blog/2014/ae061e611b11578818a2e2a2c4c847d8.png) ![External class]({{ site.url }}/images/blog/2014/ecoretools2-external.png)

Intro screenshot

![Intro]({{ site.url }}/images/blog/2014/intro.png)
