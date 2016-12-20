---
draft: true
layout: post
title: Graphical Modeling from 2016 to 2017 / Better, Faster, Stronger
categories: [eclipse]
tags: [eclipse, sirius, modeling, emf, acceleo]
---


At Obeo, we believe that modeling is the right way to help IT and industry engineers collaborate efficiently on the design of their smart products. Our innovative approach consists of building specific modeling tools that completely suit users' business domains. Modeling is a means to an end: by using modeling technologies we make sure that such a tool can be defined faster, as well as deployed and maintained better.

To achieve this goal, we develop highly customizable open source software, such as [Eclipse Sirius](http://www.eclipse.org/sirius/){:target="_blank"}. We consider that a modeling tool must be adaptable, flexible, and user-friendly. This year again, we worked hard to focus on that!

![]({{ site.url }}/images/blog/2016-2017/1capture.png)

As you may know, Sirius is the easiest way to get your own modeling tool and to do it rapidly. Indeed, it dramatically reduces the time spent on creating domain-specific modeling workbenches thanks to an interpretation mode that allows very short feedback-loops. In 2016, we invested time in the Eclipse Ecore Tools project to facilitate the definition of modeling languages by providing a very intuitive and powerful Ecore graphical editor.

![]({{ site.url }}/images/blog/2016-2017/2capture.png)

It’s been three years since Sirius was made open source and the community is growing every year. A few weeks ago, part of this community gathered for the second edition of [SiriusCon](http://www.siriuscon.org/){:target="_blank"} in Paris. More than 100 attendees coming from more than 10 different countries participated in this international conference on graphical modeling. If that is not proof that Sirius is a worldwide technology, we don’t know what is!

![]({{ site.url }}/images/blog/2016-2017/3capture.jpg)

At SiriusCon, we had the opportunity to present one of the latest key features of Sirius: [the properties view](http://www.eclipse.org/sirius/whatsnew/whatsnew4-1.html). It turned out that with all the improvements Sirius brings to the specification of the modeling view, the bottleneck was in the definition of the properties view to be linked to each graphical element. The Obeo team addressed that problem.


Now, Sirius provides an integrated way to define properties views in the same way the user is used to defining them in other parts of the designer: no need for coding - it is dynamic and query based. In addition, with [Sirius 4.1](http://www.eclipse.org/sirius/download.html){:target="_blank"}, the user is now able to specify exactly how the properties view should be represented.

<figure>
    <a href="{{ site.url }}/images/blog/2016-2017/4capture.png"><img src="{{ site.url }}/images/blog/2016-2017/4capture.png"></a>    
    <figcaption></figcaption>
</figure>

Sirius 4.1 has default rules based on the type of the elements defined in the metamodel. For example, if the user has defined a string attribute in his metamodel, it will be automatically represented by a text widget; a boolean will be represented by a checkbox, and so on. If the default properties view does not fit the user's needs, no problem: it can be customized.

<figure>
    <a href="{{ site.url }}/images/blog/2016-2017/5capture.png"><img src="{{ site.url }}/images/blog/2016-2017/5capture.png"></a>    
    <figcaption></figcaption>
</figure>

In 2017, we want to go further building on the same fundamentals. We will focus on technologies that are **real-world ready, adaptable, and give instant feedback**.

We’ve been working on the codebase for months already, but next year will see a nice scalability offspring: a core runtime that can scale any number of diagrams or their size while keeping everything consistent like it currently does today. And that’s only under the hood, in a more visible way we’ll hunt for every break a user might encounter in the workflow of using a modeling tool. Here is an example when the user ends up trying to set up diagrams and models while not being the modeling perspective:

<figure>
    <a href="{{ site.url }}/images/blog/2016-2017/6capture.png"><img src="{{ site.url }}/images/blog/2016-2017/6capture.png"></a>    
    <figcaption></figcaption>
</figure>

The model content or diagrams are not visible in the package explorer yet, the Eclipse IDE doesn't have an editor for `.aird` files, and double clicking it will not help. We plan to address this next year by providing a default editor for `.aird` files.


This editor gives us a whole new dimension to present your tooling features and is the starting point to a project that will grow during the next few years: making the tooling aware of the process to achieve better usability.

Hear me well, the word “aware” is picked with care and “process driven” is banned in this context. In the end the user gets to decide and the tool should never get in the way, but by making the tool aware of the process or methodology we can make it more helpful. This will first be translated by the integration of the Activity Explorer which got contributed to Amalgam by Thales last year. This allows anyone to define the process activities without writing a single line of code, in the very same way you can currently define diagrams, tables or the properties view, right into the `.odesign` file.

<figure>
    <a href="{{ site.url }}/images/blog/2016-2017/7capture.png"><img src="{{ site.url }}/images/blog/2016-2017/7capture.png"></a>    
    <figcaption></figcaption>
</figure>

Other improvements especially focused on the diagrams are in the works. Here is a mockup of a new mechanism to enrich existing diagram editors, you can think of it as “decorators on steroids”. Follow this [bug](https://bugs.eclipse.org/bugs/show_bug.cgi?id=506259){:target="_blank"} if you are interested.

![]({{ site.url }}/images/blog/2016-2017/8capture.png)

We are in a continuous evolution. We strive to continually improve the user experience and to streamline the complete model environment building process. This means that we have our hands in many Eclipse projects, from Ecore Tools, EMF Compare, Acceleo, Amalgam, EEF to Sirius and improve each of those. We are building various technologies independently while making sure they integrate seamlessly in the final product.

<figure>
    <a href="{{ site.url }}/images/blog/2016-2017/9capture.png"><img src="{{ site.url }}/images/blog/2016-2017/9capture.png"></a>    
    <figcaption></figcaption>
</figure>

[Capella](https://polarsys.org/capella/){:target="_blank"}, one of the solutions provided by Eclipse PolarSys Working Group, is one example of a product aggregating such technologies. It is already a field-proven Model-Based Systems Engineering (MBSE) workbench.

Capella was developed by Thales to help engineers formalize system specifications and master their architectural design. It is sustainable and adaptable and has already been successfully deployed in a wide variety of industrial contexts (aerospace, communication, transportation, etc.). This is a modeling environment focused on a domain tooling a methodology, based on many of the technologies mentioned before. It is 100% open source. [Check out what can be done with it!](https://polarsys.org/capella/){:target="_blank"}

Is modeling in 2017 going better, faster, stronger? Challenge accepted! The Obeo team is up to the task! We will do our possible to reach a new level and deliver cutting edge modeling tools.

To achieve anything we need the support of our enthusiastic community. We know that in 2017 we will be able to rely on the Eclipse users as we have always done. We want to get closer to the users and receive fine-grained feedback to improve our technologies even more. We are currently working on a new online (and IRL!) way to deal with that… but you will have to stay tuned to get more information. Keep your eyes peeled for the upcoming [SiriusCon](http://www.siriuscon.org/){:target="_blank"}, it’s the best place to interact with us!