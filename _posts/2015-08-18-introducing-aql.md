---
layout: post
title:  AQL - a new interpreter for Sirius
categories: [modeling]
tags:
  - eclipse
  - acceleo
  - sirius
  - ecore
  - aql
permalink: /eclipse/introducing-aql/
---

TL;DR: we've been working on a new query interpreter for Sirius which is small, simple, fast, extensible and bring richer validation. It's been released for early adopters with Sirius 3.0 but will be the recommended
interpreter for Sirius 3.1 in October. The MTL interpreter (`[/]`) will be deprecated at some point, this moment depending on how fast the community adopts the new `aql:` interpreter.

## Background and motivation

One of the key factor making Sirius so flexible is the ability to rely on queries when defining your graphical mapping. 
Every configurable field rendered with a yellow background in the tooling specification editor can be set either with a literal value or with a query which will be interpreted at runtime.

Sirius can be extended with new query interpreters through Eclipse plugins, each having its own prefix.

<figure>
    <a href="{{ site.url }}/images/blog/aql-completion.png"><img src="{{ site.url }}/images/blog/aql-completion.png"></a>    
    <figcaption>AQL's Code completion within the .odesign editor</figcaption>
</figure>

Some interpreters are available by default notably `feature:`, `var:`, or `service:` which are direct access either to a model element feature, a context variable or a Java service. These interpreters have the tiniest overhead you can think of. 

For everything else, `[/]` is the reference implementation : an OCL variant used in Acceleo 3.x and based on the MOFM2T OMG Standard.

