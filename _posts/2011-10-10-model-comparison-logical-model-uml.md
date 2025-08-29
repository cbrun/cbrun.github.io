---
layout: post
title: "Model Comparison : Logical Model, UML, Papyrus, EcoreTools and GMF Integration"
date: '2011-10-10T07:59:00.000-07:00'
categories: [modeling]
tags:
  - emf compare
  - eclipse
modified_time: '2011-10-10T08:24:41.271-07:00'
thumbnail: https://4.bp.blogspot.com/-QnuIRtATUd4/TpMMEWrcVpI/AAAAAAAAAnQ/a0o0Y8f99tE/s72-c/graphcompare-screen.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-7776696937751658312
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/10/model-comparison-logical-model-uml.html
draft: true
---

![EMF logo]({{ site.url }}/images/blog/2011/emf_logo.png)

We just promoted an EMF Compare 1.3 integration build providing all the latest developments regarding EMF Compare. In a nutshell:

- **Logical Model** support for team operations (more especially with the eGit team provider)
- **UML** semantic comparison with dedicated management of profiles, stereotypes, and **dependencies across changes**
- **GMF** generic bridge for graphical comparison
- **Papyrus** specific bridge for UML diagrams comparison
- **EcoreTools** specific bridge for Ecore diagrams comparison

[![Graph compare screen]({{ site.url }}/images/blog/2011/graphcompare-screen.png)]({{ site.url }}/images/blog/2011/graphcompare-screen.png)

The build is here:

https://download.eclipse.org/modeling/emf/compare/updates/interim/1.3/

(subsequent updates will be pushed here too)

Depending on what you are trying to install you might need the orbit update site (google collection):

https://download.eclipse.org/tools/orbit/downloads/drops/R20110523182458/repository

The Indigo one (papyrus, gmf and Ecoretools):

https://download.eclipse.org/releases/indigo

Please, if you are interested in any of this change, go grab the build and have a try. We will welcome your feedback through the bugzilla: https://bugs.eclipse.org/bugs/enter_bug.cgi?product=EMF&component=Compare

