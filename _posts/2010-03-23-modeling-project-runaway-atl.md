---
layout: post
title: "Modeling Project Runaway : ATL"
date: '2010-03-23T15:30:00.000-07:00'
categories: [eclipse]
tags:
  - eclipsecon
  - eclipse
  - atl
excerpt: "ATL gets a major tooling refresh—refining mode, improved editors, and a Java API—highlighted in the ‘Modeling Project Runaway’ session."
modified_time: '2010-03-23T15:30:00.444-07:00'
thumbnail: https://1.bp.blogspot.com/_u5tMWln_Ie8/S6Izgd_XcvI/AAAAAAAAARQ/pMIqMbOgAnk/s72-c/atl.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-8754344415437460672
blogger_orig_url: https://model-driven-blogging.blogspot.com/2010/03/modeling-project-runaway-atl.html
---

["Modeling Project Runaway"](https://www.eclipsecon.org/2010/sessions/sessions?id=1278) was the talk you had to attend to get a vision of what is going on in Eclipse Modeling and, more especially, how lively this community is. The talk was even too short for EEF to get in, but this project had its own talk yesterday.

In an [Ignite](https://en.wikipedia.org/wiki/Ignite_%28event%29)-style event, I did a quick demo of the new features in the ATL tooling. ATL is a model-to-model transformation language; it's incredibly powerful and usable in many different contexts. It allows you to transform information from a formalism to another one or to refine a model.

ATL has been around for quite a long time in Eclipse and has proven to be quite mature. Nevertheless, great new features have been added this year!

- The tooling editor has been reworked, providing content assist everywhere, hover tooltips, "open declaration" and even code templates to quickly get started.
- A long-awaited feature is the "refining mode". In this mode the transformation is directly applied on the loaded instances of the model; you can then use an ATL transformation as a refactoring script and integrate it in your editor. Before, the synchronization could only be on the Resource level, forcing you to save and then reload the model.
- Acceleo provides a Java API to launch your code generation — ATL now provides the same thing! It's trivial to launch ATL within any other tooling, just use the Java API. Furthermore, you can even launch it as a standalone Java application!

Demo time!

[![ATL features thumbnail]({{ site.url }}/images/blog/2010/modeling-project-runaway-atl/s320_atl.png)](https://literate.modeling.free.fr/modeling/atl/ATL_features.htm)

By the way ATL is one click away from you: just install the Helios [modeling package](https://www.eclipse.dev/downloads/packages/) and use the discovery UI to try this out!
