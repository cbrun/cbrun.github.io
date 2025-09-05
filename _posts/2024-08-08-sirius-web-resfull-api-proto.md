---
layout: post
title: "Opening Up Sirius Web: A REST API Prototype"
categories: [modeling]
tags:
  - modeling
  - emf  
  - sirius-web
---

One of the big ideas behind Sirius Web is openness. Not just “open” as in *open source*, but also “open” as in *working smoothly with the rest of the ecosystem*.

Under the hood, the Sirius Web client talks to the backend using GraphQL. This works great for the web client itself, because GraphQL gives us fine-grained control over what a UI widget asks for. But here’s the catch: GraphQL isn’t always the friendliest option when you want to integrate with other tools and platforms.

That’s what this prototype is about: exposing Sirius Web’s backend through a more classic, pervasive approach, good old REST document APIs.


## Why REST?

By going REST, we can make the Sirius Web backend feel familiar to a much broader range of tools and workflows. I also made sure this API plays nicely with EMF’s use of URIs. That means you can simply get and set model content with nothing more than EMF Core (yes, that tiny Java library you can pull from Maven). The prototype also takes care of element IDs for you.

In practice, this opens up some fun possibilities:

* **Data science workflows**: Access your model elements as CSV, ready to be consumed in a Jupyter notebook.
* **Desktop modeling**: Open and edit an EMF model in Sirius Desktop, even if it’s hosted on Sirius Web.
* **Custom automation**: Write a Java program that fetches a model, tweaks it, and saves changes back to the server, all using plain EMF APIs, without even needing a dedicated Ecore Java API. (The EPackages are retrievable through a REST endpoint.)

## What’s Inside the Prototype

Here’s what’s already working today:

* **Formats supported**: GET and PUT for XMI, zipped XMI, and Binary endpoints.
* **CSV export**: GET support for model elements as CSV.
* **Identity preservation**: IDs are provided in both XMI and Binary serialization, so object identity is preserved when you save resources back.

But keep in mind: this is still a **prototype**. It’s fine for proofs of concept, not production. At the moment, all model/project data is accessible to non-logged users, so yes, handle with care.

---

## What’s Missing (for now)

There are a few gaps you should be aware of:

* No access rights or authorization management yet.
* Error handling and proper HTTP error codes aren’t implemented.
* Only mono-valued attributes are exposed through CSV.

---

## Where Could This Go Next?

One area I’d love to explore is **PUT-like requests for CSV**. Imagine editing model data in a spreadsheet and pushing changes back directly. Unfortunately, I couldn’t make LibreOffice play nice with that yet, but it’s a direction worth exploring.

This prototype is just a first step, but it’s already a powerful way to make Sirius Web more approachable to a wide range of ecosystems. REST might not be as fancy as GraphQL, but it’s familiar, versatile, and plays well with many tools people already use every day.

If you’re curious, give it a try, just don’t forget it’s early days, and production readiness is still a few steps away, here is a code overview to get started:

## Code overview

<details>
<summary>Relevant source files</summary>
<ul>
<li>[restfulemf/backend/sirius-components-restfulemf/README.md](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/README.md)</li>
<li>[restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java)</li>
</ul>
</details>

### Purpose and Scope

This document provides an overview of the RESTful EMF (Eclipse Modeling Framework) backend system built on Eclipse Sirius. The system exposes EMF models through REST APIs, enabling remote access to modeling data in multiple serialization formats including binary XML, XMI, CSV, and compressed variants. The system supports both read and write operations through standard HTTP methods, making EMF models accessible to diverse client applications including Jupyter notebooks, Java EMF clients, and Sirius Desktop tools.

For detailed information about specific REST API endpoints and serialization formats, see [API Endpoints and Serialization Formats](/cbrun/sirius-web-playground/2.1-api-endpoints-and-serialization-formats). For event-driven document management details, see [Event-Driven Document Management](/cbrun/sirius-web-playground/3-event-driven-document-management). For configuration and setup information, see [EMF and Sirius Configuration](/cbrun/sirius-web-playground/5-emf-and-sirius-configuration).

### System Architecture

The RESTful EMF backend is built as a Spring Boot application that bridges HTTP clients with EMF model repositories through an event-driven architecture. The system provides seamless integration between web-based clients and Eclipse modeling infrastructure.

#### Core Components Architecture

![Architecture]({{ site.url }}/images/blog/2024/restfull/restfull1.png)

**Sources:** [restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L29-L82](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L29-L82)

#### REST API Endpoint Structure

![Endpoints Structure]({{ site.url }}/images/blog/2024/restfull/restfull2.png)

**Sources:** 
- [restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L89-L449](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L89-L449)
- [restfulemf/backend/sirius-components-restfulemf/README.md#L10-L95](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/README.md#L10-L95)

### Supported Serialization Formats

The system provides multiple EMF serialization formats optimized for different client types and use cases:

| Format       | Endpoint Pattern                                      | HTTP Methods | Use Case              | Key Features                      |
|--------------|--------------------------------------------------------|--------------|-----------------------|-----------------------------------|
| Binary XML   | `/projects/{id}/{doc}/bin`                             | GET, PUT     | EMF Runtime clients   | Fast, compact, preserves IDs      |
| XMI          | `/projects/{id}/{doc}/xmi`                             | GET, PUT     | Human-readable access | Standard format, preserves IDs    |
| Zipped XMI   | `/projects/{id}/{doc}/xmi.zip`                         | GET, PUT     | Compressed transfer   | Reduced bandwidth, preserves IDs  |
| CSV          | `/projects/{id}/{doc}/csv`                             | GET only     | Data science tools    | Jupyter-compatible, flattened view|
| EPackages    | `/projects/{id}/epackages/bin`                         | GET          | Reflective access     | Metamodel information             |

**Sources:** [restfulemf/backend/sirius-components-restfulemf/README.md#L12-L81](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/README.md#L12-L81)

### Event-Driven Document Management

Document updates are processed through an event-driven architecture using the `IEditingContextEventProcessorRegistry`. This enables real-time collaboration and maintains data consistency across multiple clients.

#### Document Update Flow

![Update Flow]({{ site.url }}/images/blog/2024/restfull/restfull3.png)

**Sources:** 
- [restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L394-L428](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L394-L428)
- [restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L61-L61](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L61-L61)

### Key Integration Points

The system integrates with several Eclipse Sirius components to provide a complete modeling backend:

- **`IEditingContextSearchService`** - Locates editing contexts for projects
- **`ISemanticDataSearchService`** - Retrieves semantic data and documents
- **`IProjectSemanticDataSearchService`** - Maps projects to semantic data
- **`EObjectIDManager`** - Preserves EMF object identities across serialization
- **`JSONResourceFactory`** - Creates internal JSON-based EMF resources

The `RestfulEMFResourceController` class serves as the primary integration point, coordinating between HTTP requests, EMF resources, and the Sirius event system.

**Sources:** 
- [restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L72-L82](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L72-L82)
- [restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L430-L447](https://github.com/cbrun/sirius-web-playground/blob/1c2f7809/restfulemf/backend/sirius-components-restfulemf/src/main/java/fr/obeo/playground/restfulemf/controllers/RestfulEMFResourceController.java#L430-L447)
