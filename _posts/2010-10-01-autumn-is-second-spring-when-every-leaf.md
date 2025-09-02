---
layout: post
title: "Autumn is a second spring when every leaf is a flower"
date: '2010-10-01T01:17:00.001-07:00'
categories: [eclipse]
tags:
  - obeo
  - eclipse
  - acceleo
excerpt: "Autumn updates at Obeo: Helios SR shipped, new hires, and a handy Acceleo 3 trick—calling Java services from templates with quick fixes."
modified_time: '2010-10-01T08:09:09.742-07:00'
thumbnail: https://4.bp.blogspot.com/_u5tMWln_Ie8/TKWfZNHYO2I/AAAAAAAAAYQ/ClulJG9gKZo/s72-c/internship-cake.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-6136697458246759714
blogger_orig_url: https://model-driven-blogging.blogspot.com/2010/10/autumn-is-second-spring-when-every-leaf.html
---

Maybe Twitter gives a false impression that you're keeping the users informed of what is going on. False because **140 chars can't be enough!**

Many things are keeping the Obeo guys busy, from the Eclipse and open-source involvement to the incubation of highly innovative products you'll love while still providing the best service to our customers looking for expertise :). Oh, and we provided the first Helios service release for Compare, Acceleo, EEF, ATL and much more — go [get the modeling package](https://www.eclipse.dev/modeling/amalgam/)!

Summer is an internship time in France, and for us every internship's ultimate goal is to hire another great person. I can say we did succeed this year! Expect even more great contributions, user experience polishing and features for Indigo!!

Furthermore the newcomers completely understood the **chocolate-commit** spirit ...

![Internship cake]({{ site.url }}/images/blog/2010/autumn-is-second-spring-when-every-leaf/s320_internship-cake.png)

No doubt you'll hear about those guys at some point — [Stéphane already started to blog](https://sbegaudeau.tumblr.com/)...

Speaking about Indigo, we wrote down a [long term roadmap](https://wiki.eclipse.org/EMF_Compare/Roadmap) for EMF Compare on the wiki — feel free to have a look! Coming soon: more information about the **MPatch contribution recently integrated in EMF Compare.**

Ok, enough teasing, back to code generation. In case you did not notice, Acceleo 3 provides one of the most compelling editing tooling you can get with the Eclipse platform. Using the JDT I often find myself thinking "oh, they did think about this! great!" — you'll often get the same feeling with Acceleo 3...

Let's try with an example: it's often useful to be able to call Java logic directly from a template. If you want to do so, start by writing down this Java logic.

[![Java service]({{ site.url }}/images/blog/2010/autumn-is-second-spring-when-every-leaf/s400_javaservice.png)]({{ site.url }}/images/blog/2010/autumn-is-second-spring-when-every-leaf/s1600_javaservice.png)

Then call it from your template. Obviously it's not going to work as is. Here we're calling the "getJavaCompatibleName" method on an **EClass**, but this method is not existing on this type. Acceleo provides a mechanism to call Java logic associated with a given meta-class: the first parameter of the method has to be of the type of the extended meta-class and Acceleo will automatically transform a _myInstance.myMethod()_ call to a _SomeClass.myMethod(myInstance)_.

If you want to try that, call the quickfix menu on the compilation error with CTRL+1:

[![Quick fix]({{ site.url }}/images/blog/2010/autumn-is-second-spring-when-every-leaf/s400_quickfix.png)]({{ site.url }}/images/blog/2010/autumn-is-second-spring-when-every-leaf/s1600_quickfix.png)

Choosing the `"Create Java Service Wrapper"` quick fix will add a new query to your template:

![Query]({{ site.url }}/images/blog/2010/autumn-is-second-spring-when-every-leaf/s400_query.png)

And you're done!
