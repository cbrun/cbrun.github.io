---
layout: post
title: 'Exploring Eclipse Plugins: beyond Terra Incognita'
date: '2009-10-09T06:54:00.000-07:00'
tags:
- eclipse
- cartography
- acceleo
- obeo
categories: [eclipse]
modified_time: '2009-10-09T08:24:18.244-07:00'
thumbnail: https://farm4.static.flickr.com/3040/2722476302_4bf25ea7b6_t.jpg
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-3244660270746656679
blogger_orig_url: https://model-driven-blogging.blogspot.com/2009/10/exploring-eclipse-plugins-beyond-terra.html
---

[![]({{ site.url }}/images/blog/2009/exploring-eclipse-plugins-beyond-terra/2722476302_4bf25ea7b6.jpg)](https://www.flickr.com/photos/maxbraun/2722476302/)

In software engineering the "**Terra Incognita**" boundary is never far away from where you're standing. Most software is lacking an "overview" documentation or model and you have to open your path yourself through the code trying to understand what's going on.

That's especially true when you are analyzing a legacy application in some kind of good old language not being considered, these days, as hype as SCALA. COBOL, NSDK are examples among others — reverse engineering becomes a requirement and at Obeo we are working hard [providing tooling](https://www.obeosoft.com/fr/pages/agility) so that our customers are able to understand and migrate to other technologies.

That said you don't need a flux capacitor requiring 1.21 gigawatts of electrical power to have this "understanding" issue with technologies. It's still a problem with the application we're building using 2009 ones; let's take the OSGi Bundles for the need of the demonstration.

I already did a draft implementation of a tooling easing the exploration of Eclipse plugin years ago using GMF, and we've got this nifty PDE visualization tools based on ZEST, but I was in the mood of trying again to build a tooling from the following principle:

- construct and explore **step by step**

Now that we built this [cool technology](https://www.obeosoft.com/fr/pages/obeo-designer/features/) enabling you to design your own modeling environment, I decided to give it another try.

Here is the result — please note that's a **one day** work and the **underlying runtime is in development** (you might catch a few bugs during the demo). Please also note that the demo capture software is not so friendly with the original color; we are rendering the diagram with more than 256 colors ;)

The legend is the following:

[![]({{ site.url }}/images/blog/2009/exploring-eclipse-plugins-beyond-terra/s400_legend.png)](https://1.bp.blogspot.com/_u5tMWln_Ie8/Ss9CzYPaWhI/AAAAAAAAAMQ/tyuq3a9Sym8/s1600-h/legend.png)

The plugins model is captured thanks to PDE APIs; we're going to explore the Eclipse plugins starting from Mylyn, building groups, and seeing what kind of relations those groups have with each other: dependency and/or extension.

[![]({{ site.url }}/images/blog/2009/exploring-eclipse-plugins-beyond-terra/s400_cartoplugins.png)](https://literate.modeling.free.fr/modeling/designer/plugins/demoplugins.htm)

So now the next step would be to build the **whole Galileo Map** step by step — anybody feels like a 21st century Magellan?

Here are a few extras:

![EMF Core dependencies]({{ site.url }}/images/blog/2009/exploring-eclipse-plugins-beyond-terra/s400_emf-deps.jpg)

![EMF Core extensions]({{ site.url }}/images/blog/2009/exploring-eclipse-plugins-beyond-terra/s400_emf-exts.jpg)

![Acceleo.org standalone plugins]({{ site.url }}/images/blog/2009/exploring-eclipse-plugins-beyond-terra/s400_carto_acceleo_standalone.png)

_Ok, that's Friday and I'm kinda lazy: no text annotations in the demo for now; maybe later if I've got thousand questions through the comments._
