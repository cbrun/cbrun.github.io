---
layout: post
title: Ecore.ecore using EcoreTools
categories: [eclipse]
tags: [ecore, eclipse, ecoretools]
---

A few weeks ago I ended up on the following thread on the [EMF Forum](https://www.eclipse.dev/forums/index.php/f/108/) asking for [Ecore meta-model formal documentation?](https://www.eclipse.dev/forums/index.php/t/1076719/).
Ed pointed at [some documentation](https://download.eclipse.org/modeling/emf/emf/javadoc/2.11/org/eclipse/emf/ecore/package-summary.html) which includes diagrams done with great care but done with tools from another era.

<figure>
    <a href="{{ site.url }}/images/blog/EObjectOperations-old.gif"><img src="{{ site.url }}/images/blog/EObjectOperations-old.gif"></a>    
    <figcaption></figcaption>
</figure>

As the maintainer of EcoreTools I had to do something about it, and so I did:

<figure>
    <a href="{{ site.url }}/images/blog/eobject.jpg"><img src="{{ site.url }}/images/blog/eobject-small.jpg"></a>    
    <figcaption>All participants in the Ecore Modeling Framework implement the EObject's interface</figcaption>
</figure>

Tadaa!

The following diagrams have been created thanks to [EcoreTools](https://www.eclipse.dev/ecoretools) which is part of the [Eclipse Modeling Package](https://www.eclipse.dev/downloads/packages/).
All the hard work has been done earlier by Ed when he had to decide what to display and how, all I did is reproduce those using EcoreTools and exporting those at a fairly high resolution (click on the images to get the full resolution). 

*The corresponding patchset for EMF is [here](https://git.eclipse.org/r/#/c/71892/).*

But beside this anecdotic action there is something interesting and more general in how these diagrams are presenting the Ecore.ecore model.

## Ecore Components 

Ed starts by diagramming the type hierarchy, without any other information (attributes or references). And at least in the case of Ecore but in am sure it is true in the general sense, this gives a very 
good introduction to a domain model: only starting with the types it defines.

<figure>
    <a href="{{ site.url }}/images/blog/ecore-components.jpg"><img src="{{ site.url }}/images/blog/ecore-components-small.jpg"></a>    
    <figcaption>The Ecore components are related according to this hierarchy</figcaption>
</figure>

To construct such a diagram using EcoreTools import all the EClasses in it and then enable the following filters:

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-filters.png"><img src="{{ site.url }}/images/blog/ecore-ecore-filters.png"></a>    
    <figcaption>Filters in EcoreTool</figcaption>
</figure>

You can also enable the *Constraints* layer which gives a bit more information about what makes those types valid.

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-layers.png"><img src="{{ site.url }}/images/blog/ecore-ecore-layers.png"></a>    
    <figcaption>Layers in EcoreTool</figcaption>
</figure>


<figure>
    <a href="{{ site.url }}/images/blog/ecore-components-constraints.jpg"><img src="{{ site.url }}/images/blog/ecore-components-constraints-small.jpg"></a>    
    <figcaption>The hiearchy + the specific constraints</figcaption>
</figure>


Here is a general diagram highlighting the references and attributes. It might look a bit crowded at first but it is filled with information. You can get and understand how all of the primary aspects of Ecore are working just using this diagram.

<figure>
    <a href="{{ site.url }}/images/blog/ecore-components-detail.jpg"><img src="{{ site.url }}/images/blog/ecore-components-detail-small.jpg"></a>    
    <figcaption>The Ecore Components have the following relations, attributes, and operations</figcaption>
</figure>

for this kind of diagrams you really want to know a few keyboard shortcuts, among others:

| ... | ... | ... |
|Hide element| ![](https://raw.githubusercontent.com/mbats/sirius-blog/master/keyboard/blog/images/computer_key_Ctrl_T.png) + ![](https://raw.githubusercontent.com/mbats/sirius-blog/master/keyboard/blog/images/computer_key_H_T.png) | [->doc](https://www.eclipse.dev/sirius/doc/user/diagrams/Diagrams.html#Hidingelements) |
|Hide label | ![](https://raw.githubusercontent.com/mbats/sirius-blog/master/keyboard/blog/images/computer_key_Ctrl_T.png) +  ![](https://raw.githubusercontent.com/mbats/sirius-blog/master/keyboard/blog/images/computer_key_L_T.png)| [->doc](https://www.eclipse.dev/sirius/doc/user/diagrams/Diagrams.html#Hidinglabels) |
|Remove Bendpoints | ![](https://github.com/mbats/sirius-blog/blob/master/keyboard/blog/images/computer_key_Ctrl_T.png?raw=true) + ![](https://github.com/mbats/sirius-blog/blob/master/keyboard/blog/images/computer_key_Shift_T.png?raw=true) + ![](https://github.com/mbats/sirius-blog/blob/master/keyboard/blog/images/computer_key_Minus_T.png?raw=true)  | [->doc](https://www.eclipse.dev/sirius/doc/user/diagrams/Diagrams.html#Manageedges) |
| ... | ... | ... |

You'll find all the keyboard shortcuts in [Mélanie's excellent blog post](https://melb.enix.org/sirius/keyboard-shortcuts/).


## Generics

The next diagram focuses on how **Generics** are modeled in Ecore and does a fairly good job in describing it by hidding all the other aspects. 

<figure>   
    <a href="{{ site.url }}/images/blog/generics.jpg"><img src="{{ site.url }}/images/blog/generics-small.jpg"></a>    
    <figcaption>Ecore supports generics as follows</figcaption>
</figure>

More important: this was not displayed **at all** in the previous diagram and that is a good thing as one don't need to understand this specific point to leverage Ecore.


## Java Language Types

The last diagrams are enumerating datatypes. 

<figure>   
    <a href="{{ site.url }}/images/blog/java-language-types.jpg"><img src="{{ site.url }}/images/blog/java-language-types-small.jpg"></a>    
    <figcaption>Ecore defines the data types for the following Java language types</figcaption>
</figure>

For these kind of diagrams with many un-connected shapes your best friends are the **Make same size**, **Distribute** and **Align** actions.

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-samesize.png"><img src="{{ site.url }}/images/blog/ecore-ecore-samesize.png"></a>    
    <figcaption>Make same size</figcaption>
</figure>

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-align.png"><img src="{{ site.url }}/images/blog/ecore-ecore-align.png"></a>    
    <figcaption>Align</figcaption>
</figure>

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-distribute.png"><img src="{{ site.url }}/images/blog/ecore-ecore-distribute.png"></a>    
    <figcaption>Distribute</figcaption>
</figure>

## External Types

<figure>   
    <a href="{{ site.url }}/images/blog/external-types.jpg"><img src="{{ site.url }}/images/blog/external-types-small.jpg"></a>    
    <figcaption>Ecore defines following additional data types</figcaption>
</figure>


So now, who wants a nice poster in the office ?