A specific plugin bring the `<%%>` syntax which was the first interpreter supported by Sirius (long before Sirius was even named 'Sirius') and is using Acceleo 2 behind the scene. 
The Acceleo2 syntax is a mix in between XPath and OCL syntax, it has been deprecated long ago (and as such has to be installed through a [specific update site](https://download.eclipse.org/sirius/updates/legacy)) but you might still find it in .odesign models which originated before Sirius was contributed to Eclipse.

Being `<%%>`, `[/]` or even the "forever experimental" `ocl:`, every interpreter was implemented by integrating a pre-existing language and trying to make him happy about the dynamic nature of Sirius :
during a diagram refresh, a given query might be evaluated thousands of times, each time on different `EObjects` which would not even necessarly share a common type, each time  with different variables values.

This *worked* but sometime would lead to fairly complex code just to *integrate* things. To make the MTL interpreter (`[/]`) happy enough to evaluate the query we had to create templates in memory keeping the parameters signature, comparing the signatures with the new context for each variable change and evicting those templates at some point.

Fairly complex code generally means subtle bugs, sub-optimal performance and/or memory usage.

The interpreter is a cornerstone of the flexibility provided by Sirius, it also is a key player in the performance you'll get in the end, so as heavy users of Sirius where painfully migrating from `<%%>` to `[/]` we quickly noticed that we would be better of with an implementation specificaly tailored for Sirius and that it would come at a fraction of the cost of all those migrations.

## A new interpreter

With Sirius 3.0 we started a new interpreter implementation with the goal of being a perfect fit for Sirius:

* Support static and **dynamic** Ecore models, no compilation phase required 
* **the least possible overhead at evaluation time for an interpreted language**: the evaluation actually goes forward and will not even try to validate or compile the expressions. Errors are tracked and captured along the way.
* **strong validation**: types are checked at validation time (in the .odesign editor) and metamodels are analyzed to do some basic type inference and avoid false positive errors.
* **union types**: in the context of Sirius, a variable in a given query have N potential types, with N being often greater than 1. We needed an interpreter embracing this fact and not falling back to *EObject* as soon as there is more than one type.
* a **straightforward implementation** easily extensible with Java classes providing extension methods.
* a very **narrow dependency surface**: only the very central parts of EMF, Guava and Antlr so that we could easily deploy it server-side or in standalone scenarios.


## Proof of Concept

Last summer the proof of concept phase quickly demonstrated that we would not be able to be 100% compatible with the implementation of `[/]` without inheriting limits in the context of Sirius. 

Here is a specific example :

In MTL `[name/]` is a valid expression, though depending on the available variables it might mean *The variable named name* or *The 'name' attribute of the self object*

This is a useful feature for a template language when 99% of the templates have no parameters besides `self`:  this cut the clutter and lead to a template which is more readable:

<figure>
    <a href="{{ site.url }}/images/blog/acceleo-template.png"><img src="{{ site.url }}/images/blog/acceleo-template.png"></a>    
    <figcaption>An Acceleo Template</figcaption>
</figure>

But in the context of an expression defined in a .odesign model : there are **always more than one available variable**: the selected object, the text value entered by the user, the possible sources or targets of an edge and so on.

Using the *implicit self* makes you .odesign file actually way harder to maintain and understand. 

Furthermore from an implementation point of view, "implicit **self** " induces runtime overhead : when a new variable has been set or has a new value, the previous AST parsed from a String had to be invalidated. Again, in the context of Sirius variables values or type are changing **a lot** and are not necessarly sharing a common type besides EObject (this allows us to mix Ecore based instances or UML one in a single editor for instance). 

All these factors led to a runtime which might reparses and re-link a query because a variable changed its value with a completely new type.

That's just one example (among several others), that led us re-consider those choices at the cost of a language which would not be 100% compatible. As such both interpreters will co-exist but the benefits the new one bring should be so strong that this transition time will be kept reasonnable.

## Introducing AQL : Acceleo Query Language.


As languages, AQL and MTL are very close yet there are some notable differences:

* there is no implicit variable reference
* auto-collect and auto-flatten : there is no such thing as a List of List in AQL. 
* type literals can't be in the form of somePackage::someSubPackage::SomeType but instead someSubPackage::SomeType should be directly used
* you can only have Lists or Sets as collections and the order of their elements is always deterministic.

From an implementation point of view AQL:

* is small : 100 non generated Java files
* works with both dynamic or generated Ecore models.
* is fast at runtime with minimal overhead
* is smart at validation time by considering the union types in its analysis
* is easy to re-use, extend and integrate in other contexts.

AQL is a pure Java library  : `org.eclipse.acceleo.query.jar` and is part of the Acceleo project. Here are its dependencies :

<figure>
    <a href="{{ site.url }}/images/blog/aql-deps.png"><img src="{{ site.url }}/images/blog/aql-deps.png"></a>    
    <figcaption>AQL dependencies</figcaption>
</figure>

## Try it !

It is meant to be reused and has already seen several adoptions at [Obeo](https://www.obeosoft.com/fr/). 

If the Sirius use-case matches yours, give it a try and tell us what you think !

With Sirius 3.0 a first version of the AQL interpreter has been released as **Experimental** so that early adopters can work with it. 

<figure>
    <a href="{{ site.url }}/images/blog/install-aql.png"><img src="{{ site.url }}/images/blog/install-aql.png"></a>    
    <figcaption>Install AQL experimental support in Sirius 3.0</figcaption>
</figure>

[EcoreTools](https://www.eclipse.dev/ecoretools/) has been the early-early adopter and has migrated with the Mars release. [UML Designer](https://www.umldesigner.org/) is also using AQL on the master branch since July and more migrations will follow in the upcoming months.

## First benchmarks


We started to measure performances and overhead compared to the other interpreters as even if it was one of the important factor, no specific effort had been made already besides keeping the implementation small and straightforward.

Here is the first bench we made to compare the different interpreters overhead. Projects to reproduce these measures are [published on Github](https://github.com/cbrun/sirius-interpreters-benchmark) if you feel like giving it a shot.

<figure>
    <a href="{{ site.url }}/images/blog/sirius-query-bench-setup.png"><img src="{{ site.url }}/images/blog/sirius-query-bench-setup.png"></a>    
    <figcaption>Benchmarking Environment</figcaption>
</figure>

The benchmark is a composed of synchronized diagram descriptions, one for each interpreter. They are strictly equivalent from the end-user point of view.

* `[/]` is using the Acceleo MTL interpreter
* `<%%>` is using the Acceleo2/Legacy interpreter
* `AQL` uses the AQL interpeter
* `Service:` uses the service: interpreter which dispatch to a Java method defined by the Specifier
* `feature:` : is only using direct access to a attributes, references or hardcoded logic for eAllContents for instance.
* `Service over AQL` : uses the same Java services as service: but dispatch those through aql, for comparison.

I created a diagram instance for every diagram description on top of a simple Ecore model, the corresponding diagrams have 3267 elements (node, edges, list items). After a "warmup" phase,  I trigger an explicit *refresh* of the diagram while profiling with Yourkit in tracing (non-adaptative) mode.

Then I split the methods call-tree to break down the time spent in three categories: 

* *calling external code/eAllContents* : 'external' is EMF here. This is the time spent in doing eGet() or eAllContents() for instance. 
* *managing variables* : during a single refresh the interpreter state changes thousands of times, this is the time spent in managing these changes.
* *interpreter dispatch* : the CPU time used by the interpreter to decide what to call (eGet, eAllContents, a java service...).

All these numbers are relativised with 100% being the total time of a given refresh, which in this case was in the order of 500ms to 1sec. 


<figure>
    <a href="{{ site.url }}/images/blog/sirius-query-bench.png"><img src="{{ site.url }}/images/blog/sirius-query-bench.png"></a>    
    <figcaption>Sirius 3.0 Interpreters Overhead</figcaption>
</figure>


A few small things you can notice already :

- We are focusing **at most** on `40%` of the refresh time: in the 200 to 500ms range.
- `<%%>` and  `[/]` tend to have a bigger overhead managing variables. That's because their implementation are eagerly creating data structures each time a new value is set.
- `<%%>` spent less time in eGet/eAllContents. That's because this 10 years old implementation benefits from an `eAllContents()` algorithm which prunes subtrees based on a small analysis of the accessible metamodels.

The main thing you should notice : **there is not much reasons to prefer anything other than AQL**. Indeed `feature:` will always be faster if what you need is a direct access to an attribute or reference but AQL has the same overhead that direct service calls and gives you better analysis and validation capabilities in your .odesign.

## Plan for Sirius 3.1 (release in mid-October)

Since the Sirius 3.0 release we are ramping up : 

* migrating more Sirius based products owned by Obeo and creating helper tools to conduct those.
* ironing out bugs, streamlining things.
* documenting the language and the standard services.
* implementing missing services.
* making it smarter at runtime : AQL will now prune model subtrees if an analysis shows that a subtype can't possibly exist in this branch. And that makes AQL even faster.
* making it smarter at validation time : with static analysis which can consider a contextual branch of alternative.
* more experiments (stay tuned !)

All of these to make [AQL the recommended query language implementation](https://bugs.eclipse.org/bugs/show_bug.cgi?id=470460) for Sirius 3.1 !









