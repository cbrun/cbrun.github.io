---
layout: post
title: Eclipse Modeling Summer of Code 2009
date: '2009-03-10T08:46:00.000-07:00'
tags:
- eclipse
- acceleo
- obeo
categories: [eclipse]
modified_time: '2009-05-07T08:06:52.391-07:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-7945694064996685286
blogger_orig_url: https://model-driven-blogging.blogspot.com/2009/03/eclipse-modeling-summer-of-code-2009.html
excerpt: "Google Summer of Code ideas across EMF/Acceleo/Modeling—for students and mentors eager to build practical tooling and 3D diff visualizations this season."
---

<figure>
  <a href="{{ site.url }}/images/blog/2010/soc.png">
    <img src="{{ site.url }}/images/blog/2010/soc.png" alt="Google Summer of Code" />
  </a>
</figure>

Yes, summer is coming fast, and if you're a student interested in software development and engineering, Eclipse is a great place for a **Summer of Code**!

New ideas are still appearing on the [wiki page](https://wiki.eclipse.org/index.php?title=Google_Summer_of_Code_2009_Ideas) and no doubt you'll get many more in a few weeks. Let me highlight some of the cool subjects you might apply for if you're interested in modeling.

Let's speak about [EMF Compare](https://wiki.eclipse.org/EMF_Compare); we tried to focus on **cool stuff** as that's what open source is about.

<figure>
  <a href="{{ site.url }}/images/blog/2009/Java3DFeedbackFigure.jpg">
    <img src="{{ site.url }}/images/blog/2009/Java3DFeedbackFigure.jpg" alt="3D visualization idea" />
  </a>
</figure>

First, the **3D visualization**! Using EMF Compare, the GMF Diagram support and [GEF 3D](https://www.eclipse.dev/proposals/gef3d/), one can imagine a nice "time machine like" visualization of the model differences. One can easily imagine really nice representations using that third dimension; we have to display two (or three) versions of a diagram annotating the diagram elements with graphical hints saying "that's a new element", or "this one has been changed", so 3D can make sense here.

<figure>
  <a href="{{ site.url }}/images/blog/2009/Stub1.png">
    <img src="{{ site.url }}/images/blog/2009/Stub1.png" alt="Huge models comparison" />
  </a>
</figure>

Second: **huge models comparison** — by huge we mean really huge like millions of elements. EMF Compare uses a heuristic-based algorithm to compare two models, while doing so it's keeping processing data in memory (the more important the models are, the more memory is used). The subject is twofold: first design and implement a MatchEngine needing less stuff in memory, then leverage Eclipse technologies like [CDO](https://www.eclipse.dev/modeling/emf/?project=cdo#cdo) or [JCRManagement](https://www.eclipse.dev/modeling/emft/?project=jcrm) in order to break the memory bound! That may seem trivial, but when you need to process a lot of data, [many parameters are changing.](https://scienceblogs.com/goodmath/2008/11/scale_how_large_quantities_of.php)

Third: improving the "**Graphical Compare**" proof of concept initiated by Tobias ([flash demo here](https://literate.modeling.free.fr/modeling/compare/GMFCompareEcoredi.htm)).

Many more ideas are available and look really cool especially in the modeling area, so if you're a student, jump and meet the **Eclipse Community**!
