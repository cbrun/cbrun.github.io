---
layout: post
title: "SysML Comparison and Contributions"
date: '2011-12-01T11:41:00.000-08:00'
categories: [modeling]
tags:
  - eclipse
  - community
  - compare
  - emf
modified_time: '2011-12-01T11:41:14.389-08:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-8928794163682835913
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/12/sysml-comparison-and-contributions.html
draft: true
---

Community and Ecosystem

The Juno release cycle has been very interesting for EMF Compare — as a project.

Discussions started through the Modeling Platform working group lead to the sponsorship of a bunch of new features (we covered those before but in a nutshell: UML dedicated support, UI enhancements, Graphical comparison support and Logical Model for EGit).

Meanwhile we took a number of actions to make this project a more welcoming area for contributions and to ease adoption; some of these actions are technical (documentation, build, tests and continuous integration) and others are focused on community growth (transparency, communication, [discussions with academic researchers](https://www.iwmcp.org/2011/)).

We are not done yet and have several remaining actions but we can already see some results:

- new adopters appeared and contacted us through the bugzilla with use cases we had not envisioned; trying to keep the answering delay reasonable helped a lot in converging to a patch. Within Eclipse itself we've seen several new projects adopting the technology.
- new features contribution: thanks to Arthur from Atos a [dedicated support for SysML](https://bugs.eclipse.org/bugs/show_bug.cgi?id=360757) model just got integrated and is now built. In those cases where timeframe is obviously bigger than a simple patch, git helps a lot.
- discussions with academics helped us drafting powerful new features for 2.0 like fingerprints-based matching (a complete blog post about this will come soon)

EclipseCon US will be a great place to share our experience. If you're interested or would like to see a specific topic within this scope, [feel free to add a comment](https://www.eclipsecon.org/2012/sessions/models-and-scm-eclipse-bright-future).

More about SysML ...

The SysML contribution is built on top of the UML dedicated support; it just got integrated and built. It never got released so it might be a bit rough, and we still have some issues we [want to fix for 1.3](https://bugs.eclipse.org/bugs/show_bug.cgi?id=365285) but if you feel adventurous, [go get the bits here](https://download.eclipse.org/modeling/emf/compare/updates/interim/1.3/)! (update site)

