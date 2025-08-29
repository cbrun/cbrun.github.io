---
layout: post
title: "Model Comparison : Patching with MPatch"
date: '2010-10-13T05:25:00.000-07:00'
categories: [modeling]
tags:
  - eclipse
  - compare
modified_time: '2010-10-13T05:28:41.528-07:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-8443724993412705362
blogger_orig_url: https://model-driven-blogging.blogspot.com/2010/10/model-comparison-patching-with-mpatch.html
---

The following message is posted on this blog on behalf of Patrick Könemann.

![Delta]({{ site.url }}/images/blog/2010/model-comparison-patching-with-mpatch/delta.png)

Cédric already announced it two weeks ago: **MPatch is integrated into EMF Compare!**

Did you ever want to transfer changes from one model to another?

Or do you frequently perform the same changes on your models?

MPatch is a technology that stores model changes as self-contained artifacts, just like patches, that are also applicable to other models! Let me show an example of how MPatch works:

This is just a simple model, a base version on the left and a modified version on the right. Modeled with the IBM Rational Software Architect, but any kind of EMF model is supported. The changes are highlighted: 3 deleted attributes, 1 updated attribute, 1 new class, 3 new generalizations.

![Model A]({{ site.url }}/images/blog/2010/model-comparison-patching-with-mpatch/modela.png)

EMF Compare is a nice tool for calculating such changes. The result is shown below. All changes are nicely highlighted in the treeviews and one can browse through them. This is where **MPatch** comes into play: the export menu lists a new option!

![EMF Compare]({{ site.url }}/images/blog/2010/model-comparison-patching-with-mpatch/emfcompare.png)

An export wizard is started that guides the user through the **MPatch** creation task. In the end, the changes are stored in a file, `extract_id.mpatch` for example. This file can now be applied to other models, even if **their contents differ**!

![Apply]({{ site.url }}/images/blog/2010/model-comparison-patching-with-mpatch/apply.png)

The model below is a different one — again we want to extract the id attribute into a common superclass. However, the attributes, the classes, and even the number of attributes and classes differ!

![Model B]({{ site.url }}/images/blog/2010/model-comparison-patching-with-mpatch/modelb.png)

Let's see how **MPatch** handles the situation. Selecting _Apply MPatch_ triggers a wizard with the same name. The crucial part is the so-called _resolution of symbolic references_ — they are responsible for selecting the proper model elements of your target model. Let's have a closer look:

![Resolve]({{ site.url }}/images/blog/2010/model-comparison-patching-with-mpatch/resolve.png)

- The first change is not applicable because there is no attribute called _Title_ — ignore this!
- The second change is applicable because a similarly named package (_data_ vs. _customerdata_) is found — ok.
- The third change is applicable because I manually selected _Contract_ and _Invoice_ — ok.
- The fourth change is applicable because similarly named attributes (_id_ vs. _inv_id / con_id_) are found — ok.

Following the wizard to its end updates the given model and this is the result:

![Applied]({{ site.url }}/images/blog/2010/model-comparison-patching-with-mpatch/applied.png)

To wrap up, an **Mpatch** is not only a self-contained patch for models, it is even able to make the changes applicable to different models!

Installation instructions and a lot more information on the project website: https://modeldiff.imm.dtu.dk/.

