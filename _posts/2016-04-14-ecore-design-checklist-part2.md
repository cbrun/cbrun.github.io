---
layout: post
title: Metamodel (Ecore) Design Checklist - part 2
categories: [eclipse]
tags: [draft]
draft: true
---

THIS IS A DRAFT, PLEASE DO NOT SHARE AT THIS STAGE

This article is the second part of a series focusing on Metamodel design (more especially Ecore models). 
Following the [first part focused on some ground rules]() this second part is focused on slightly more technical aspects: scalability and Java. The general disclaimer still applies: 

> Most of the checks stated here are very easy to comply with when considered from the start but might not be that cheap later on. Furthermore this list is not exhaustive, 
> and not necessary the unique and unviversal truth. Your mileage may vary but then [tell me about it!](https://twitter.com/bruncedric)

___

## Scalability 

<img src="{{ site.url }}/images/blog/rainbowdash.png" style="float: left;">

<br>
Your Ecore model design **has** scalability and performances implications, most especially memory and I/O wise but not only. 
If you want to get the most of Eclipse Modeling technologies in general you should check the following items.

<br><br>

### ☑ Instances which will be present a lot in the models have a terse serialization

Ask yourself:  how many instances of this EClass will I have in a nominal model? If the answer is "quite a lot"(100K for instance) then check how will they be serialized and make sure there is not an improvement you could bring here. This is particularly true using the XMI serialization which is not the most space efficient one.

This is also very true for custom datatypes. Once you define this custom datatype EMF requires you to write the ``fromString()`` and ``toString()`` methods for it. If this datatype is being used by a lot of instances then make sure your serialization is terse.

### ☑ Everything which is serialized needs to be serialized

<img src="{{ site.url }}/images/blog/fat_pinkie_pie_by_nice123456-d4xy2w3.png" style="float: right;">

<br>
<br>

You need this model, but are there parts which have no need to be serialized? Can you strip out parts of the information? What information is actually captured by the users versus infered by the tool? Is there any part of this data which has a shorter lifecycle than "load the file"/"save the file"?


### ☑ There is no EClass which could be replaced by an EDatatype

Any EClass used for an important number of instances should be inspected and a conscious decision should be made about whether it is best modeled as an EClass or as an EDatatype. Even with the [EMF Ultra Slim Diet](http://ed-merks.blogspot.fr/2009/01/emf-ultra-slim-diet.html) an EObject comes with an overhead, both in term of memory usage but even more importantly in the overhead framework code might induce (cross-referencers, change recorders..)

Rule of thumb: if you have many instances which will be never referenced by other instance beside the containing one and you don't really need the individual change notifications of each attribute of the EObject, then it's probably best to model it as an EDatatype. An EClass only having EAttributes and not EReferences is also a clear indication that this might be a good candidate for being an EDatatype.

### ☑ The model has some structure

There are two main reasons to stay away from flattened models with tens of thousands of instances in a single reference value:

1. for legacy reasons, EMF will check the uniqueness of any addition and as such in the Java implementation, a call to `.add()` will check for every item in the list. (there are way to explicitely avoid those checks by using `addUnique()`)
2. displaying the reference content in the user interface will likely lead to the creation of tens of thousands of SWT items in a list or in a tree. SWT is not good at that and that might lead to long freezes.

> Sirius is kind enough to detect those situations and group such references, but you can't count on that for every tree viewer.

<figure>
    <a href="{{ site.url }}/images/blog/sirius-grouping.png"><img src="{{ site.url }}/images/blog/sirius-grouping.png"></a>    
    <figcaption>Sirius grouping tree items</figcaption>
</figure>

### ☑ The implementation classes are using MinimalEObjectImpl

Make sure your *.genmodel* is configured to leverage `MinimalEObjectImpl`. This is the default if you created your genmodel with a recent version of EMF, more information about this is available on [Ed's blog](http://ed-merks.blogspot.fr/2009/01/emf-ultra-slim-diet.html)

___


## Java

### ☑ Multiple inheritance is not over-used

<img src="{{ site.url }}/images/blog/mutant-pony.png" style="float: right;">

<br>

Ecore allows for multiple inheritance. But in the end your Ecore model is transformed into Java code and Java only allows multiple interfaces to be implemented. 

The EMF code generator hides that for you and might ends up dupplicating code to make sure everything works as expected. A few things to keep in mind:

* the order of the inheritance matters: the implementation class will extends the implementation class of the **first** EClass in the list of supertypes, the subsequent classes will lead to dupplicated code.
* just like for Object Oriented designs, having a lot of multiple inheritance screams of a design which is not really splitting concerns (or not the right ones)

### ☑ Custom DataType are used in every situation where it makes sense

EMF provides off-the-shelve datatypes for *Strings*, *Integer*, *Float*, *Long* and their primitive counterparts as *EString*, *EInt* ...

<figure>
    <a href="{{ site.url }}/images/blog/datatype1.png"><img src="{{ site.url }}/images/blog/datatype1.png"></a>    
    <figcaption>cutieMark is an open-ended list, designed as a String</figcaption>
</figure>

But *String* is a technical concern and it might make the design more obvious to replace usages of the *EString* by your own EDataType which express a domain specific type but is mapped to ``java.lang.String`` all the same. It makes the Ecore model more explicit and paves the way for a behavior which can be specific to this particular type.

<figure>
    <a href="{{ site.url }}/images/blog/datatype2.png"><img src="{{ site.url }}/images/blog/datatype2.png"></a>    
    <figcaption>We are know sure we won't mix cutiemarks with something else</figcaption>
</figure>

If your custom datatype is not mapped to a very standard Java type, then make sure your implementation **is compliant with the equals/hashcode contract**.

### ☑ the .genmodel output folders are specified or made empty

A simple right-click, *Generate All* action on the genmodel should give the result you intend. Don't rely on peoples **knowing** before-hand that you should only generate the `model` and `edit` plugin for instance.
You can do so in making the corresponding `[...] Directory` properties empty.

<figure>
    <a href="{{ site.url }}/images/blog/empty-tests-directory.png"><img src="{{ site.url }}/images/blog/empty-tests-directory.png"></a>    
    <figcaption>Emptying the Tests Directory property</figcaption>
</figure>

The editor will then adapt its contextual menu and *Generate all* will not launch the tests generation.

<figure>
    <a href="{{ site.url }}/images/blog/disabled-gen.png"><img src="{{ site.url }}/images/blog/disabled-gen.png"></a>    
    <figcaption>Un-used generations are disabled</figcaption>
</figure>

Also it is generally better to use `src-gen` instead of `src` as the final folder, take the chance to update that at the same time.

<figure>
    <a href="{{ site.url }}/images/blog/srcgen-model-directory.png"><img src="{{ site.url }}/images/blog/srcgen-model-directory.png"></a>    
    <figcaption>Use src-gen as an output directory by default</figcaption>
</figure>


### ☑ the .genmodel base package is specified

The `base package` property in the *.genmodel* file as it drives your Java namespace. You should **never introduce empty EPackages** to get the Java namespace result you want but instead you should use the `base package` property.

<figure>
    <a href="{{ site.url }}/images/blog/basepackage.png"><img src="{{ site.url }}/images/blog/basepackage.png"></a>    
    <figcaption>Specifying the base package in the genmodel properties</figcaption>
</figure>








