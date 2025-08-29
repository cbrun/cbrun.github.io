---
layout: post
title: "Will you be Sirius at EclipseCon Europe ?"
date: '2013-09-19T01:05:00.000-07:00'
categories: [eclipse]
tags:
  - eclipsecon
  - sirius
  - eclipse
modified_time: '2013-09-19T01:19:00.739-07:00'
thumbnail: https://cedric.brun.io/images/blog/2013/esa2-t.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-9086028157993160208
blogger_orig_url: https://model-driven-blogging.blogspot.com/2013/09/will-you-be-sirius-at-eclipsecon-europe.html
---

We've been in some sort of "Stealth mode" since the proposal for Eclipse Sirius got accepted. It did not make sense to us to communicate on Sirius as long as it's not there, in Eclipse. That said, the summer actually was quite intense; I'll start by a quick status report:

Pierre-Charles worked on preparing the move to the Eclipse infrastructure and the Foundation IP Team reviewed the code. We just got the green light from Sharon (kudos to her!) and the code was committed by Stéphane Bonnet (Thales) two weeks ago. The code is now hosted on [git.eclipse.org](https://git.eclipse.org/c/sirius/org.eclipse.sirius.git/). [Continuous integration](https://hudson.eclipse.org/sirius/) and [gerrit](https://git.eclipse.org/r/#/q/org.eclipse.sirius,n,z) are operational though builds are not published on Eclipse.org yet.

Right now the team is working on 6 different streams to prepare for upcoming releases, notably Obeo Designer 6.2 and service releases for Obeo Designer 6.1 and 6.0. The team will progressively ramp up on the Eclipse.org infrastructure as our 6 different streams are delivered.

We are also taking the opportunity of this big namespace change to clean-up some long deprecated APIs and to rethink the way Sirius is modularized. See the [wiki for more details](https://wiki.eclipse.org/Sirius/Modularization) but in the end, the APIs we are publishing right now will probably move quite a lot until the 1.0 release. We are soon going to [draft the plan](https://projects.eclipse.org/projects/modeling.sirius) for the 0.9 and 1.0 releases and officially announce our participation to Eclipse Luna.

In the meantime the Obeo Marketing and Communication team is working on giving the project a visual identity. I can't wait for it!

In a nutshell, everything will be ready for EclipseCon Europe: we'll have RC quality builds of Sirius 0.9 by then, a website, more content on the wiki, published downloads, Obeo and Thales will be actively working on the Eclipse git repository and bugzilla.

![EclipseCon Europe]({{ site.url }}/images/blog/2013/eclipsecon_logo.png)

You'll get to see the Sirius in action during EclipseCon Europe; we worked on a few cool talks for you:

![Arduino]({{ site.url }}/images/blog/2013/Arduino_Uno_Angle.jpg)

It will start on Tuesday at 15:00, right after the keynote. Mélanie will turn Eclipse into an Arduino Programming platform for kids, providing a visual programming environment not unlike [Ardublock](https://blog.ardublock.com/) (you bet, based on Sirius). How can we tweak the Eclipse user experience so that even kids can use it?

On Wednesday at 14:30, Sirius, Changing the Game of Systems Architecture, a sponsored talk presented by Etienne and Frederic in which you'll get to learn about a collection of Sirius case studies from a space agency to an insurance company and for each of them how Eclipse Modeling — and Sirius — have been effectively combined.

![Sirius ECF]({{ site.url }}/images/blog/2013/sirius-ecf.jpg)

At 16h15 Stéphane Bonnet (Thales) and Pierre-Charles will present Sirius By Example: Build Your Own Diagram, Table and Tree Editors in 20 minutes. This talk will give an overview of the main Sirius features, and show how to use it to create custom tooling around a given technology. You will also learn about the origin and history of Sirius and how it has been deployed in operational and intensive contexts within Thales. It was given at EclipseCon France, the room was packed and we had a very good feedback about it.

Right after this talk, at 17:00, I will present EcoreTools 2.0: The Making-Of — or "How to transform a GMF based modeler to a Sirius based one". You will discover how I used Sirius's features — some of them quite advanced — to re-design the user experience of EcoreTools.

Then the team will gather for a Sirius BOF (to be announced). You get to ask any question about Sirius and we will be glad to coach you in getting started with the technology.

![Booth]({{ site.url }}/images/blog/2013/booth-ece-france.jpg)

Last but no least, Obeo will have a booth during the whole conference; feel free to come by to ask questions or even just to have a chat. We are always eager to learn about use cases or experiments.

I'm looking forward to it. If you're interested in modeling and did not register for EclipseCon Europe yet, [consider doing it,](https://www.eclipsecon.org/europe2013/) I guarantee you'll learn a lot!

