---
layout: post
title: The 20 minute Graphical Modeler based on Eclipse
date: '2009-05-13T10:02:00.000-07:00'
tags:
- graphical
- eclipse
- viewpoint
- acceleo
categories: [modeling]
modified_time: '2009-05-13T11:21:55.918-07:00'
thumbnail: https://1.bp.blogspot.com/_u5tMWln_Ie8/SgsLjej2tHI/AAAAAAAAAJI/aKswPsPwwHM/s72-c/flowdiag_specify.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-1848800102029818548
blogger_orig_url: https://model-driven-blogging.blogspot.com/2009/05/20-minute-graphical-modeler-based-on.html
---

My last post about the flow model simulation was really missing a demo so that you get the **"live"** aspect of the model construction. No problem, that's a good occasion to show you a secret product we've been building on **top of the Eclipse Modeling projects** since a few years now. In my [_dictator_ position](https://model-driven-blogging.blogspot.com/2009/02/engineering-dictator-strikes-back.html) on this product you can guess I'm quite excited to show you that — nothing public came out about it until now but the first public release is not so far...

Let's stop the teasing and watch the content. Here are a few flash demos. If you're just interested in the resulting modeler, go directly to the last one showing the live model design. If you don't understand what's about that _flow_ stuff or are wondering how all that _load_ and _capacities_ properties get updated, have a look at my preceding post.

- Specify the modeler: https://literate.modeling.free.fr/modeling/designer/SpecifyModeler.htm

[![]({{ site.url }}/images/blog/2009/20-minute-graphical-modeler-based-on/s400_flowdiag_specify.png)](https://literate.modeling.free.fr/modeling/designer/SpecifyModeler.htm)

The first demos show the graphical modeler construction. In a few clicks, just defining the concepts you want to display, how you want to display them and how to retrieve them in the semantic model. You get your modeler in a matter of minutes.

I really like the **"specifying the modeler and using it side by side"** feature even if you need a big display for that.

- Customize with conditional styles: https://literate.modeling.free.fr/modeling/designer/CustomizeModeler.htm

[![]({{ site.url }}/images/blog/2009/20-minute-graphical-modeler-based-on/s400_flowdiag_customize.png)](https://literate.modeling.free.fr/modeling/designer/CustomizeModeler.htm)

Define "conditional styles" so that graphical shapes change depending on changes in the semantic model (node/edge sizes and colors). In this demo I also specify that a _CompositeProcessor_ reuses the graphical mappings defined for the diagram and that I should be able to create a sub diagram on a _CompositeProcessor_. The request language I'm using is **Acceleo**, but you could also use **OCL**.

- Use the modeler: https://literate.modeling.free.fr/modeling/designer/UsingModeler.htm

[![]({{ site.url }}/images/blog/2009/20-minute-graphical-modeler-based-on/s400_flowdiag_usage.png)](https://literate.modeling.free.fr/modeling/designer/UsingModeler.htm)

To be fair, the final modeler is more a 25 minute modeler than 20, but I get a first working modeler at minute 10 of the first demo.

Be sure that's only a tiny portion of what we've been able to achieve leveraging the Eclipse Modeling components ([EMF, GMF](https://www.eclipse.dev/modeling/), [Acceleo](https://www.acceleo.org), [Compare](https://www.eclipse.dev/modeling/emft/?project=compare#compare) just naming a few...) and the Eclipse Platform. Graphic modelers are one thing, but other representations matter — and I'm not even speaking about the "full viewpoint support".

Stay tuned for more eye candy ;)

