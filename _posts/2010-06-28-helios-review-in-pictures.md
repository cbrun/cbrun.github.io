---
layout: post
title: "3 Good Reasons to use the Helios Modeling Package"
date: '2010-06-28T05:31:00.000-07:00'
categories: [eclipse]
tags:
  - eclipse
  - amalgamation
  - compare
  - ecoretools
  - obeo
excerpt: "Three reasons the Helios Modeling Package became my daily driver—hidden EMF goodies, EcoreTools diagrams, and full SDK access—with add‑ons to try."
modified_time: '2010-07-05T08:51:45.448-07:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-795928650798672137
blogger_orig_url: https://model-driven-blogging.blogspot.com/2010/06/helios-review-in-pictures.html
---

Now that the entire world noticed that I [don't know even one thing about soccer]({{ site.url }}/images/blog/2010/colored_generatedcode.png) and I'm [even trying to cheat](https://model-driven-blogging.blogspot.com/2010/06/forecasts-comparison-for-world.html), I should get back to sharing what I understand instead of those silly forecasts.

Helios has been out for a little while now; the mediatic storm is pretty much gone and it's a good time for me to have a look back.

This year one of my goals was: "I want to transform the Modeling Package into a product which I would use myself". I've been using it quite extensively lately and I'm pretty happy with the results. The Galileo package is far from being usable but the Helios version is just great :)

Why? A few reasons...

1. because **it's including hidden EMF goodness!**

   EMF generates code... which is good as any code you don't need to write means less bugs. But sometimes you don't even want to see that code!

   If so, you're lucky — there is a **specific filter for your workspace!**

   ![Filter generated code]({{ site.url }}/images/blog/2010/filter_generatedcode.png)

   And the integration goes even further, code you manually changed is **highlighted with different colors**!

   ![Colored generated code]({{ site.url }}/images/blog/2010/colored_generatedcode.png)

   Oh, and you can **compare and merge** any kind of EMF model, starting from the Ecore ones.

   ![Team support]({{ site.url }}/images/blog/2010/team_support.png)

2. **It provides Class diagram support**

   As a developer you always end up needing some kind of graphical support for your communication. A _class-like_ diagram is well known by others; the modeling package includes support for Ecore thanks to the EcoreTools project.

   ![Graphical modeling]({{ site.url }}/images/blog/2010/graphical_modeling.png)

   And you even have specific views to browse your design hierarchy or usages.

   ![Hierarchy graphical]({{ site.url }}/images/blog/2010/hiearchy_graphical.png)

   While I'm at it, if you're interested in contributing to this project which is highly popular, you should really get in touch with [Ed](https://ed-merks.blogspot.com/)! We're looking for fresh people to reboot this project — **it's not as active as it deserves to be!**

3. **It's an SDK**

   As the modeling project provides a lot of high quality frameworks, you often need to have access to their source and as such it's **one of the few packages providing SDKs.**

   ![SDK]({{ site.url }}/images/blog/2010/sdk.png)

All those reasons make the modeling package the best one to get started with any modeling task, but also any **RCP development planning to leverage those great frameworks.**

Oh yes, that should make this package a **nice starter for e4** too:

![Helios]({{ site.url }}/images/blog/2010/helios.png)

post scriptum: 4. **It's easily extensible**

Of course the modeling community is way more active than that. I would strongly encourage you to have a small click on this button ![Button]({{ site.url }}/images/blog/2010/button.png) and have a try on the latest hot contributions which were not part of the Helios release: the Agent Modeling Platform:

![AMP]({{ site.url }}/images/blog/2010/amp.png)

And the Papyrus UML modeler

![Papyrus]({{ site.url }}/images/blog/2010/papyrus.png)
