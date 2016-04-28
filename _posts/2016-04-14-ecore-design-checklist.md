---
layout: post
title: Metamodel (Ecore) Design Checklist
categories: [draft]
tags: [draft]
---

THIS IS A DRAFT, PLEASE DO NOT SHARE AT THIS STAGE

### Ground rules

|:-------------:| -----:|
|[The purpose and audience of the models are stated ](../ecore-design-checklist-part1)| ☑ |
|[The nsURI is the definitive one and is consistent with your naming conventions.  ](../ecore-design-checklist-part1)| ☑ |
|[Nested EPackages are not used. ](../ecore-design-checklist-part1)| ☑ |
|[Names are real ones, precise and consistent. ](../ecore-design-checklist-part1)| ☑ |
|[Reference and attribute names are consistent. ](../ecore-design-checklist-part1)| ☑ |
|[All the non-abstract EClasses are supposed to be instanciated. ](../ecore-design-checklist-part1)| ☑ |
|[0..1 and 1..1 cardinalities have been reviewed. ](../ecore-design-checklist-part1)| ☑ |
|[Containment relationships have been reviewed. ](../ecore-design-checklist-part1)| ☑ |
|[Every validation rule which is not enforced by the Ecore model structure itself is named. ](../ecore-design-checklist-part1)| ☑ |
|[The concepts are all documented. ](../ecore-design-checklist-part1)| ☑ |
|[There are no Boolean monsters in the making ](../ecore-design-checklist-part1)| ☑ |

### Outside world

|[I decided how instances should be referenced from the outside ](../ecore-design-checklist-part1)| ☑ |
|[A user can't introduce cyclic references in between model fragments ](../ecore-design-checklist-part1)| ☑ |
|[The dependencies in between EPackages are in control ](../ecore-design-checklist-part1)| ☑ |
|[The concepts which might be extended by subtypes are clearly identified ](../ecore-design-checklist-part1)| ☑ |

### Scalability 

|[Instances which will be present a lot in the models have a terse serialization ](../ecore-design-checklist-part1)| ☑ |
|[Everything which is serialized needs to be serialized ](../ecore-design-checklist-part1)| ☑ |
|[There is no EClass which could be replaced by an EDatatype ](../ecore-design-checklist-part1)| ☑ |
|[The implementation classes are using MinimalEObjectImpl ](../ecore-design-checklist-part1)| ☑ |
|[The model has some structure](../ecore-design-checklist-part1)| ☑ |

### Java

|[Multiple inheritance is not over-used ](../ecore-design-checklist-part1)| ☑ |
|[Custom DataType are used in every situation where it makes sense ](../ecore-design-checklist-part1)| ☑ |
|[the .genmodel output folders are specified or made empty ](../ecore-design-checklist-part1)| ☑ |
|[the .genmodel base package is specified ](../ecore-design-checklist-part1)| ☑ |


