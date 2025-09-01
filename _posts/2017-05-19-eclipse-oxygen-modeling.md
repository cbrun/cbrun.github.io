---
layout: post
title: 'EcoreTools: user experience revamped thanks to Sirius 5.0'
categories: [eclipse]
tags:
  - eclipse
  - sirius
  - modeling
  - emf
  - acceleo
excerpt: "A hands-on look at EcoreTools’ Oxygen revamp powered by Sirius properties: for EMF/Sirius tool builders and modelers; why it matters—lighter code, better UX, and new dialogs landing in Oxygen M7."
---

Every year the Eclipse M7 milestone act as a very strong deadline for the projects which are part of the release train: it's then time for polishing and refining!

<blockquote class="twitter-tweet" data-lang="fr"><p lang="en" dir="ltr">Time&#39;s up ! Pencils down, it&#39;s M7 !</p>&mdash; Cédric Brun (@bruncedric) <a href="https://twitter.com/bruncedric/status/13356256886">4 mai 2010</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

When your company is responsible for a number of inter-dependent projects some of them core technologies like [EMF Services](https://projects.eclipse.org/projects/modeling.emfservices){:target="_blank"} , the GMF Runtime, others user facing tools like  [Acceleo](https://www.eclipse.dev/acceleo/){:target="_blank"},  [Sirius](https://www.eclipse.dev/sirius/){:target="_blank"} or [EcoreTools](https://www.eclipse.dev/ecoretools/){:target="_blank"}, packaging and integration oriented projects like Amalgam or the Eclipse Packaging project and all of these releases needs to be coordinated, then may is a busy month.

<blockquote class="twitter-tweet" data-lang="fr"><p lang="en" dir="ltr">This week: M7 milestones for EcoreTools, Amalgam, Sirius, testing the Modeling package. Plot twist: 3 work days ! <a href="https://t.co/msqQkImRu4">pic.twitter.com/msqQkImRu4</a></p>&mdash; Cédric Brun (@bruncedric) <a href="https://twitter.com/bruncedric/status/727412029292711936">3 mai 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I'm personally involved in EcoreTools which makes me in the position to step in the role of the consumer of the other technologies and my plan for Oxygen was to make use of the Property Views support included in Sirius. This support allows me, as the maintainer of EcoreTools to specify directly through the `.odesign` every Tab displayed in the **properties view**. Just like the rest of Sirius it is 100% dynamic, no need for code generation or compilation, and complete flexibility with the ability to use queries in every part of the definition.

Before Oxygen EcoreTools already had property editors. Some of them were coded by hand and were developed more than 8 years ago. When I replaced the legacy modeler by using Sirius I made sure at that time to reuse those highly tuned property editors. Others I generated using the first generation of the [EEF Framework](https://eclipse.org/eef/#/){:target="_blank"} so that I could cover every type of Ecore and benefit from the dialogs to edit properties using double click. The [intent at that time](https://cedric.brun.io/ecoretools-20-luna-revival/) was to make the modeler usable in **fullscreen** when no other view is visible.

Because of this requirement I had to wait for the Sirius team to make its magic: the properties views support was ready for production with [Sirius 4.1](https://www.eclipse.dev/sirius/whatsnew/whatsnew4-1.html), but this was not including any support for dialogs and wizards yet. 

Then magic happened: the support for dialogs and wizards is now completely merged in Sirius, starting with M7. In EcoreTools the code responsible for those properties editors represents more than 70% of the total code which peaks at 28K.

<figure>
    <a href="{{ site.url }}/images/blog/properties/locs.png"><img src="{{ site.url }}/images/blog/properties/locs.png"></a>    
    <figcaption>Lines of Java code subject to deletion in EcoreTools</figcaption>
</figure>

In gray those are the plugins which are subject to removal once I use this new feature, as a developer **one can only rejoice at the idea of deleting so much code!**.

I went ahead and started [working](https://git.eclipse.org/r/#/c/96674/) on this, the schedule was tight but thanks to the ability to define reflective rules using **Dynamic Mappings** I could quickly cover everything in Ecore and get those new dialogs working. 

<figure>
    <a href="{{ site.url }}/images/blog/properties/ng-dialogs-ecoretools.png"><img src="{{ site.url }}/images/blog/properties/ng-dialogs-ecoretools.png"></a>    
    <figcaption>New vs old dialogs</figcaption>
</figure>


Just by using a dozen reflective rules and adding specific *Pages* or *Widgets* when needed.

<figure>
    <a href="{{ site.url }}/images/blog/properties/vsm.png"><img src="{{ site.url }}/images/blog/properties/vsm.png"></a>    
    <figcaption>The tooling definition in ecore.odesign</figcaption>
</figure>


It went so fast I could add new tools for the **Generation Settings** through a specific tab.

<figure>
    <a href="{{ site.url }}/images/blog/properties/genmodel.png"><img src="{{ site.url }}/images/blog/properties/genmodel.png"></a>    
    <figcaption>Genmodel properties exposed through a specific tab</figcaption>
</figure>

And even introduce a link to directly navigate to the Java code generated from the model:

<figure>
    <a href="{{ site.url }}/images/blog/properties/ecoretools-navigate-java.png"><img src="{{ site.url }}/images/blog/properties/ecoretools-navigate-java.png"></a>    
    <figcaption>Link opening the corresponding generated Java code.</figcaption>
</figure>

Even support for EAnnotations could be implemented in a nice way:

<figure>
    <a href="{{ site.url }}/images/blog/properties/eannotations.png"><img src="{{ site.url }}/images/blog/properties/eannotations.png"></a>    
    <figcaption>Tab to add, edit or delete any EAnnotation</figcaption>
</figure>

As a tool provider I could focus on streamlining the experience, providing tabs and actions so that the end user don't have to leave the modeler to adapt the generation settings or launch the code generation, give visual clues when something is invalid. I went through many variants of these UIs just to get the feel of it, as I get an instant feedback I only need minutes to rule out an option.  I have a whole new dimension I can use to make my tool super effective.

**This is what Sirius is about, empowering the tool provider to focus on the user experience of its users.**

It is just one of the many changes which we've been working on since last year to improve the user experience of modeling tools, Mélanie and Stéphane will present a talk on this very subject during EclipseCon France at Toulouse: ["All about UX in Sirius."](https://www.eclipsecon.org/france2017/session/all-about-ux-sirius).

All of these changes are landing in [Eclipse Oxygen](https://www.eclipse.dev/downloads/index-developer.php){:target="_blank"} starting with M7, those are newly introduced and I have no doubt I'll have some polishing and refining to do, I'm counting on you to [report anything suspicious](https://bugs.eclipse.org/bugs/enter_bug.cgi?product=Ecoretools){:target="_blank"}
