---
layout: post
title: Metamodel (Ecore) Design Checklist
categories: [eclipse]
tags: [ecore, eclipse, emf]
---

This is an index page for the *Metamodel (Ecore) Design Checklist* serie, a condensed version listing all the rules of the article ([part1](../ecore-design-checklist-part1) and [part2](../ecore-design-checklist-part2)) for your convenience.

I compiled the following checklist based on my personal experience, this is not exhaustive and I expect it to live and get richer over time.

> Most of the checks stated here are very easy to comply with when considered from the start. 
> When it's later down the road the gain/risk ratio should be evaluated as some changes might need to update some code, some files or might just be too much work to be worth it then. 
> Because of this and because we sometime learned the hard way you might quite easily find some Ecore models I authored which are not 100% compliant with this list ;).

By the way, feel free to [tell me about your own rules](https://twitter.com/bruncedric), I might add it to the list!

### Ground rules

|:-------------:| -----:|
|[The purpose and audience of the models are stated ](../ecore-design-checklist-part1#the-purpose-and-audience-of-the-models-are-stated)| ☑ |
|[The nsURI is the definitive one and is consistent with your naming conventions.  ](../ecore-design-checklist-part1#the-nsuri-is-the-definitive-one-and-is-consistent-with-your-naming-conventions)| ☑ |
|[Nested EPackages are not used. ](../ecore-design-checklist-part1#nested-epackages-are-not-used)| ☑ |
|[Names are real ones, precise and consistent. ](../ecore-design-checklist-part1#names-are-real-ones-precise-and-consistent)| ☑ |
|[Reference and attribute names are consistent. ](../ecore-design-checklist-part1#reference-and-attribute-names-are-consistent)| ☑ |
|[All the non-abstract EClasses are supposed to be instanciated. ](../ecore-design-checklist-part1#all-the-non-abstract-eclasses-are-supposed-to-be-instanciated)| ☑ |
|[0..1 and 1..1 cardinalities have been reviewed. ](../ecore-design-checklist-part1#and-11-cardinalities-have-been-reviewed)| ☑ |
|[Containment relationships have been reviewed. ](../ecore-design-checklist-part1#containment-relationships-have-been-reviewed)| ☑ |
|[Every validation rule which is not enforced by the Ecore model structure itself is named. ](../ecore-design-checklist-part1#every-validation-rule-which-is-not-enforced-by-the-ecore-model-structure-itself-is-named)| ☑ |
|[The concepts are all documented. ](../ecore-design-checklist-part1#the-concepts-are-all-documented)| ☑ |
|[There are no Boolean monsters in the making ](../ecore-design-checklist-part1#there-are-no-boolean-monsters-in-the-making)| ☑ |

### Outside world

|[I decided how instances should be referenced from the outside ](../ecore-design-checklist-part1#i-decided-how-instances-should-be-referenced-from-the-outside)| ☑ |
|[A user can't introduce cyclic references in between model fragments ](../ecore-design-checklist-part1#a-user-cant-introduce-cyclic-references-in-between-model-fragments)| ☑ |
|[The dependencies in between EPackages are in control ](../ecore-design-checklist-part1#the-dependencies-in-between-epackages-are-in-control)| ☑ |
|[The concepts which might be extended by subtypes are clearly identified ](../ecore-design-checklist-part1#the-concepts-which-might-be-extended-by-subtypes-are-clearly-identified)| ☑ |

### Scalability 

|[Instances which will be present a lot in the models have a concise serialization ](../ecore-design-checklist-part2#instances-which-will-be-present-a-lot-in-the-models-have-a-terse-serialization)| ☑ |
|[Everything which is serialized needs to be serialized ](../ecore-design-checklist-part2#everything-which-is-serialized-needs-to-be-serialized)| ☑ |
|[Derived features are fast, straightforward, or externalized ](../ecore-design-checklist-part2#derived-features-are-fast-straightforward-or-externalized)| ☑ |
|[There is no EClass which could be replaced by an EDatatype ](../ecore-design-checklist-part2#there-is-no-eclass-which-could-be-replaced-by-an-edatatype)| ☑ |
|[The model has some structure](../ecore-design-checklist-part2#the-model-has-some-structure)| ☑ |
|[It is possible to load part of the model without loading everything](../ecore-design-checklist-part2#it-is-possible-to-load-part-of-the-model-without-loading-everything)| ☑ |
|[The implementation classes are using MinimalEObjectImpl ](../ecore-design-checklist-part2#the-implementation-classes-are-using-minimaleobjectimpl)| ☑ |

### Java

|[Multiple inheritance is not over-used ](../ecore-design-checklist-part2#multiple-inheritance-is-not-over-used)| ☑ |
|[Custom DataType are used in every situation where it makes sense ](../ecore-design-checklist-part2#custom-datatype-are-used-in-every-situation-where-it-makes-sense)| ☑ |
|[The .genmodel output folders are specified or made empty ](../ecore-design-checklist-part2#the-genmodel-output-folders-are-specified-or-made-empty)| ☑ |
|[The .genmodel base package is specified ](../ecore-design-checklist-part2#the-genmodel-base-package-is-specified)| ☑ |


