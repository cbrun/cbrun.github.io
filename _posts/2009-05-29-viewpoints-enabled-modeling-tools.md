---
layout: post
title: Viewpoints-enabled Modeling Tools
date: '2009-05-29T05:37:00.000-07:00'
tags:
- eclipse
- viewpoint
- sirius
- acceleo
- modeling
- ecore
categories: [modeling]
modified_time: '2009-05-29T07:56:06.558-07:00'
thumbnail: https://3.bp.blogspot.com/_u5tMWln_Ie8/Sh-3ZE0NAyI/AAAAAAAAAJY/bZpXkgra8KQ/s72-c/flow_viewpointsdefinition.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-8577426604884474196
blogger_orig_url: https://model-driven-blogging.blogspot.com/2009/05/viewpoints-enabled-modeling-tools.html
---

This post follows those showing how it's possible to leverage [EMF and JBoss Drools](https://model-driven-blogging.blogspot.com/2009/05/live-models-using-jboss-rules-drools.html) to get an interactive model updated considering business rules, and how you can get a set of [graphical modelers](https://model-driven-blogging.blogspot.com/2009/05/20-minute-graphical-modeler-based-on.html) to ease your design tasks and provide feedback while you're building your system.

Now let's focus on providing _"the right feedback at the right time"_. When you're designing a system, you're trying to reach the goal of building it **nicely** and making sure it fits **your requirements and constraints**. You're always balancing between different concerns: simplicity, agility, performance, safety...

Having good tooling for that is more than important, and tooling often failed until now: it provides many more information or possible actions than what you actually need — and not what's your focus **right now**.

Here come the viewpoints ([IEEE](https://standards.ieee.org/reading/ieee/std_public/description/se/1471-2000_desc.html)). Viewpoints-enabled tooling is able to extend, hide, or provide new representations and actions depending on **what you want to consider**. As building a system is always a trade-off between multiple criteria, you don't want to be overwhelmed with all the constraints feedback; you just want to see **relevant** information and be able to do **relevant** actions. The concept is quite similar to the Eclipse perspectives.

The first demo (a few minutes) provides an overview of the _tooling specification model_ we started in the last post. It's been completed with a few more representations, validation rules, and more importantly re-organized in terms of **viewpoints**.

[![]({{ site.url }}/images/blog/2009/viewpoints-enabled-modeling-tools/s400_flow_viewpointsdefinition.png)](https://literate.modeling.free.fr/modeling/designer/ViewpointsDefinition.htm)

The following demo (6 minutes) shows the usage of such a tooling, using (again) the simple "Flow" example.

[![]({{ site.url }}/images/blog/2009/viewpoints-enabled-modeling-tools/s400_flow_viewpointsusage.png)](https://literate.modeling.free.fr/modeling/designer/UsingViewpoints.htm)

Eclipse **is** great as a platform and enables you to build great tooling so that your users stay focused on their business issues (which are complex enough already). That's what we are trying to achieve with this product.

Moreover, **Eclipse Modeling** is a gem mine driven by enthusiastic people. Don't wait and come with us — resistance is futile ;)
