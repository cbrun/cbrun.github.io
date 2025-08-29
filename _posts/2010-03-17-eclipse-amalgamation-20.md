---
layout: post
title: "Eclipse Amalgamation 2.0"
date: '2010-03-17T01:52:00.000-07:00'
categories: [eclipse]
tags:
  - eclipsecon
  - eclipse
  - amalgamation
  - modeling
modified_time: '2010-03-17T07:48:04.631-07:00'
thumbnail: https://2.bp.blogspot.com/_u5tMWln_Ie8/S6DqyN0fxrI/AAAAAAAAARI/gjLiFrDCZ6U/s72-c/puzzle.jpg
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-2393432359444410631
blogger_orig_url: https://model-driven-blogging.blogspot.com/2010/03/eclipse-amalgamation-20.html
draft: true
---

I'm waiting for a nightly M6 Modeling package to get downloaded on my laptop. As I've got a few hours to wait, I'll use this chance to give news about the [Amalgamation project](https://www.eclipse.dev/modeling/amalgam/).

It's a well-known fact that the Eclipse Modeling Project is myriad of small focused projects. [Kenn](https://kenn-hussey.blogspot.com/) is working on sanity checks for each of those projects — more than 50! The benefit of this organization is that you can choose which bits you want to use depending on your use case, but this flexibility comes at a cost: making sure there is no overlap between proposals is often tricky and ensuring those projects, taken as a whole, provide a consistent platform is even more challenging.

![Puzzle]({{ site.url }}/images/blog/2010/eclipse-amalgamation-20/s320_puzzle.jpg)

A few years ago the Eclipse Modeling Amalgamation project was created and started by providing Eclipse distros tailored for specific needs and an "All Eclipse Modeling in One Package" distro through EPP. At some point the project stalled and during last October a new team gathered and I've been designated project lead.

Most users and adopters consume the Eclipse Modeling Project through the EPP package; one doesn't have to figure out how to browse and install the projects you need. But this package was including all of modeling; as such it was huge, cluttered, untested, and nobody could really use it. Downloads of the package fell down and the Eclipse Modeling project as a whole probably suffered from that.

My first objective for the Amalgam project was to update the package to get a sane one: changing our big messy package to an **Eclipse Modeling SDK** composed of the core runtime components and frameworks:

- **EMF core** and its low-UI-profile companions: **XSD, Transaction, Validation, Mint**, and **compare**
- Graphical support with **GEF** and **GMF runtime**
- **OCL** and **UML2** — you can't really live without those standards
- **CDO** — it brings EMF, as a framework, to another level with collaborative editing and a remote model repository

This set of features + Eclipse SDK and Mylyn composes our new platform, and we went from almost `400` to 250 Mb. It's still big but hey, it's an SDK!

Still, many more great and useful components are built within the Eclipse Modeling Project and getting those to install was painful. Mylyn was already providing a solution to that: a discovery UI:

![Discovery UI]({{ site.url }}/images/blog/2010/eclipse-amalgamation-20/s320_discovery.png)

In the meantime during the year this discovery support has been [moving from Mylyn to P2](https://bugs.eclipse.org/bugs/show_bug.cgi?id=295273).

As a user, having this UI makes my life easier: I can install components without even thinking about where I'll find the pieces and P2 takes care of the requirements and consistency of my Eclipse installation. I'm looking forward to hear from your feedback about it when the M6 package is out.

This modeling platform is a basis we'll test and polish to get a streamlined user experience, and we'll have to organize ourselves to make sure we release a tested, used, and clean platform. The [Eclipse Modeling Panel](https://www.eclipsecon.org/2010/sessions/sessions?id=1528) will be a perfect time to give your opinion and feedback — do not miss it; it's on Monday!

