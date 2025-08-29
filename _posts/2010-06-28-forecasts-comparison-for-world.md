---
layout: post
title: "Forecasts Comparison For The World !"
date: '2010-06-28T01:04:00.000-07:00'
categories: [modeling]
tags:
  - eclipse
  - compare
  - acceleo
  - obeo
modified_time: '2010-06-28T02:23:12.676-07:00'
thumbnail: https://2.bp.blogspot.com/_u5tMWln_Ie8/TCha9tHZZXI/AAAAAAAAAUQ/ZYmMQtmLQRI/s72-c/compare_menu.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-5597262855966298773
blogger_orig_url: https://model-driven-blogging.blogspot.com/2010/06/forecasts-comparison-for-world.html
---

I have to admit I know nothing about soccer. Yes I'm a French guy, but I know nothing about soccer. That said I'm not against having a few beers in front of this broadcasted green field and I'm always in when it's about having fun with a small game leveraging Eclipse technologies.

Obviously I played with the EEF-based rich client for the forecasts, and from the moment the [source code has been made available](https://eef-modeling.blogspot.com/2010/06/eclipse-wordlcup-bye-bye-france-hello.html) I started hacking the code.

The forecasts, matchs and results are all kept in a model accessible through an http URI, and as _EMF rule them all, find them, bring them all and in the darkness bind them,_ you can leverage any Eclipse Modeling component to hack something quite easily.

![Compare menu]({{ site.url }}/images/blog/2010/forecasts-comparison-for-world/s400_compare_menu.png)

That's what I did with Compare.

I extended the EMF editor adding a specific action, **"Compare with / Player with Best Rank"**.

This action allows you to compare your own forecasts with the best ones, and then merge your own forecast with the best player's one _(Noooo, that's not cheating!)_

And here is the user interface you get for free*, with a pure semantic comparison:

[![Compared forecast]({{ site.url }}/images/blog/2010/forecasts-comparison-for-world/s400_compared_forecast1.png)]({{ site.url }}/images/blog/2010/forecasts-comparison-for-world/compared_forecast1.png)

_\* you have to depend on EMF Compare though..._

Here is the logic needed to launch the comparison:

<iframe src="https://pastebin.com/embed_iframe.php?i=0wdcF2fm" style="border:none;width:100%;height:400px"></iframe>

I had to use a few tricks: I had to provide a specific match engine enforcing the match of two players, otherwise the Compare component stops matching the forecasts from the beginning as the players are different.

<iframe src="https://pastebin.com/embed_iframe.php?i=Ls4aqfPJ" style="border:none;width:100%;height:600px"></iframe>

That's all for today. If I can free more time for this hack I'll provide a diff extension to change the score delta representation to a more meaningful one — so far it's left as an exercise for the reader ;)
