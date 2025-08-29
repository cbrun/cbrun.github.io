---
layout: post
title: "Comparing pom.xml files while waiting for indigo"
date: '2011-06-21T07:01:00.000-07:00'
categories: [eclipse]
tags:
  - eclipse
  - compare
  - maven
modified_time: '2011-06-21T07:52:46.945-07:00'
thumbnail: https://4.bp.blogspot.com/-wScqYBvFleE/TgCr2lpHzzI/AAAAAAAAAf8/izHt7q-rq1A/s72-c/pomxsd.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-8579311473137419148
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/06/comparing-pomxml-files-while-waiting.html
---

I know you're all waiting for the **Indigo** release final bits! These 0 and 1 are finding their way on the mirrors as I'm writing to make sure we'll get the smoothest release ever ;)

So, you end up waiting... In the meantime, I'm going to show you a nice piece of technology which is not going to be a new feature in Indigo — as it's been around a few years already ;)

Maybe you had a look at Maven/Tycho; it definitely gained momentum this year. It's completely based on these pom.xml files. I used them a few times already and even with the [Minerva](https://wiki.eclipse.org/Minerva) project (which helps a lot) I'm already in a love/hate relationship with those files.

"When the wise man points at the model, the idiot looks at the XML"

Hopefully Maven provides an XSD here: https://maven.apache.org/maven-v4_0_0.xsd which you can use to initiate an EMF model:

![pom XSD]({{ site.url }}/images/blog/2011/comparing-pomxml-files-while-waiting/s400_pomxsd.png)

Starting from an XSD is never as cool as starting from Ecore, but at least the EMF project can provide you an automatic mapping. And here is the mapped Ecore:

![pom diag]({{ site.url }}/images/blog/2011/comparing-pomxml-files-while-waiting/s400_pomdiag.png)

![pom ecore]({{ site.url }}/images/blog/2011/comparing-pomxml-files-while-waiting/s400_pomecore.png)

If you want a cleaner model you can tweak the mapping.

Using the genmodel you'll get the corresponding Java code. From now EMF is now able to load and save pom.xml files transparently and you can work with them using the Java API or the EMF reflective API.

What for? To leverage all the great components around here; for instance, EMF **compare** is then able to use this and compare the model and not the XML serialization.

[![pom comparison]({{ site.url }}/images/blog/2011/comparing-pomxml-files-while-waiting/s400_pomcomparison.png)]({{ site.url }}/images/blog/2011/comparing-pomxml-files-while-waiting/pomcomparison.png)

Ok, it probably took you less than five minutes to read this. If you're not a Friend of Eclipse you still have to wait for the release. As a sidenote, it did not take me more than 5 minutes to prepare it ;)

If you did not check out EMF&co, you should really have a look!

