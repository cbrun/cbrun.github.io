---
layout: post
title:  EclipseCon Europe 2015 and Sirius 3.1
categories: [eclipse]
draft: true
---

EclipseCon Europe 2015 is over now. This conference is the one in which the "Eclipse Family" feeling is the most inescapable. The downside of this is that one might experience a slight melancholy when the conference is over.

This [tweet](https://twitter.com/alex_schl/status/662556186986864640) from Alexandra reflects quite well the mood

<blockquote class="twitter-tweet" lang="fr"><p lang="en" dir="ltr">Where are all the people? :-( <a href="https://twitter.com/eclipsecon">@eclipsecon</a> I&#39;m having awesomeness withdrawal symptoms already...</p>&mdash; Alex Schladebeck (@alex_schl) <a href="https://twitter.com/alex_schl/status/662556186986864640">6 Novembre 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

This was a busy and exhausting week -- especially for those like me who just landed on the old continent from the bay area --  but on the other hand it was **fabulously energizing !**

<figure>
    <a href="{{ site.url }}/images/blog/ludwigsburg.jpg"><img src="{{ site.url }}/images/blog/ludwigsburg.jpg"></a>    
    <figcaption>Welcome to Germany !</figcaption>
</figure>

Right before the conference Pierre-Charles [announced](https://dev.eclipse.org/mhonarc/lists/sirius-dev/msg00132.html) the general availability of Sirius 3.1 ([new noteworthy](https://www.eclipse.org/sirius/whatsnew3-1.html), [release notes](https://www.eclipse.org/sirius/doc/Release_Notes.html) ). 

This version brings pleasants improvements to empower you in building **state of the art** modeling tools, among other things :  vertical and horizontal compartments, new graphic capabilities for ports... This version also mark the graduation of [AQL](http://cedric.brun.io/eclipse/introducing-aql/) as the recommended query langage for your `.odesign` files. 

Because of all those changes we landed in this beautiful part of Germany with many topics to discuss and were ready for the wave of questions. Most of them should be anwered by [Maxime's presentation: Sirius 3.1 - Stronger, Faster and Smarter Diagram Editors](http://mporhel.github.io/slides/2015_EclipseConEU_Sirius31_StrongerFasterSmarter/#/) if you could not make it to the conference.

<figure>
    <a href="https://farm1.staticflickr.com/690/22761525601_1864b66937.jpg"><img src="https://farm1.staticflickr.com/690/22761525601_1864b66937.jpg"></a>    
    <figcaption>Obeo Team at ECE 2015</figcaption>
</figure>

Of course many interesting discussions ensued but the energizing factor was : our users are enthusiastic, eager and passionate ! I can't stress enough how this feels; in the day-to-day development we are so much focused on the things *which are not quite right* or on this *use case which we should support better* that we tend to forget about all the other things which are making Sirius amazing. Conferences such as EclipseCon Europe are occasions for your users to charge you up.

Another remarkable thing for us was the breadth of tools we got to see from your users: different domains,different goals, different methodologies, but always the same will to build a beautiful and usable product. That's what we want to support, that's where we are going.

<figure>
    <a href="{{ site.url }}/images/blog/etienne-pres-sirius.jpg"><img src="{{ site.url }}/images/blog/etienne-pres-sirius.jpg"></a>    
    <figcaption>Etienne Presenting : A graphic model is worth a thousand words</figcaption>
</figure>

Etienne presented talk giving a pretty good overview of what Sirius can do and how it is being used, you should probably start by having a look at the presentation [on youtube](https://www.youtube.com/watch?v=Rhd3MZ6DQ3g&list=PLy7t4z5SYNaR0yp9EQ9txQhO-JgCLJAga&index=79) if you are still wondering about what Sirius does.

<figure>
    <a href="{{ site.url }}/images/blog/breathlife.png"><img src="{{ site.url }}/images/blog/breathlife.png"></a>    
    <figcaption>Breathe life into your Designer!</figcaption>
</figure>

And because we all love blinking LED's, Melanie presented a session describing how to animate your models with Sirius and the [Gemoc technologies !](http://gemoc.org/). See the [slides here](http://fr.slideshare.net/melbats/eclipsecon-eu-2015-breathe-life-into-your-designer) for more information.

---------------------------------------

A trend started with the last few EclipseCon : talks speaking about Sirius which are not from Obeo. At ECE 2015 two talks were especially noteworthy in this regard as they were tackling fairly detailed and specific areas.

First, a lightning talk by Max Bureck : [A Sirius editor to define Sirius editors](https://www.eclipsecon.org/europe2015/session/sirius-editor-define-sirius-editors). 

He actually designed an `.odesign` to design `.odesigns` with instant graphical feedback.

<figure>
    <a href="https://pbs.twimg.com/media/CN9yy2nWwAAlxIQ.png:large"><img src="https://pbs.twimg.com/media/CN9yy2nWwAAlxIQ.png:large"></a>    
    <figcaption>EcoreTool's odesign</figcaption>
</figure>

The presentation style was quite fun, as it can only be for such a 'meta' project. I can only recommend you check it out as it's been captured and published [on youtube](https://www.youtube.com/watch?v=JAoJRfM4uVs&list=PLy7t4z5SYNaR0yp9EQ9txQhO-JgCLJAga&index=32).

<figure>
    <a href="{{ site.url }}/images/blog/incquery.png"><img src="{{ site.url }}/images/blog/incquery.png"></a>    
    <figcaption>IncQuery gets Sirius!</figcaption>
</figure>

Another talk, another subject : [IncQuery gets Sirius: faster and better diagrams](https://www.eclipsecon.org/europe2015/session/incquery-gets-sirius-faster-and-better-diagrams) where Akos Horvath from IncQuery Labs explored how Sirius could integrate with IncQuery to achieve a complete incrementality. As you may -- or may not -- be aware, Sirius is projectional and offers you a lot of flexibility in how you want your model elements to be projected in a diagram view. The downside of this flexibility is Sirius can't easily decide if there is a new node to create, to update, or to delete based on what has changed on the model. The only way to know for sure that something needs to be updated is to refresh it and see if it has changed in the process. That's why we work quite a lot on making sure this process is as fast as possible but IncQuery can helps when this "as fast as possible" is "not fast enough". If you are willing to spare some heap memory,  IncQuery can boost your diagram editor! Have a look [on the slides](https://www.eclipsecon.org/europe2015/sites/default/files/slides/iqgetsSirius_eclipsecon_15_ha_final_0.pdf)

---------------------------------------

Looking at the overall conference : 
* the content was really good, amoung the best years (if not the best!). Thank you for submitting such good talks we could choose from !
* we had a lot of fun as a [Program Committee](https://www.eclipsecon.org/europe2015/about-pc), we worked as a team and I'm quite proud of the result
* the Eclipse community *is a family*, just look at how people react when you step in the bar, not even having unpacked your luggage yet, now compare with what happens when you meet family which you barely see each year. That's right. Same spirit.

But that's not it. What will we do with all that energy ? SiriusCon is just around the corner, an international event dedicated to Sirius. It's free, it's in Paris. The program is out already and is packed with content for both beginners and advanced users. A 'clinic' will be held all day long where you'll be able to question the experts and come with your own tooling. 

3rd of December 2015 in **3 weeks**

Did I mention it's **free** ? Well, it is, but it doesn't mean we have infinite rooms so [register now](http://www.siriuscon.org/register.php), **places are limited**!

