---
layout: post
title: "On being open and transparent"
date: '2013-01-31T04:19:00.001-08:00'
categories: [eclipse]
tags:
  - foss
  - emf compare
  - eclipse
  - community
modified_time: '2013-01-31T04:22:51.759-08:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-6882059087189884358
blogger_orig_url: https://model-driven-blogging.blogspot.com/2013/01/on-being-open-and-transparent.html
draft: true
---

We always intend to run our Eclipse projects as real open-source projects. Being open, transparent and so on. The Eclipse Development process forces you to do so in some way; the simultaneous release brings a bit more constraints in this regard but in the end, if you want a truly open project you'll need to do more.

Let's take EMF Compare. It quickly jumped into the release train, adopted the Eclipse practices, got used by other components and had a [number of major contribution.](https://www.eclipse.dev/projects/ip_log.php?projectid=modeling.emf.compare)

We have two main groups of adopters: the first group is comprised of end-users, which mostly have the perception the problem itself of comparing models is quite easy and it should "just works". They tend to report bugs, UI glitches, and sometimes even with patches. The second group is researchers; they know the problem is [not that easy](https://bugs.eclipse.org/bugs/show_bug.cgi?id=399361#c3) and having this component enables all kind of experiments on top of models for them. They tend to use compare in contexts we never ever envisioned.

We had several fairly big contributions from the second group (research) among the years and have always been keen in integrating them, getting them on board in the team and in the release process. But the contributors tend to fade away when their research subject changes or when they leave the academic world. The problem with "big" contributions is: we can't really maintain those over time with just the core team.

We also participated in several google summer of code programs, but so far never really managed to transform students into day-to-day committers.

Driven by the first group of user, we rewrote many of the core code of Compare last year, and now is a good time to get more people aboard.

We acknowledged that conferences, bugzilla, release reviews, and blog posts were not enough, and we started a bunch of actions:

Being visible

Includes posting notes on the interweb about progress, new use cases. Giving talks in tech or academic conferences, and having a comprehensive documentation.

With the 2.x stream, we had to go over all of our documentation anyway; the [User Guide](https://wiki.eclipse.org/EMF_Compare/User_Guide) is now in a better shape.

A build system you can launch@home

Building Compare is just a matter of `mvn clean package`

you can point to a specific target platform (we tend to keep the widest compatibility possible) with

`mvn clean package -Pjuno`

or `mvn clean package -Pkepler`

launching the tests is just as easy: `mvn clean verify -Pkepler`

As you would expect, the builds are run on the [eclipse public server.](https://hudson.eclipse.org/hudson/job/emf-compare-master/)

The only part of the build which depends on the eclipse infrastructure is the signing and promote process, but those are kept in particular profiles.

Contributor 101

We describe our expectation regarding contribution in the [Contributor Guide](https://wiki.eclipse.org/EMF_Compare/Contributor_Guide). Our requirements regarding checkstyle, API tooling, specifications documents are described there.

Setting our expectation can be seen as a new barrier to contribution, but on the other hand our expectations have always been that way and not describing it lead to misunderstandings: your contribution is valuable, make no mistake, but most of the time there is way more to do than just dropping a line of code in the bugzilla.

Gerrit looked like a good way to ramp up; a contributor can have feedback from the committers, but also from the automated build launched on top of his changes. This looks like a win win so we decided to migrate to gerrit and to [setup a build](https://hudson.eclipse.org/sandbox/job/emf-compare.gerrit/) which checks the tests on top of the platforms we are currently supporting. The [Eclipse wiki](https://wiki.eclipse.org/Gerrit) is highly valuable for this, and the webmasters have again demonstrated their support in this process.

We'll see how it goes over time; I'm not 100% buying gerrit itself which can be quite intimidating and I'm looking forward to the list of cons [Miles](https://milesparker.blogspot.fr/) will soon publish ;), but it feels right to have this public and open staging area with constant feedback.

Documentation also is a key ingredient here. Have a look on the [Developer Guide](https://wiki.eclipse.org/EMF_Compare/Developer_Guide); I wouldn't say it's complete because it's not, but you can at least start and have a rough understanding of how Compare works behind the scene.

We're not completely done here; we still have to list "low hanging fruits" - aka Junior Jobs or tasks which can be tackled to discover Compare's internals.

Engage

To engage developers — adopters which might turn into contributors and maybe at some point committers — you have to at least support them. [Laurent](https://eclipsemde.blogspot.fr/) is checking the following channels besides the bugzilla: the Eclipse forums/newsgroup and stackoverflow. We always had a great example of that in the EMF community through Ed's relentless effort on the newsgroups.

But to take part in the development of a project, you also need to know what's going on. We were missing a real channel for this: notifying peoples when we drafted the work we are starting and engaging them in a potential discussion about these evolutions. We recently decided to use the emf-dev mailing list for that; you might have seen a [few](https://dev.eclipse.org/mhonarc/lists/emf-dev/msg01551.html) [examples](https://dev.eclipse.org/mhonarc/lists/emf-dev/msg01553.html) [lately](https://dev.eclipse.org/mhonarc/lists/emf-dev/msg01558.html), the golden rule being: these mails are just a starting point for further discussions into a given bugzilla. We won't turn the mailing-list as a very chatty place; on the other hand with only a dozen of threads for one year which are not related to committer election or project meta-data I think there is room for more discussions.

I can't say this triggered a lot of reaction so far but I'd love to see other projects doing that on the emf mailing list.

Predictability

Always set expectations. We used to have a fairly thin project plan only describing themes; we now have a detailed one:

[EMF Compare 2.1 project plan.](https://www.eclipse.dev/projects/project-plan.php?projectid=modeling.emf.compare)

One can see which bugzilla tickets we'll work on during which milestone of a given release.

In the process we cleaned up our bugzilla, closing pending tickets, often with a comment "this is no longer true for 2.x, it just rocks".

Also set expectations on a given issue/bugzilla. We always tend to think: "your problem is a real one, we'll have to tackle it at some point", and let the thing open waiting for the moment we'll get back to it. Sometimes, this moment only comes months or years after the original report. Being clear whether we'll work right away on something you reported is important, and stating the contrary is an occasion for an adopter to get onboard.

As a side note, there are times that we look at a bug, think that "this is a totally stupid mistake" ... but then simply forget about it (we're working on something else, we're not on the good branch to tackle it directly...). Do not hesitate to ping us if we do not answer to trivial bugs (such as https://bugs.eclipse.org/bugs/show_bug.cgi?id=367527) in a timely manner.

Conclusion

We already have a fairly good track records of openness with many contributions in the history of the project; we'll see if doing so much more efforts will have an impact and I'll sure get back to you then. I can only assure you one thing: it takes a bit more time, it takes commitment, but it feels good.

