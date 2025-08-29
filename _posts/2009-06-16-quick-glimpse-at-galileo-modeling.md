---
layout: post
title: Quick glimpse at Galileo Modeling Package
date: '2009-06-16T03:30:00.000-07:00'
tags:
- eclipse
- acceleo
- obeo
categories: [modeling]
modified_time: '2009-06-16T01:32:09.406-07:00'
thumbnail: https://2.bp.blogspot.com/_u5tMWln_Ie8/SjOA5c4r7oI/AAAAAAAAAJo/25e-VYWfvW4/s72-c/ecoretools.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-6597968654399650768
blogger_orig_url: https://model-driven-blogging.blogspot.com/2009/06/quick-glimpse-at-galileo-modeling.html
---

Eclipse Galileo aka _3.5 simultaneous release_ is coming soon. We now all have this fuzzy feeling when development stops and we stay here a bit dizzy, wondering what we'll do next.

Yet another release, yet another step in the direction of the best IDE, of the best Platform, of the best Modeling tooling or whatever goal you have. The eco-system is so diverse, every new release can't be reviewed as whole; you can only savour "just a bite of this big cake".

Even if I'm quite sensitive to all the good stuff added in the platform — _as a plugin developer these features make me happy every day_ — I'm gonna focus on only **some** features of the modeling package for Galileo.

Each year a few more modeling projects are joining the team for the simultaneous release; you're now getting a full-fledge modeling environment for Galileo.

Let's design stuff — that's what models are about, right? Thanks to **EcoreTools**, you now have a nice modeler for your domain models. The sexyfication of this modeler is great :) You now have nice gradients, shadows, and many views bringing you things you're used to in the Java tooling: Class hierarchy, Show references and so on.

![EcoreTools]({{ site.url }}/images/blog/2009/quick-glimpse-at-galileo-modeling/s400_ecoretools.png)

Definitely worth trying!

If you design your models with a team, you'll be happy to see EMF Compare when you want to merge your changes with those made by your coworkers.

![EMF Compare on Ecore]({{ site.url }}/images/blog/2009/quick-glimpse-at-galileo-modeling/s400_compare_ecore.png)

Compare graduated and has now the **1.0** stamp! It's seamlessly integrated with CVS, SVN, GIT and can diff and merge any kind of models.

Speaking about design, **xText** allows you to design your models using a textual syntax; that's pretty cool and the team worked hard this year — check it out!

Once you design your stuff, most of the time you want to transform that into something you can use for your development. There are basically two options here: _model to model_ transformation or _model to text_ transformation. Each one has pros and cons depending on your use case.

Eclipse Galileo provides pretty much anything you might want to transform your models, some of them being based on standards:

- Model To Text (aka code generation):
  - **JET** has been here for quite a long time now providing a steady and stable code generation technology.
  - **XPand** and **Acceleo** joined the release train this year providing template languages with great tooling, debug mode, full featured editors...
- Model To Model:
  - **QVT Operational** and **ATL** compete in the model to model area.

Work on **ATL** has been focused on user interface and API, which means **ATL** is now easier to use from both an end-user point of view and developer point of view.

I looooove the new wizards compared to the old one :)

![ATL wizard]({{ site.url }}/images/blog/2009/quick-glimpse-at-galileo-modeling/s400_atl3.png)

**Acceleo** is a complete rewrite from the Acceleo 2.x versions which made our team "Eclipse Award Winners". One thing that's cool with this rewrite is that from the beginning we're making sure the core generator is "standalone" and might be used without Eclipse — something we had a hard time to provide _a posteriori_ with Acceleo 2.X. Another common need is the ability to easily launch your generation from your Java code; it's most of the time quite tricky when you use your own language.

The Acceleo team came with a nice solution: next to every "main-like" template we generate a Java class which is this template API. Then you can easily launch the generation — you just have to create an instance of this Java class and launch it.

Here is a small and dumb template:

![Acceleo template]({{ site.url }}/images/blog/2009/quick-glimpse-at-galileo-modeling/s400_acceleo-template.png)

And here is the corresponding Java launcher:

![Acceleo Java launcher]({{ site.url }}/images/blog/2009/quick-glimpse-at-galileo-modeling/s400_acceleo-java.png)

Kicking your generation is just a class instantiation and a call to the **doGenerate(**) method! You have no excuse for not integrating your code generation into your editor.

In a nutshell Galileo brings the best of modeling with pragmatic components — you can't miss that!
