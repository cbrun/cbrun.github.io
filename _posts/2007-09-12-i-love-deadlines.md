---
layout: post
title: '" I love deadlines...'
date: '2007-09-12T03:02:00.000-07:00'
tags:
- compare
- acceleo
- modeling
categories: [modeling]
modified_time: '2009-05-07T08:23:27.044-07:00'
thumbnail: https://cedric.brun.io/images/blog/2007/gmfgraph-current-and-129-t.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-6103436277211914396
blogger_orig_url: https://model-driven-blogging.blogspot.com/2007/09/i-love-deadlines.html
---

… I like the whooshing sound they make as they go by.” _D. Adams_

Here it comes, the first release of the EMF Compare component! You can download it on the [website](https://www.eclipse.dev/modeling/emft/downloads/?project=compare) and use it for your every-day work. If it doesn’t fit, [report a bug](https://bugs.eclipse.org/bugs/enter_bug.cgi?product=EMFT); work keeps going in the maintenance branch and in the CVS head.

So, what will I get with this piece of software:

- **Model comparison and merge**: compare any EMF model, serialized in files or not, coming from XSD or a twisted metamodel.
- **ID (XMI or Ecore) support**: if your model provides IDs, they will be used in the comparison process.
- **SCM management**: thanks to the Eclipse compare framework you will be able to compare versions of models in CVS or SVN repositories.
- **Sexy user interface**: we said at EclipseCon we would not focus our work on the user interface, but thanks to Laurent’s work the result has outperformed our expectations.
- **“EMF only” dependent core**: the core, responsible for comparison and merge, only depends on EMF and as such is easily re-usable.
- **Extensible framework**: if you have a shiny new idea about model comparison, or on your specific kind of model you can set up a strategy to match two elements, then you can define your own engine and EMF Compare will use it.
- **Export diff**: save your diff in a file (emfdiff) and re-open it later without computation.

So what, let’s have a look now:

![EMF Compare on GMF Graph]({{ site.url }}/images/blog/2007/gmfgraph-current-and-129.png)

**Where is the doc?**
The bundle only provides reference doc right now. In order to get up-to-date FAQ, tutorials or a design overview, stay tuned on the [wiki](https://wiki.eclipse.org/EMF_Compare).

**What’s next?**
Next release (0.8.0) will provide 3-way comparison, diff extensions and many other nice stuffs. Concerning the algorithms we are trying to get better results with generic comparison through methods coming from the research world. An initiative ([website](https://www.model-transformation.org/)) about model transformation/weaving and comparison is taking place in Europe and you may expect that the EMF Compare implementation will evolve toward these works.

We will also take part in the Ganymede simultaneous release to help in providing a coordinated modeling distribution.

I’ll give a [talk at ESE](https://eclipsesummit.org/summiteurope2007/index.php?page=detail/&id=24) about all these nice stuffs and the potential use of this component in other Eclipse tools. It will be a great place for exchanges — if you’re interested, do not hesitate.

