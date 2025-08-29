---
layout: post
title: "Graphical, textual, table, trees, its your call, to us its just EMF models"
date: '2012-03-05T12:44:00.001-08:00'
categories: [modeling]
tags:
  - eclipse
  - diagram
  - xtext
  - obeo designer
modified_time: '2012-03-06T00:51:17.320-08:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-4451408571424473580
blogger_orig_url: https://model-driven-blogging.blogspot.com/2012/03/graphical-textual-table-trees-its-your.html
---

Lately I've been making sure the upcoming Designer 6.0 release still plays well with Xtext. Results: fairly good. The newly introduced "Modeling Project" lets you behave with your Xtext models just like any other kind of models. Everything is synchronized; you can edit using the Xtext Editor, or using the Graphical modeler and the other one gets automatically refreshed. It just feels right.

One identified glitch so far: Xtext DSLs having references to JVM types might need a bit more work.

CDO, Xtext, Acceleo ... the product allows you to leverage the Eclipse Modeling ecosystem while having a huge productivity boost defining modeling environments. Of course we can still argue whether the state machine is more readable using the text or the diagram ;)

Some niceties are visible for those who want to have a deeper look:

- the State "Soon" has a specific grayish style because it's not linked to transition (incoming or outgoing)
- the Transition to Event blue dash link uses the "Edge on Edge" new feature for 6.0.
- and the "Connect" tool in the palette is smart enough to "do the right thing" depending on where you click: from State to State or Transition to Event. One tool to bind them all!

But where does the "PlanningTheTravel" to "InThePlane" edge come from? I created this transition using the graphical modeler. Xtext won't allow to save the model in this state because of the textual syntax, that's why the graphical modeler has been specified in a way which leads to the edge being red.

When building the basis of the modeler takes minutes of work, you have enough time to think about user experience and focus on providing the right feedback, at the right time.

I'm quite proud of what's cooking for this 6.0 release :)

