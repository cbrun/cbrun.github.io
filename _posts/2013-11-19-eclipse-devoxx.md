---
layout: post
title: "Eclipse @Devoxx"
date: '2013-11-19T07:07:00.002-08:00'
categories: [eclipse]
tags:
  - devoxx
  - eclipse
  - obeo
modified_time: '2013-11-19T08:43:28.562-08:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-1933487336794831213
blogger_orig_url: https://model-driven-blogging.blogspot.com/2013/11/eclipse-devoxx.html
---

I'm back from a full week at Devoxx in Antwerpen- Belgium. I was there to present the Sirius project and Eclipse Modeling at the Eclipse Foundation booth. (by the way, thanks again to the foundation staff!) It was quite fun to be there with Jelena Alter, Marcel Bruch, Julien Vermillard and Gael Blondelle; we had a good mix of things: Marcel for the Java developers with Code Recommender, Julien for M2M stuff (which was very hot at Devoxx this year) Jelena and Gael for the Eclipse Foundation itself and me with fancy graphical modelers.

![Booth]({{ site.url }}/images/blog/2013/10851443223_42c39a30b9_o.jpg)

Here are a few random notes:

- The conference organization and setup is quite amazing. Wifi worked very well, the venue is a theater complex which means you always get to sit very comfortably and the screens are just huge. There were some hacking spaces with people hanging there all the time, voting was easy thanks to a bunch of arduino modules installed in each room. Interactions were encouraged with tweets being displayed on every screen in between the sessions, "free to use" whiteboards were positioned in the hallway leading to some wild polls. I liked these small things which are triggering more involvement from the audience.
- The content was good or very good in general but I could not attend many sessions as I had many things going on at the booth too, but overall I was impressed. It's not perfect though; I had my share of "sexy looking talks" which did end up being very badly presented.
- In the end I have seen only a few Java talks; many sessions were related to web dev, cloud, or the now famous "Internet of Things".

I was there as an Eclipse guy and believe me, the Eclipse hoodie is like a secret weapon to get to talk to pretty much any programming rock star. On the other hand there is this trend going on in the Java community about Eclipse being really bad compared to the competition which made me a bit reluctant first: will people attack me there?

After speaking with many Java developers during the conference here is my report: most of them are loving Eclipse, as an IDE.

Juno was a lot of pain though and they did not understand why it got released with such poor performances and behavior. They like Eclipse Kepler way better but it's still not exactly on par with what they used to expect, and they expect a lot from Luna, in particular:

- Performances and responsiveness
- Quality and reliability, no more UI glitches in the workbench.
- Java 8 support.
- Maven integration (Many people have given up on this one starting from Juno...)

In the end the differences between the major IDEs are quite small and we have room for improvements in several points, but users have pain with IntelliJ too.

What about innovative features? Actually Code Recommender in itself impressed many peoples, and the others could quite easily be impressed with features which have been around for years through specific plugins they did not know about.

In a way that was kind of a relief for me to see that our work was not completely rejected by the community and that people could say things like: "Eclipse is the best for this, or that" (for instance having support for multiple languages in the same IDE). Also, several sessions presenting very cool stuff that could not have existed without Eclipse.

<blockquote class="twitter-tweet" lang="fr"><p>The Crazyflie quadcopter is made with oss tools. Eclipse is one of those, kudos to the Eclipse community! <a href="https://twitter.com/search?q=%23devoxx&amp;src=hash">#devoxx</a> now demo time</p>— Cédric Brun (@bruncedric) <a href="https://twitter.com/bruncedric/statuses/400618965191643136">13 Novembre 2013</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

But on the other hand it is very hype to reject and bash Eclipse when you want to brag as a speaker.

Of course it was also a great occasion to try a few ideas discussed here and there lately. I realized that:

- "Code Recommender" in itself makes people wanting to use Eclipse again for Java.
- most of them don't understand what they are downloading from Eclipse.org and the whole idea behind the release train. They could not really figure out which "thing" they should download between "Classic", "Java" or "JEE".
- most did tell me they downloaded "Eclipse" (which means, for instance, the Java package) and were surprised that it was not having the X or Y feature — which actually is part of the release train. They just have no clue how to discover that.
- nobody wanted the "uber package": that would make an un-usable IDE and they don't want features they don't use to interact with others (and the bloat)
- the "let's display fake wizards which are provisioning the IDE on demand" was mildly received. Most people I talked to want to be sure they won't need to install something more once they prepared their setup.
- a "configurator wizard" opening up the first time so that the developers get to pick what kind of language support he wants, which SCM integrations, which bug tracker and so on, kinda excited the crowd. They see that as the perfect way to provision just the Eclipse they want without needing to figure out what all these weird feature names are meaning and knowing this is a selection of high quality plugins, all of them being open-source.
- only a few would be willing to pay for Eclipse, even if it is a special version, and even if it's a very low price. They are used to Eclipse being free and are more willing to click donate than to buy the binary. By the way, they feel like when they click on this donate button, they are already helping the development of Eclipse as an IDE.
- many features of Eclipse, even if they can be installed through the release train and can be useful for a developer, are not known at all. (the configurator wizard could help here too). This is, again, probably the smallest effort on our side to have the highest impact.
- several were using Eclipse as a platform, to build applications or tools, and they could not find the same level of flexibility and extensibility in any other platform out there.

This is it for "Eclipse as an IDE".

Regarding Sirius, I had very good feedback. People were either curious about it or left with the idea of trying it in their own context, which was more than I could expect from such a conference!

![Sirius demo]({{ site.url }}/images/blog/2013/10851011866_d536c4ce30_o.jpg)
