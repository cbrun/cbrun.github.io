---
layout: post
title: "Obeo Designer 6.1.0 - no 4.x platform... yet !"
date: '2013-01-22T12:55:00.000-08:00'
categories: [eclipse]
tags:
  - uml
  - eclipse
  - obeo designer
modified_time: '2013-01-22T12:55:54.311-08:00'
thumbnail: https://cedric.brun.io/images/blog/2013/unicorn.jpg
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-7966782633835511957
blogger_orig_url: https://model-driven-blogging.blogspot.com/2013/01/obeo-designer-610-no-4x-platform-yet.html
---

![Unicorn]({{ site.url }}/images/blog/2013/unicornf.jpg)

We've been quite busy in the last few months at Obeo: building and releasing a brand new product [dedicated to EA](https://www.obeosmartea.com/), celebrating our seventh birthday, building almost [20 modeling environments](https://marketplace.obeonetwork.com/) based on DSLs and/or standards, bringing model comparison [far beyond](https://fr.slideshare.net/mikaelbarbero/emfcompare-20-scaling-to-millions) the competition, tackling the issue of software and design documentation with a [novel approach in the Mylyn project](https://www.eclipse.dev/intent/) and step by step getting closer to our perfect development process, our [unicorn](https://www.eclipsecon.org/2012/sessions/98-days-1-our-continuous-deployment-pivot).

And working on Obeo Designer: we just released 6.1.0 bringing among other things:

- compatibility with Eclipse 3.8 (and Indigo, and Helios)
- a ready-to-launch server for live and instant collaboration on models with fine-grained locks
- token/floating licenses — meaning you can now buy licenses for, let's say, 30 simultaneous users, no matter who
- a better packaging, documentation and examples
- updated versions of all its OSS components: Acceleo, ATL, EEF, EMF Compare

Roughly 160 tasks have been closed for this release not counting the work done on the OSS components. It's quite hard to summarize but you can find [a few highlights here](https://www.obeodesigner.com/features/whatisnew).

Why Eclipse 3.8?

We worked on bringing the 4.2 compatibility for the product (and are still working on it) but we got hit by [some limitations](https://bugs.eclipse.org/bugs/show_bug.cgi?id=366528) of the compatibility layer. It was detected late as the problem came when we decided to rely more on the platform mechanisms to get [more extensibility](https://www.obeodesigner.com/features/whatisnew#extensible_tab_bar)... It's not trivial to fix; we are trying to help the platform team as much as we can to implement this either in the 4.2 or 4.3 stream.

What does that mean? It means on Eclipse 4.2 you don't get the diagram contextual toolbar, also known as TabBar:

![Graal e4]({{ site.url }}/images/blog/2013/graal-e4.png)

This prevents end users to enable/disable graphical layers or to switch to the "layout mode" (a.k.a. VI for diagrams). That's quite a big loss for end users; you get used to this ability to apply layers on your diagram, but as I said, we're working on it.

Obeo Designer is an integrated platform to build modeling environment. Using it you can quickly and easily leverage the power of the whole Eclipse Modeling eco-system: EMF, CDO, Xtext, GMF, Acceleo, ATL, Compare.... It's packaged, tested and includes additional components to create richer modeling environments, quicker.

The problem with such a product is — as it's a base for you to build things — getting what you can achieve with it can be hard. One example (among many on the Eclipse or [Obeo Marketplace](https://marketplace.obeonetwork.com/)) of what you can do is the UML Designer. You can install it from the marketplace, and you can have a look at the [sources here](https://github.com/ObeoNetwork/UML-Modeling). We've already seen 580 installations in the last 5 days, yeah!

Well, ok, But what's really new in your product?

Many changes are not directly visible in this version. We streamlined the CDO and collaborative support, worked on performances, and introduced a few nice features. Go have a look on the [new and noteworthy](https://www.obeodesigner.com/features/whatisnew) page. This blog post is already filled with sentences making me sound like a boastful person. Ok. Just a small glimpse...

You can now use a new construction in your diagram definition: **Brackets**. Using those you can easily represent intervals in a diagram. You can use it in a sequence diagram just like here, but also in any other diagram.

HTML Export: publish your model. You can browse through an example [here](https://obeonetwork.github.com/UML-Modeling/export/index.html).

The complete new and noteworthy (with more pics!) is available [here](https://www.obeodesigner.com/features/whatisnew).

