---
layout: post
title: "Textual Adventures in Ecore + Graphical Modeler"
date: '2011-09-21T02:16:00.000-07:00'
categories: [modeling]
tags:
  - graphical
  - eclipse
  - diagram
  - obeo designer
  - game
  - emf
modified_time: '2011-09-21T02:16:00.094-07:00'
thumbnail: https://1.bp.blogspot.com/-56zFyxZPdGE/TmnW6PBNBsI/AAAAAAAAAmw/G9dwegS5FJI/s72-c/adventure-domain.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-5829610168321635030
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/09/textual-adventures-in-ecore-graphical.html
draft: true
---

I was cleaning up my `${HOME}` folder today and found a set of demos I prepared two years ago.

I did this for a modeling course given at [Polytech'](https://www.polytech.univ-nantes.fr/). The course was about Model Driven Engineering; toward the end the students have to build a domain-specific model for textual adventure games and then generate the corresponding Java app. Some students tend to go very far on this exercise, building a fairly complex DSL.

The following demos are here to give an idea to the students of what can be done in a few minutes: a simple Ecore model

[![Adventure domain]({{ site.url }}/images/blog/2011/textual-adventures-in-ecore-graphical/s320_adventure-domain.png)]({{ site.url }}/images/blog/2011/textual-adventures-in-ecore-graphical/s1600_adventure-domain.png)

And then a graphical modeler:

[![Adventure modeler]({{ site.url }}/images/blog/2011/textual-adventures-in-ecore-graphical/s320_adventure-modeler.png)]({{ site.url }}/images/blog/2011/textual-adventures-in-ecore-graphical/s1600_adventure-modeler.png)

And then we build Acceleo generator templates to directly map a game instance into its running Java code. It's a very interesting exercise; students stay focused because it's about a game, and at the same time it's a great example of the power of specific modeling. You don't design a game with a UML diagram, but building your own language and using it you're quickly getting results and can evaluate many designs.

Building the complete tooling is a matter of minutes, not hours. Here are the live demos:

- Designing the Domain Model: [video](https://ks360939.kimsufi.com/~cedric/data/AdventureGameEcore.htm)
- Specifying while running the Graphical Designer: [part1](https://ks360939.kimsufi.com/~cedric/data/GameModeler1.htm) and [part2](https://ks360939.kimsufi.com/~cedric/data/GameModeler2.htm)

As a sidenote, these flash demos are based on a pretty old version of Obeo Designer — if you're interested, have a look at the latest versions which are even better!

