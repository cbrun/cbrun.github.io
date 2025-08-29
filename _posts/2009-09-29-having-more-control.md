---
layout: post
title: Having more control ...
date: '2009-09-29T06:57:00.000-07:00'
tags:
- designer
- eclipse
- acceleo
- modeling
- obeo
categories: [modeling]
modified_time: '2009-09-29T09:09:44.397-07:00'
thumbnail: https://3.bp.blogspot.com/_u5tMWln_Ie8/SsIi1OL6w-I/AAAAAAAAALw/IpAvHoRsmME/s72-c/100_9865.JPG
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-8062935893527033571
blogger_orig_url: https://model-driven-blogging.blogspot.com/2009/09/having-more-control.html
---

Who never asked for more time to focus on things that matter, like, for instance, [gigantic barbecues](https://mariot-thoughts.blogspot.com/2009/09/nathalie-effect-goals-tests-and-patches.html)?

[![]({{ site.url }}/images/blog/2009/having-more-control/s400_100_9865.JPG)](https://3.bp.blogspot.com/_u5tMWln_Ie8/SsIi1OL6w-I/AAAAAAAAALw/IpAvHoRsmME/s1600-h/100_9865.JPG)

And then you fulminate against this tool which should help you and which is not; it's just another burden placed on you to provide this documentation nobody will ever maintain or even read. _Is that what modeling is about?_

Life as a software user is often harsh, especially as you have, most of the time, no **control** at all on the software you use. As a developer it's even more difficult as you have an idea on what's going on behind the scene, and not having control is something you just can't handle now that so much open-source products provide you this power.

If you had control on your tools, if you could adapt it or even easily define it, then you could focus on useful things. **Modeling** can bring it back to you — not modeling like in UML modelers, modeling like formalizing your domain model as a way to capture your thought or your coding tasks.

A model doesn't have to be high level; a model doesn't have to provide as much information as your source code; a model is just here to help you answer questions about what you're doing. If you can't say for a given model what kind of questions it's helping you to answer, then your model is just not relevant — it's not a model, let's call that **boxes with edges**.

And now let's take a small example: you want to define a software using components which are providing services, then you want to assign these "logical" components to Eclipse plugins. Here is a model definition you can come up with:

[![]({{ site.url }}/images/blog/2009/having-more-control/s400_ecoremodel.png)](https://4.bp.blogspot.com/_u5tMWln_Ie8/SsIbD5F8ZMI/AAAAAAAAALQ/pHQPTzsglpQ/s1600-h/ecoremodel.png)

From an instance of a model you can answer the questions: how is my application split? What services are provided and required by whom? And how are these components linked to the Eclipse plugins I'm coding?

From now you can either capture an instance and start working thanks to EMF Dynamic support, or specify a tooling to ease this capture. If a diagram is a good representation for your problem, pick it; if it's not, pick a tabular, tree or even textual representation.

The following demo describes a tooling specification (click on the image!). At the top: the specification. At the bottom: the tooling which is dynamically adapting itself to the specification.

[![]({{ site.url }}/images/blog/2009/having-more-control/s400_specify.png)](https://literate.modeling.free.fr/modeling/designer/overview/OD-specifier.htm)

Modeling itself is useful to organize your thought, validate your design or even help to pick the best trade-off for a given architecture. In an [old post I was showing how a modeling tooling having support for viewpoints](https://model-driven-blogging.blogspot.com/2009/05/viewpoints-enabled-modeling-tools.html) is powerful in this regard. The next demo is showing you how the developer or analyst can then leverage the tooling definition (click again!):

[![]({{ site.url }}/images/blog/2009/having-more-control/s400_use.png)](https://literate.modeling.free.fr/modeling/designer/overview/OD-user.htm)

Now you've described everything and you're quite happy with the result, why not use this information to help you produce code? As soon as the modeling environment is linked to the development tasks with code generators, the model is **not going to be deprecated** — it will be used by the team to get the **tedious** work done.

Moreover when the environment provides you navigation from your code to the model, then to the code, and support for customizing anything in the generated code, then the tool is no more a burden, but a relief. (yet another demo!)

[![]({{ site.url }}/images/blog/2009/having-more-control/s400_generate.png)](https://literate.modeling.free.fr/modeling/designer/overview/OD-Acceleo_Traceability.htm)

It's been 3 years now since I arrived in [Obeo](https://www.obeosoft.com/fr/), and every tool we developed since then has been designed following this motto: "Having more control, not getting in the way and providing value to the developer."

So far I'm quite happy with the results :)

_ps: thanks to Jérôme who did the demo_
