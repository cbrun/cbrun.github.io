---
layout: post
title: Metamodel (Ecore) Design Checklist index
categories: [draft]
tags: [draft]
---

## Ground rules

| ☑ [The purpose and audience of the models are stated ]()| |
| ☑ [The nsURI is the definitive one and is consistent with your naming conventions.  ]()| |
| ☑ [Nested EPackages are not used. ]()| |
| ☑ [Names are real ones, precise and consistent. ]()| |
| ☑ [Reference and attribute names are consistent. ]()| |
| ☑ [All the non-abstract EClasses are supposed to be instanciated. ]()| |
| ☑ [0..1 and 1..1 cardinalities have been reviewed. ]()| |
| ☑ [Containment relationships have been reviewed. ]()| |
| ☑ [Every validation rule which is not enforced by the Ecore model structure itself is named. ]()| |
| ☑ [The concepts are all documented. ]()| |
| ☑ [There are no Boolean monsters in the making ]()| |

## Scalability related

| ☑ [The implementation classes are using MinimalEObjectImpl ]()| |
| ☑ [Instances which will be present a lot in the models have a terse serialization ]()| |
| ☑ [Everything which is serialized needs to be serialized ]()| |
| ☑ [There is no EClass which could be replaced by an EDatatype ]()| |

## Java-related implications

| ☑ [Multiple inheritance is not over-used ]()| |
| ☑ [Custom DataType are used in every situation where it makes sense ]()| |
| ☑ [the .genmodel output folders are specified or made empty ]()| |
| ☑ [the .genmodel base package is specified ]()| |

## Outside world

| ☑ [I decided how instances should be referenced from the outside ]()| |
| ☑ [A user can't introduce cyclic references in between model fragments ]()| |
| ☑ [The dependencies in between EPackages are in control ]()| |
| ☑ [The concepts which might be extended by subtypes are clearly identified ]()| |
