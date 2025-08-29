---
layout: post
title: "Compare/Helios - Every Second Counts"
date: '2010-04-28T05:43:00.000-07:00'
categories: [eclipse]
tags:
  - performance
  - eclipse
  - compare
  - acceleo
modified_time: '2010-04-28T07:27:07.112-07:00'
thumbnail: https://3.bp.blogspot.com/_u5tMWln_Ie8/S9gt4IR8UQI/AAAAAAAAASw/J8dPvXGk1OE/s72-c/beforeSprint.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-5291931750421210200
blogger_orig_url: https://model-driven-blogging.blogspot.com/2010/04/comparehelios-every-second-counts.html
---

I tend to break a lot of keyboards. Not because I release all the aggression that I hold deep within me on them, but because I drool testing the product Obeo is going to launch — really soon now.

During EclipseCon 2010 it struck me that some keyboards might have died because of EMF Compare. Ok, no more drooling here; the colors are nice, but when you are using compare with pretty decent models (like thousands of elements) you end up thinking it could be faster.

**Hold your breath**, order your very last keyboard which you'll use for a long time now — Compare's scalability has been improved **a lot** both in terms of performance and memory.

This work was pretty focused on the matching pipeline. There is room for improvements in the other parts of compare (especially the UI), but the matching was just so obviously slow and is even called 2 times for the 3-way match. That was just making sense to fix things there.

The performance test case is using UML models containing 1,000 to 256,000 elements organized in a decent way and is matching them several times. Here are the results before the scalability sprint:

[![Before sprint chart]({{ site.url }}/images/blog/2010/comparehelios-every-second-counts/s400_beforeSprint.png)]({{ site.url }}/images/blog/2010/comparehelios-every-second-counts/s1600_beforeSprint.png)

_Yes we have quite a strange value for the 1000 elements model; after investigation it looks like it's just some kind of corner case._

The last models have no time result for the simple reason they use all my memory and I end up with this **dreaded** OOM error.

Here are the figures after the sprint:

[![After sprint chart]({{ site.url }}/images/blog/2010/comparehelios-every-second-counts/s400_afterSprint.png)]({{ site.url }}/images/blog/2010/comparehelios-every-second-counts/s1600_afterSprint.png)

Now I can feel from here that you've been **thrilled** by all these figures and you only want one thing: _to get your hands on this release_. The Helios M7 release will be a good time to do so — wait for a few more days and go ahead: give us feedback!

Not only will the Helios release provide these major performance enhancements but the future looks even better: Stefan will work on a new match engine implementation focused on scalability for his Google Summer of Code.

Waking up as every morning, getting up but being a bit happier than usual as I know I made progress on something important for adopters :)

Please, keep in mind that **your** feedback made me work on this — thanks again.

