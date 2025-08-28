---
layout: post
title: XML files comparison/merge
date: '2007-03-20T17:34:00.000-07:00'
tags:
  - eclipse
  - compare
  - acceleo
  - modeling
categories: [modeling]
modified_time: '2009-05-07T08:25:06.025-07:00'
thumbnail: https://1.bp.blogspot.com/_u5tMWln_Ie8/SXsDG5Moo5I/AAAAAAAAAFY/kxbeVOlsmFU/s72-c/emfcomparexml.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-1637851078079211243
blogger_orig_url: https://model-driven-blogging.blogspot.com/2007/03/xml-files-comparisonmerge.html
---

On the EMFT mailing-list, Martin Taal asked me if EMF compare component was useful when one has to handle XML files.

Thanks to the EMF/XSD project this feature just comes at no cost! If you create your metamodel using an XSD then the model will be serialized in its native XML format but in the EMF compare point of view, it’s just another EMF model! Then you’re able to compare, and of course merge modifications on the files.

Here’s a screenshot of the tool comparing two XML files coming from the well-known “Library” example (sorry I did not put nice icons on the models ;) )

[![EMF Compare XML]({{ site.url }}/images/blog/2007/xml-files-comparisonmerge/s400_emfcomparexml.png)](https://1.bp.blogspot.com/_u5tMWln_Ie8/SXsDG5Moo5I/AAAAAAAAAFY/kxbeVOlsmFU/s1600-h/emfcomparexml.png)

The XSD project really should have more visibility, it’s obviously useful in many use cases where XML matters and EMF provides so many nice features, you should not miss that!

