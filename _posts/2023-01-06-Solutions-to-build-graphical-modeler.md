---
layout: post
title: Building Graphical Modeling Tools: Approaches to Reducing Complexity
categories: [modeling]
tags: [draft]
---

Building graphical modeling tools can be a complex undertaking, especially if they need to support many features and functions. At Obeo, we have extensive experience in this area and strive to make the process as easy and accessible as possible. To accomplish this, we rely on several strategies, including modular design, higher-level abstractions, and the ability to iterate quickly on a tool definition.

## The Fellowship of the Modules 

Just like how the quest to destroy the One Ring in the Lord of the Rings was made easier by breaking it down into smaller tasks and delegating them to various members of the fellowship, we at Eclipse modeling technologies use a modular design to manage complexity in our software. Each project is responsible for a specific task, delivering components that can be reused and integrated into a tool for the end user.

For example, 
- [EMF](https://www.eclipse.org/modeling/emf/) handles model data and its API, 
- [Sirius](https://www.eclipse.org/sirius) focuses on editors and tooling, 
- [EMF Compare](https://www.eclipse.org/emf/compare/) enables the comparison, merging, and conflict resolution of different versions of models, 
- [Acceleo](https://www.eclipse.org/acceleo/) allows for code or text generation from models, 
- [M2Doc](https://www.m2doc.org/) produces reports and documents using models and diagrams as inputs.

This modular design has several benefits. It makes the software easier to understand and work on, as you can focus on one module at a time rather than trying to comprehend the entire system all at once. Modular design also facilitates code and functionality reuse. If you build a module that does something useful, you can use it in other projects. The Sirius project is a good example of this, as it provides a complete set of features that are reused and exposed through hundreds of graphical modelers. You can see some examples in the [Sirius Gallery]( https://www.eclipse.org/sirius/gallery.html)

While modular design is useful, it is not a perfect solution and does have some challenges. One challenge is ensuring that the modules work well together and do not have conflicts or dependencies. This can be especially difficult when the modules are evolving independently within their own projects. To address this issue, we coordinate with other projects within the Eclipse Release Train and build an integrated suite called the "Obeo Designer Community," which is a ready-to-use packaging.

<figure>
    <a href="https://www.obeodesigner.com/en/download"><img src="{{ site.url }}/images/blog/2023/od.png"></a>
    <figcaption>Obeo Designer download</figcaption>
</figure>


## Inception: The Higher-Level Abstraction Edition 

Just like Cobb and his team in Inception, we use higher-level abstractions to hide the underlying complexity of building a graphical modeling software and make the process more manageable for our users.

Higher-level abstractions can take many forms, such as libraries, frameworks, or domain-specific languages (DSLs). At Obeo, we use DSLs as our choice for higher-level abstractions. An example of this is Sirius.

When you define a tool using Sirius, you specify the graphical modeler you want to achieve in terms of graphical shapes and how these shapes are mapped to the domain model. You can also specify a set of editors, actions, and wizards that can be launched by the end user, without having to deal with the details of coding these features on the underlying platform. Sirius handles these details behind the scenes.

<figure>
    <img src="{{ site.url }}/images/blog/2016-2017/1capture.png">
    <figcaption>Part of a tool definition and the corresponding result for the "Family" DSL.</figcaption>
</figure>

However, higher-level abstractions also have their challenges. One challenge is that they can add an extra layer of complexity to the software. Developers must understand how the abstraction works and how to use it correctly. To help with this, we offer support and expertise, training, and tutorials for getting started with Sirius. We also hold the SiriusCon conference each year since 2015 to help our community discover what they can do with Sirius.

Another challenge is that higher-level abstractions can be limiting. They may not provide all the features and flexibility that developers need, or they may make it difficult to do things in a different way. To address this, we allow for tool behavior to be extended with Java code when necessary. This is useful when the tool needs to interface with another tool directly, rather than through file exchanges, or when specific computations or user interfaces are required.

The Eclipse Modeling platform is generally extensible, and EMF, Compare, Acceleo, Sirius, and other projects provide dedicated extension points to allow their behavior to be customized using Java code and APIs. In addition, Sirius and Acceleo allow for branching out to simple Java code directly, without the need to fully understand the Eclipse platform.

# The Fast and the Furious of Graphical Modeling Tools: Hot Reloading

Like the crew in the Fast and Furious franchise, we aim to reduce the complexity of building graphical modeling software by enabling fast iteration and turnaround.

Fast iteration means being able to make changes to the software quickly and easily, and see the results of those changes right away.
In the case of Sirius two factors are enabling this, first by providing a higher level abstraction to define modeling tool one can express quicker and with more precision what the tool should look like and do. The second factor, and this one stands out quite a bit compare to the other frameworks you can use to build a graphical tool, is that Sirius will hot-reload your tool definition, you are able to instantly see the tool in action, adapt it's definition, see the result, and iterate.
It's life changing, as then the cost of trying another way to represent the domain and interact with it is only minutes, and going back to the previous version of the tool is one CTRL-Z away.


<figure>
    <img src="{{ site.url }}/talks/ModelingAvengers/pics/dynamic-shapes-vsm.png">
    <figcaption>Part of a tool definition and the corresponding result for a DSL related to farming.</figcaption>
</figure>

With Sirius Web we even go one step further in reducing this feedback loop: you adapt the tool, it's instantly usable by all the engineers accessing it directly from their web browser.

----
To summarize, building a graphical modeling tool can be complex, but there are several ways to approach this complexity. Modular design allows for easier understanding and reuse of code, while higher-level abstractions can hide underlying complexity from the user. Fast iteration and turnaround is also important for efficient development. Obeo has been working on technologies to make building graphical modeling tools more accessible for many years now, and we are excited by the prospects of what is to come on this path : while Sirius on the desktop has proven this is an efficient way to tackle this complexity, [Sirius on the Web](https://www.eclipse.org/sirius/sirius-web.html) goes even one step further in making such tools accessible to anyone.



