---
layout: post
title: "Eclipse Modeling : the definitive tutorial"
date: '2011-09-14T05:08:00.000-07:00'
categories: [modeling]
tags:
  - gsoc
  - eclipse
  - acceleo
modified_time: '2011-09-14T05:08:00.699-07:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-8314226034257898745
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/09/eclipse-modeling-definitive-tutorial.html
---

One of the things we keep hearing from adopters is: we need more doc — not just reference documentation but also how to use and combine the Eclipse Modeling components.

Richard Gronback's answer to these requests was to write a book. But as we are living in a fast-changing world filled with innovation, it quickly got outdated.

Reinaldo de Souza, a [GSOC](https://wiki.eclipse.org/Google_Summer_of_Code) student, did an amazing work as part of the Amalgamation Project. He prepared an awesome cross-modeling components tutorial: the design of an Android DSL using Ecore, providing a textual syntax using XText, customizing EMF editors using EEF up to generating the Android code using Acceleo.

The EMF domain model and Eclipse editors:
https://github.com/eclipse-soc/amalgamation-examples-emf

Xtext textual syntax for the DSL:
https://github.com/eclipse-soc/amalgamation-examples-xtext

Acceleo to generate the Android code:
https://github.com/eclipse-soc/amalgamation-examples-acceleo

It is more than just a start — it really is a complete tutorial with step-by-step instruction on the wiki and the corresponding projects one can import in his workspace.

https://github.com/eclipse-soc/amalgamation-examples-acceleo/wiki/Android-code-generation-with-Acceleo

The original idea was to provide also tutorials and examples for GMF or Graphiti. It could not be done in the timeframe but anybody wanting to continue the example with the same domain model using other components is very welcome!

Now we still have to package it properly so that the adopters can get it in a nicely integrated way in their IDE.

