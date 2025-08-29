---
layout: post
title: "Eclipse Modeling Survey results"
date: '2010-06-18T01:50:00.000-07:00'
categories: [eclipse]
tags:
  - eclipse
  - amalgamation
  - acceleo
modified_time: '2010-06-18T07:32:14.601-07:00'
thumbnail: https://2.bp.blogspot.com/_u5tMWln_Ie8/TBs4EOCQ0jI/AAAAAAAAATY/iuvwfIcGfR4/s72-c/commiter.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-89262900413695265
blogger_orig_url: https://model-driven-blogging.blogspot.com/2010/06/modeling-survey-results.html
---

The survey has been going on for more than one week now and the trends are only enforcing themselves. Let's summarize it:

[![Committer vs non-committer]({{ site.url }}/images/blog/2010/modeling-survey-results/s400_commiter.png)]({{ site.url }}/images/blog/2010/modeling-survey-results/s1600_commiter.png)

First, the audience represents **many non-committers (2/3)** though the committers are still quite represented. That's quite consistent with what I was expecting: the survey was published on the planet, some newsgroups and through Twitter and as such targeting committers or adopters following quite closely what's happening in Eclipse Modeling.

![Package size]({{ site.url }}/images/blog/2010/modeling-survey-results/s400_packagesize.png)

Concerning the package size, we're right now at **250 MB** — it looks like it's mostly OK but being a bit smaller would still be nice.

As the package is an SDK, we could probably drop most of the duplicated javadoc in the plugins.

[![Best practices]({{ site.url }}/images/blog/2010/modeling-survey-results/s400_bestpractices.png)]({{ site.url }}/images/blog/2010/modeling-survey-results/s1600_bestpractices.png)

This one is interesting — it's something we're hearing again at each Eclipse conference. Users do want **more documentation**; moreover best practices are hard to reveal through the wiki, newsgroup and online help jungle.

There is probably something to do here but, hey, there is an [EMF Book](https://www.informit.com/store/product.aspx?isbn=9780321331885) already, an [Eclipse Modeling](https://www.informit.com/store/product.aspx?isbn=0321580540) one, and everybody can contribute on the wiki, so **why isn't this urgent need covered yet**?

It might be because:

- People are not even aware of these books or books are old-fashioned now — all content should be on the web!
- It's so hard to understand what each project is providing that one really needs some _Modeling Guide_.
- As a user you always want doc even if you won't ever read it — it just gives you the confidence that the technology is not going to vanish in a glimpse.
- [ ] <— any opinion expressed through the comments

It's even more disturbing when ...

![Invests]({{ site.url }}/images/blog/2010/modeling-survey-results/s400_invests.png)

Yes, **most people would be willing to give time to make this happen.** We might need to do something here; maybe [crowdsourcing](https://wiki.eclipse.org/DocumentationGuidelines/CrowdSourcingExample) the doc would do the trick... What is pretty sure is I wouldn't like it if Eclipse Modeling committers spent half of their time documenting — we should make it easier for the adopters to contribute back.

And yes, writing doc and books takes a **huge amount of time**!

[![Examples]({{ site.url }}/images/blog/2010/modeling-survey-results/s400_examples.png)]({{ site.url }}/images/blog/2010/modeling-survey-results/s1600_examples.png)

I asked another related question in the survey about "examples". In fact examples are way easier to provide and, in my opinion, are more valuable in most cases. And when you look at it, **each project is already building its own examples,** but these examples cannot be composed in some way. Just like Toast is a best practices application for OSGi, we would need a modeling one.

At its beginning the Amalgam project was providing some; yet since these examples were not part of their target Eclipse project (EMF examples in EMF, ATL examples in ATL) they were not maintained correctly. As a result they are not reflecting the "state of the art" of Eclipse Modeling anymore... Maybe for the next release!

I'm done for the strong trends. Other questions like "Having on-the-shelf design and generation tools" or "Domain-focused UI instead of component-focused one" were quite uncertain.

A few more ideas or questions have been given through this survey. It will take another blog post to describe those.

Thanks again for your feedback!

