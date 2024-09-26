---
layout: post
title: "How much time do I need to make coffee ?"
categories:
  - modeling
tags:
  - modeling
  - eclipse
  - sirius
  - opensource  
translation_fr: /modeling/guesstimate-modelisation-probabilite/
---

As you might be enjoying your summer and browsing around here, let me show you a little prototype I’ve been developing on and off through several versions of Sirius Web.

It’s now based on the latest Sirius Web release. Kudos to the Sirius team for releasing every 8 weeks like clockwork!

The idea was inspired by Guesstimate: 
> 𝘈 𝘴𝘱𝘳𝘦𝘢𝘥𝘴𝘩𝘦𝘦𝘵 𝘧𝘰𝘳 𝘵𝘩𝘪𝘯𝘨𝘴 𝘵𝘩𝘢𝘵 𝘢𝘳𝘦𝘯’𝘵 𝘤𝘦𝘳𝘵𝘢𝘪𝘯!" 

It’s a tool I’ve always liked, and I wanted to see how far we could take it with Sirius.

This prototype is a domain-specific tool for "𝘨𝘶𝘦𝘴𝘴𝘵𝘪𝘮𝘢𝘵𝘪𝘯𝘨" using Monte Carlo simulations. It’s just a proof of concept, but it really showcases some cool features of Sirius Web:
 - All the domain-specific logic is kept in an EMF-based metamodel and the corresponding Java implementation. It’s only 11 files and 1028 lines of non-generated code.
 - I’m using the charts widget in the details view, which adds a nice touch.
 - Integration with Java libraries is super easy – here, I’ve used Apache Common Maths and PetitParser.

 Check out the video to see it in action!

<video  width="640" height="360" controls><source src="{{ site.url }}/media/2024-08-08-Guesstimate.mp4">Your browser does not support the video tag.</video>
