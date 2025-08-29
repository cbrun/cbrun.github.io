---
layout: post
title: "Introducing Eclipse Sirius"
date: '2013-03-19T10:16:00.000-07:00'
categories: [obeo]
tags:
  - eclipse
  - acceleo
  - obeo
  - ecore
  - emf
modified_time: '2013-03-22T03:44:44.418-07:00'
thumbnail: https://4.bp.blogspot.com/-sdiNF9QpU08/UUcpF4VHxcI/AAAAAAAAGgs/QkCmFrnnfkk/s72-c/entities.jpg
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-7466617162319474411
blogger_orig_url: https://model-driven-blogging.blogspot.com/2013/03/introducing-eclipse-sirius.html
---

You might have noticed some signs of excitement from us lately, one being the following tweet:

<blockquote class="twitter-tweet" lang="fr">4:45 pm : I'm clicking on "send" and it's gonna rock.<br />— Cédric Brun (@bruncedric) <a href="https://twitter.com/bruncedric/status/309331351579009024">6 mars 2013</a></blockquote>
<script async charset="utf-8" src="//platform.twitter.com/widgets.js"></script>

What was sent at 4:45pm? a [new project proposal](https://www.eclipse.dev/proposals/modeling.sirius/) for Eclipse, one which, in my opinion, is a major event.

Let me introduce you to **Eclipse Sirius**!

Have you ever wanted a nice graphical environment customized for your domain data but been discouraged by the complexity of all the technologies needed to create one? Maybe you compromised and decided to use an existing format or notation, even if it does not completely fit your needs, just to benefit from the associated tools. Fear no more! Instead of adapting your needs to some existing tool, with Sirius the tooling adapts itself to you, as it should be. And you don't even need to learn about the Eclipse Modeling stack, we did it for you.

That said, if you want to tweak something you can always plug your customization in through the underlying frameworks, namely: GMF, GEF, EMF and the Eclipse Platform.

How did it all start?

It's no vaporware. We started the development of Sirius a few years ago with Thales. We've set-up together a great team to build this technology, known as Doremi at that time.

Thanks to this collaboration, we've reached a very high [level of maturity](https://fr.wikipedia.org/wiki/Technology_Readiness_Level): Sirius is used in many very large projects within Thales and it's been around in Obeo Designer for a few years already. It is also the foundation of several tools you can already find in the Eclipse Marketplace, [some](https://marketplace.eclipse.org/content/database-designer-indigo-version#.UUc2InFHq2A) [of](https://marketplace.eclipse.org/content/graal-designer-indigo-version#.UUc2J3FHq2A) [them](https://marketplace.eclipse.org/content/risk-analysis-designer-helios-version#.UUc2M3FHq2A) being installed by more than [2000 users a month.](https://marketplace.eclipse.org/node/622477)

We are not kidding.

This contribution to Eclipse means a whole new team will become committers. They have been working on Sirius for years and you already know them as contributors. You will now see those guys from Thales and Obeo co-leading and working in the open.

What about Obeo Designer?

Sirius is one Obeo Designer's components. Once published via Eclipse the Sirius open source version will be included in Obeo Designer.

Sirius being open-source doesn't change much besides strengthening Obeo Designer by significantly growing the user base of one of its components. This means more diverse usages, more tests "in the wild" and potentially more designers to reuse or extend.

Obeo Designer remains a commercial product: a strong and open platform to build and deploy your modeling environment with well integrated and tested components. It is the perfect companion for professional usage by bringing collaborative modeling and support.

Why?

First because it is in our DNA; we strive to build great products in the open. And our partners are supporting us on this, especially Thales, since Sirius is the result of many years of a joint and rich collaboration with Obeo.

Secondly to unleash the energies in Eclipse Modeling. There is a lot of interest in this domain; companies are in dire need of solutions but the cost to fill the gap between what they need and what Eclipse Modeling provides right now is too high. We are reducing this gap with Sirius and this will trigger more usage and more funding for Eclipse Modeling as a whole.

We also want to work with you, fellow committers and OSS tool providers, in building the best tools ever. We are building a great component, but having a non open-source runtime may slow down its adoption. This last barrier is now gone.

Have some questions?

I'm sure you have tons of them. Please use the [dedicated Eclipse forum.](https://www.eclipse.dev/forums/index.php?t=thread&frm_id=202)

Want to know more?

![EclipseCon Boston]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/logo.png)

I'll be at EclipseCon Boston next week. [At 1:30 pm On Tuesday](https://www.eclipsecon.org/2013/sessions/your-custom-modeling-environment-definition-made-easy-last).

I'll present the project with Stephane Bonnet from Thales in the session:

"Your custom modeling environment definition made easy. At last!"

During this session you'll learn about the project, its goals, its current deployments and you'll see it in action with live demos.

I will also introduce the project during the [Modeling Symposium](https://www.eclipsecon.org/2013/sessions/modelling-symposium) later the same day!

Sirius brings you the ability to quickly define your dedicated editors: diagram, tree, tables; it would be a shame not to show you what you can do with it:

[![Entities]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s640_entities.jpg)]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s1600_entities.jpg)

[![ISO 26262]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s640_safety-iso26262.png)]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s1600_safety-iso26262.png)

[![Flow topography]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s400_flow-topography.jpg)]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s1600_flow-topography.jpg)

[![Sequence]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s320_sequence-global.png)]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s1600_sequence-global.png) [![MARTE]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s320_marte-multi_view_points.png)]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s1600_marte-multi_view_points.png)

[![Requirements cross-table]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s640_SysML_RequirementsCrossTable.png)]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s1600_SysML_RequirementsCrossTable.png)

![Custom styles]({{ site.url }}/images/blog/2013/introducing-eclipse-sirius/s400_od6_feat_customstyles.png)
