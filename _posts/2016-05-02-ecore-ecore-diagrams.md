---
layout: post
title: Ecore.ecore using EcoreTools
categories: [eclipse]
tags: [ecore, eclipse, ecoretools]
draft: true
---

A few weeks ago I ended up on the following thread on the [EMF Forum](https://www.eclipse.org/forums/index.php/f/108/) asking for [Ecore meta-model formal documentation?](https://www.eclipse.org/forums/index.php/t/1076719/).
Ed pointed at [some documentation](http://download.eclipse.org/modeling/emf/emf/javadoc/2.11/org/eclipse/emf/ecore/package-summary.html) which includes diagrams done with great care but done with tools from another era.

<figure>
    <a href="{{ site.url }}/images/blog/EObjectOperations-old.gif"><img src="{{ site.url }}/images/blog/EObjectOperations-old.gif"></a>    
    <figcaption></figcaption>
</figure>

As the maintainer of EcoreTools I had to do something about it, and so I did.

## EObject

<figure>
    <a href="{{ site.url }}/images/blog/eobject.jpg"><img src="{{ site.url }}/images/blog/eobject.jpg"></a>    
    <figcaption>All participants in the Ecore Modeling Framework implement the EObject's interface</figcaption>
</figure>

Tadaa!

The following diagrams have been created thanks to [EcoreTools](www.eclipse.org/ecoretools) which is part of the [Eclipse Modeling Package](https://www.eclipse.org/downloads/packages/).
All the hard work has been done earlier by Ed when he had to decide what to display and how, all I did is reproduce those using EcoreTools.

## Ecore Components 

<figure>
    <a href="{{ site.url }}/images/blog/ecore-components.jpg"><img src="{{ site.url }}/images/blog/ecore-components-small.jpg"></a>    
    <figcaption>The Ecore components are related according to this hierarchy</figcaption>
</figure>

<figure>
    <a href="{{ site.url }}/images/blog/ecore-components-constraints.jpg"><img src="{{ site.url }}/images/blog/ecore-components-constraints-small.jpg"></a>    
    <figcaption>The hiearchy + the specific constraints</figcaption>
</figure>

<figure>
    <a href="{{ site.url }}/images/blog/ecore-components-detail.jpg"><img src="{{ site.url }}/images/blog/ecore-components-detail-small.jpg"></a>    
    <figcaption>The Ecore Components have the following relations, attributes, and operations</figcaption>
</figure>




## Java Language Types

<figure>   
    <a href="{{ site.url }}/images/blog/java-language-types.jpg"><img src="{{ site.url }}/images/blog/java-language-types-small.jpg"></a>    
    <figcaption>Ecore defines the data types for the following Java language types</figcaption>
</figure>

## External Types

<figure>   
    <a href="{{ site.url }}/images/blog/external-types.jpg"><img src="{{ site.url }}/images/blog/external-types-small.jpg"></a>    
    <figcaption>Ecore defines following additional data types</figcaption>
</figure>


## Generics

<figure>   
    <a href="{{ site.url }}/images/blog/generics.jpg"><img src="{{ site.url }}/images/blog/generics-small.jpg"></a>    
    <figcaption>Ecore supports generics as follows</figcaption>
</figure>








