---
layout: post
title: 'Engineering dictator strikes back : querying your team repository'
date: '2009-02-17T08:44:00.000-08:00'
tags:
- modeling kata
- eclipse
- acceleo
- software engineering
categories: [obeo]
modified_time: '2009-05-07T08:07:35.197-07:00'
thumbnail: https://4.bp.blogspot.com/_u5tMWln_Ie8/SZr29ji1-FI/AAAAAAAAAF4/qzOj-W9IvE8/s72-c/teammodel..png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-8666280745850019187
blogger_orig_url: https://model-driven-blogging.blogspot.com/2009/02/engineering-dictator-strikes-back.html
---

This post inaugurates a series of **modeling kata**. Modeling kata are about basic usage of Eclipse Modeling and related technologies to create fun stuff, and more importantly doing it again and again using different ways and analyzing the pros and cons of each solution. Of course the "kata" terminology [is not from me.](https://pragdave.pragprog.com/)

Let's introduce the problem:

Taking my role of "<strike>Non</strike> Benevolent Dictator for Life" [at work](https://www.obeosoft.com/fr/) seriously, I like to keep an eye on the source code history of our products; on the mass of changes and on the places where the changes are made.

That was the idea behind the teamlog2rss.py script I wrote last year. But now, going a bit further in the "big brother" concepts, I hacked a small EMF model to retrieve the logs from the team repository and to generate reports; I'm then able to analyze the log messages and file URIs :)

The model is straightforward, here is a quick extract of the result:

[![]({{ site.url }}/images/blog/2009/engineering-dictator-strikes-back/s400_teammodel..png)](https://4.bp.blogspot.com/_u5tMWln_Ie8/SZr29ji1-FI/AAAAAAAAAF4/qzOj-W9IvE8/s1600-h/teammodel..png)

The model implementation is querying [Subversive](https://www.eclipse.dev/subversive/) to retrieve the logs through a "derived reference". That solution is quite crappy as accessing the model means going through the network (meaning — that's slow), but the advantage is: my EMF model is a plain old EMF model, and as such any tool will work with it.

Then I'm producing reports using [Acceleo](https://www.acceleo.org/pages/accueil/). For each week and committer, I'm checking:

- how many changes have been made
- how many unique files have been changed
- how many tests have been changed
- how many "happy checkstyle" commits were done
- commit activity concerning "bugfixing"
- how many "happy boyscout" commits were done

Here is an extract of the M2T template:

[![]({{ site.url }}/images/blog/2009/engineering-dictator-strikes-back/s400_teamtemplate.png)](https://1.bp.blogspot.com/_u5tMWln_Ie8/SZr24t1WZfI/AAAAAAAAAFw/VXXtkzusc8U/s1600-h/teamtemplate.png)

I'm then able to generate HTML, and even generate a small URI for Google charts to get nice pictures:

[![]({{ site.url }}/images/blog/2009/engineering-dictator-strikes-back/chart)]({{ site.url }}/images/blog/2009/engineering-dictator-strikes-back/chart)

I'm even able to add the committers picture in the "weekly hall of fame" through user code tags in the HTML :)

That said, M2T transformation is not the best pick for such a need. I really need to deduce new information from the original team log data to produce, afterwards, a nice report. Next try on this kata will probably involve M2M transformation to deduce the information, or BIRT reporting... But I don't want to spoil you, _stay tuned ;)_

