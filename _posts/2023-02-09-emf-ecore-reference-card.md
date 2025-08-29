---
layout: post
title: Do you know Ecore? Looking for a reference card?
categories: [modeling]
tags:
  - modeling
  - emf
  - eclipse
  - sirius
  - opensource
  - ecore
permalink: /modeling/emf-ecore-reference-card/
translation_fr: /modeling/ecore-diagram-reference/
excerpt: "A one‑page Ecore reference card—handy for EMF users and educators—explaining why the core model concepts still matter and how to use them today."
---


“𝐸𝑣𝑒𝑟𝑦𝑡ℎ𝑖𝑛𝑔 𝑠ℎ𝑜𝑢𝑙𝑑 𝑏𝑒 𝑚𝑎𝑑𝑒 𝑎𝑠 𝑠𝑖𝑚𝑝𝑙𝑒 𝑎𝑠 𝑝𝑜𝑠𝑠𝑖𝑏𝑙𝑒, 𝑏𝑢𝑡 𝑛𝑜𝑡 𝑠𝑖𝑚𝑝𝑙𝑒𝑟” probably was one of the mantra the [Eclipse Modeling Framework](https://www.eclipse.dev/modeling/emf/) team (Ed Merks, Marcelo Paternostro, Dave Steinberg among others...) sticked to when the created the core concepts which would allow the definition of all the others tools.

Ecore is a kernel, you define your domain specific model using these constructs. It boils down to classes, types, attributes and relationships, yet there is a lot of beauty in the way it has been designed and we can safely say it passed the test of time. In 2016 I tried to condensed all of it in a single reference card. I did not finished it to the point of publishing it but I'm doing it today (better late than never!)

<figure>
    <a href="{{ site.url }}/images/blog/2023/Ecore_reference_card.pdf"><img src="{{ site.url }}/images/blog/2023/Ecore_reference_card.png"></a>
    <figcaption>Ecore Reference Card</figcaption>
</figure>


To produce it I exclusively used Open-Source tools :
- [Ecore Tools](https://www.eclipse.dev/ecoretools/): Ecore diagraming editor built on top of Eclipse Sirius ,
- [Inkscape](https://inkscape.org/) : one of my favorite OSS tool to produce vector graphics.

I created 4 distincts diagrams from the Ecore.ecore model, then used the "Export as Image" feature of Sirius to get SVG files out of it. I dragged and dropped those file in Inkscape, scaled, composed a bit, and voilà ! Here is the refcard.

You can decorate your office now ;) Hope you enjoy



