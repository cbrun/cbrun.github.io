---
layout: post
title: "Model Transformation Preview"
date: '2011-10-18T08:37:00.000-07:00'
categories: [modeling]
tags:
  - uml
  - eclipse
  - compare
  - transformation
  - preview
modified_time: '2011-10-18T08:47:56.157-07:00'
thumbnail: https://4.bp.blogspot.com/-y0egF8rjm6Y/Tp2YUkJLHFI/AAAAAAAAAn4/U-tzStIFPJY/s72-c/compare-transfo-uml.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-6296517877997441289
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/10/model-transformation-preview.html
draft: true
---

Let's say you have a model-to-model transformation, and you want to provide the ability for the end-user to see and control what is going to be applied on the target model. How could you do that? EMF Compare might do the trick.

Here is a trivial transformation example: renaming all Classes which are abstract by adding a prefix to their name. The orchestrator loads the original models, applies the transformation, and then opens a comparison preview between the current serialized state ("now") and the transformed state ("future").

The preview is shown using EMF Compare by computing the match/diff, forging a compare editor input, and opening it:

[![Transformation compare]({{ site.url }}/images/blog/2011/model-transformation-preview/s640_compare-transfo-uml.png)]({{ site.url }}/images/blog/2011/model-transformation-preview/s1600_compare-transfo-uml.png)

Now, if you want to allow the end user to customize the output model and detect conflicts between transformation changes and their customizations, move to a three-way comparison by adding an untouched "ancestor" version. Use it as the common ancestor in EMF Compare, and conflicts will be highlighted:

[![Conflict compare]({{ site.url }}/images/blog/2011/model-transformation-preview/s640_compare-transfo-uml-conflict.png)]({{ site.url }}/images/blog/2011/model-transformation-preview/s1600_compare-transfo-uml-conflict.png)

It's a simple example of what you can achieve using EMF Compare and how you can reuse it in your tooling.

