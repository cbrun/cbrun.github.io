---
layout: post
title: Metamodel (Ecore) Design Checklist
categories: [draft]
tags: [draft]
---

THIS IS A DRAFT, PLEASE DO NOT SHARE AT THIS STAGE

### Ground rules

|:-------------:| -----:|
|[The purpose and audience of the models are stated ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[The nsURI is the definitive one and is consistent with your naming conventions.  ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[Nested EPackages are not used. ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[Names are real ones, precise and consistent. ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[Reference and attribute names are consistent. ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[All the non-abstract EClasses are supposed to be instanciated. ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[0..1 and 1..1 cardinalities have been reviewed. ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[Containment relationships have been reviewed. ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[Every validation rule which is not enforced by the Ecore model structure itself is named. ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[The concepts are all documented. ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[There are no Boolean monsters in the making ](./2016-04-14-ecore-design-checklist-part1)| ☑ |

### Outside world

|[I decided how instances should be referenced from the outside ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[A user can't introduce cyclic references in between model fragments ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[The dependencies in between EPackages are in control ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[The concepts which might be extended by subtypes are clearly identified ](./2016-04-14-ecore-design-checklist-part1)| ☑ |

### Scalability 

|[Instances which will be present a lot in the models have a terse serialization ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[Everything which is serialized needs to be serialized ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[There is no EClass which could be replaced by an EDatatype ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[The implementation classes are using MinimalEObjectImpl ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[The model has some structure](./2016-04-14-ecore-design-checklist-part1)| ☑ |

### Java

|[Multiple inheritance is not over-used ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[Custom DataType are used in every situation where it makes sense ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[the .genmodel output folders are specified or made empty ](./2016-04-14-ecore-design-checklist-part1)| ☑ |
|[the .genmodel base package is specified ](./2016-04-14-ecore-design-checklist-part1)| ☑ |


