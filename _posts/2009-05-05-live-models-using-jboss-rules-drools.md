---
layout: post
title: Live Models Using JBoss Rules (Drools) and EMF
date: '2009-05-05T09:03:00.000-07:00'
tags:
- modeling kata
- jboss drools
- eclipse
- acceleo
- live model
- emf
categories: [modeling]
modified_time: '2009-05-07T07:52:42.284-07:00'
thumbnail: https://2.bp.blogspot.com/_OJuY9x1lbxI/Se9tLzXRS_I/AAAAAAAAALU/ny6uKiFIev4/s72-c/essaim_abeilles.jpg
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-1036180728036140709
blogger_orig_url: https://model-driven-blogging.blogspot.com/2009/05/live-models-using-jboss-rules-drools.html
---

**Modeling Kata** here again! Models are useful to describe things, systems, knowledge — basically any information you want to organize and formalize will gain by using a solid formalism like [Ecore](https://www.eclipse.dev/modeling/emf/).

Structuring and describing is nice, but then most of the time you need to evaluate your design. One choice is using the validation tools so that any _"error in your design"_ is shown to you and you can fix it. The drawback of validation is that you can't easily get the **big picture** of your design quality corresponding to the constraints you defined.

Who can say that these bees invading my garden are organized in a nice or poor way? That's definitely **not a binary information**.

[![]({{ site.url }}/images/blog/2009/live-models-using-jboss-rules-drools/s400_essaim_abeilles.jpg)](https://2.bp.blogspot.com/_OJuY9x1lbxI/Se9tLzXRS_I/AAAAAAAAALU/ny6uKiFIev4/s1600-h/essaim_abeilles.jpg)

Another approach is designing your models with tooling **updating or self-constructing** other parts to give you information about its quality. Let's take a (quite naive but still interesting) example:

I defined a formalism for a "flow-like" language. You can use it to describe _DataSources_ and _Processors_ linked by _DataFlows_. Processors and DataFlows are capacity-bounded, which means they've got a maximum capacity and under given load will be _idling_ or _overused_.

Here is a class diagram displaying the simplest parts of the flow.ecore:

[![]({{ site.url }}/images/blog/2009/live-models-using-jboss-rules-drools/s400_flow_ecore.png)](https://4.bp.blogspot.com/_u5tMWln_Ie8/SgBrG2UiMCI/AAAAAAAAAIA/O-AZFjFMGSI/s1600-h/flow_ecore.png)

Here I'm mixing both the information I'll describe (a given system with _datasources, processors_ and _flows_) and the feedback about my design (the flow element usage). Note that every element here might be activated or not (see the _FlowElementStatus_ enumeration).

Now, to define my rules updating each value considering the overall model, I basically have the choice either to implement that in Java, or use a Rules Engine. Implementing in Java might look like a good idea but you quickly end up rebuilding an inference engine. Using **Drools** lets you focus on the rules. From there, the model can be updated live to give feedback on the design quality.

