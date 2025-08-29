---
layout: post
title: "Mylyn Intent @ EclipseCon 2011"
date: '2011-03-03T05:48:00.000-08:00'
categories: [eclipse]
tags:
  - eclipsecon
  - eclipse
  - intent
modified_time: '2011-03-03T07:44:18.920-08:00'
thumbnail: https://3.bp.blogspot.com/-eWRpNigecMc/TW-v4_J6L8I/AAAAAAAAAbk/0vE-Ksl34-I/s72-c/featurescapture.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-8297330572755532929
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/03/mylyn-intent-eclipsecon-2011.html
---

In case you're not aware (yet ;) ) the **Mylyn Intent** [proposal](https://www.eclipse.dev/proposals/mylyn.docs.intent/) is going forward — if everything goes well we'll be able to get a shiny git repository on Eclipse.org in the incoming weeks.

Mylyn Intent is going to help you **co-document** and design things. As we consider that code activity is part of the design itself, the tool analyzes your source code and projects to assist documenting it.

What does "assist" mean in this context?

At any time, you can synchronize your documentation artifacts regarding the corresponding models and source code. The really interesting things happen when it is not synchronized: you'll then be able to compare the **expected design** versus the actual one and, either update the doc, or update the code depending on what makes sense.

The "design" word has a broad meaning, and indeed under this term we place anything that we formalize through an Ecore model.

It really is up to your team and development process. Here is an example of what you could want to capture if you develop Eclipse plugins:

[![Features capture]({{ site.url }}/images/blog/2011/mylyn-intent-eclipsecon-2011/s400_featurescapture.png)]({{ site.url }}/images/blog/2011/mylyn-intent-eclipsecon-2011/s1600_featurescapture.png)

This one is pretty flexible and straightforward; you could come up with a slightly more complex model taking in account the versioning and change management aspects.

Basically this model captures every feature targeting either the end users or the developers. For a developer feature, one has to associate at least one corresponding API exported by a bundle; for each API, one has to associate the corresponding unit tests. For an end user feature, an acceptance test is required and it should be associated to an interaction (this part is left as an exercise to the reader ;)).

I already hear you screaming: but you said it would be fun to document!? I'll have to fill all that information?

Don't panic.

[![Features capture synchronized]({{ site.url }}/images/blog/2011/mylyn-intent-eclipsecon-2011/s400_featurescapturewithsynchronized.png)]({{ site.url }}/images/blog/2011/mylyn-intent-eclipsecon-2011/s1600_featurescapturewithsynchronized.png)

With a blue highlight now: the things which are going to be synchronized with your development environment. What does that mean? It means you won't have to dig yourself through the code finding unit tests, filling the bundle and exported packages — **Intent will do this for you** and will be able to quickly update your documentation. Furthermore, once you're back on coding, **Intent will still work** and check that your changes are in sync with the doc, telling you when it's not.

The non-blue things — you'll have to describe those in your document; Intent really can't figure it out for you.

Please note that this is an example of what can be achieved plugging a specific model and the corresponding synchronization code in Intent; you'll be able to plug-in your own very soon.

Let's go back to the point: what does Intent offer then as a platform? What does Alice have to do with this? How does she look like?

You'll figure it out at [EclipseCon on Tuesday 22th, in Steven Creek at 11:10](https://www.eclipsecon.org/2011/sessions/?page=sessions&id=2199). Don't miss it.

