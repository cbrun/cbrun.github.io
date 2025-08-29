---
layout: post
title: EMF Compare now uses XMI_ID
date: '2007-03-26T14:43:00.000-07:00'
tags:
- compare
- modeling
categories: [modeling]
modified_time: '2010-03-01T00:37:42.802-08:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-3398213415942634780
blogger_orig_url: https://model-driven-blogging.blogspot.com/2007/03/emf-compare-now-uses-xmiid.html
---

The generic EMF comparison engine uses statistics in order to match elements. It compares their content, their type, the relations with other objects and their name. This process gives good results on many metamodels, especially specific ones, but it can be costly for instance on UML models because there are many attributes on each element. On the other side, big models and standard ones are often serialized in XMI using IDs.

The generic engine now uses these IDs if they are available in order to find matching elements: the cost is close to zero and the correctness is good. Next step is to use the functional IDs one may define in an Ecore metamodel.

Here comes a screenshot showing the current state of the EMF Compare project, comparing two UML files.

<figure>
  <a href="https://eclipse.dev/emf/compare/">
    <img src="{{ site.url }}/images/blog/2007/emfcompare-compare-merge.png" alt="EMF Compare comparing two UML files" />
  </a>
  <figcaption>EMF Compare comparing two UML files.</figcaption>
  </figure>

