---
title: "EclipseModelingGuidedTour-aql.pdf"
generated_at: "2025-09-02T09:03:44.800872+00:00"
model: "gpt-4.1-mini"
dpi: 144
pages: 18
---

# Slide-by-slide notes

## Page 1
- The page introduces "Acceleo Query Language" as a small, fast, and strong tool designed to assist with software tooling.
- It positions the language as a helpful sidekick, implying it complements existing tools rather than replacing them.
- The slide is part of a presentation titled "A Guided Tour of Eclipse Modeling," dated October 23, 2017, suggesting the language is relevant to Eclipse modeling users.
- The presence of logos for Obeo and EclipseCon Europe indicates official endorsement or sponsorship.
- The background image featuring two serious-looking men in a dramatic setting may aim to convey strength or reliability, though its relevance to the content is unclear.
- No technical…

## Page 2
- The page highlights the motivation behind developing a query language specifically for Sirius, a modeling tool.
- It shows a screenshot of a user interface where different query language expressions can be selected or entered, indicating flexibility and integration.
- The emphasis on "Query language for Sirius" suggests the language is tailored to enhance Sirius’s capabilities.
- The presence of legacy and various query options implies a need to support multiple query syntaxes or transition from older languages.
- The slide implicitly conveys the goal of improving or simplifying querying within Sirius, but does not detail specific problems addressed or benefits.
- Uncertainty remains…

## Page 3
- The page explains the motivation for creating a query language tailored to the Sirius modeling environment, emphasizing integration and expressiveness.
- It shows a screenshot of a document template using M2Doc expressions to generate structured documentation from model data, illustrating practical application.
- Key data points include examples of iterating over tables and columns, extracting properties like names, types, and constraints dynamically.
- The intent is to highlight how M2Doc enables automated, model-driven document generation, improving efficiency and accuracy.
- The page assumes familiarity with modeling concepts and M2Doc syntax, which may limit accessibility for…

## Page 4
- The page illustrates the motivation behind creating a query language integrated with the Sirius modeling environment, focusing on expressiveness and seamless integration.
- It shows a screenshot of a document template using M2Doc expressions to generate structured documentation from model data, highlighting practical application.
- A code snippet in Acceleo-MTL demonstrates template-based generation of elements, emphasizing flexibility in querying and document generation.
- The implicit takeaway is the value of embedding query expressions directly within documentation templates to automate and streamline model-based documentation.
- The page assumes familiarity with modeling tools and…

## Page 5
- The page explains the motivation for integrating a query language within the Sirius modeling environment to enhance expressiveness and seamless model data manipulation.
- It highlights the use of M2Doc expressions to generate structured documentation directly from model data, improving automation and consistency.
- A code snippet in ALE (Action Language for EMF) illustrates how behavior can be defined and executed within the modeling framework, showcasing practical application.
- The implicit takeaway is that embedding such languages enables more powerful, maintainable, and automated documentation and model handling.
- The page assumes familiarity with Sirius, M2Doc, and EMF concepts;…

## Page 6
- The page defines "Language" as a combination of syntax, semantics, tooling, and runtime components.
- It focuses specifically on the syntax aspect, noting it is familiar to users of OCL (Object Constraint Language).
- The syntax is described as easily extensible, implying adaptability for various use cases.
- The content suggests the language design aims to leverage existing knowledge (OCL) while allowing customization.
- There is no detailed explanation of semantics, tooling, or runtime on this page, indicating partial coverage.
- The intent is to clarify the foundational syntax element within a broader language framework.

## Page 7
- The page defines "Language" as a combination of syntax, semantics, tooling, and runtime, focusing here on syntax and semantics.
- Syntax is designed to be familiar to users of OCL and is easily extensible, suggesting adaptability for different needs.
- Semantics are statically typed, ensuring type safety, but also forgiving by allowing null or unset values and collections, which adds flexibility.
- The intent is to highlight a balanced language design that is both robust and user-friendly.
- No detailed explanation of tooling or runtime components is provided, leaving some aspects unclear.

## Page 8
- The page defines "Language" as a combination of syntax, semantics, tooling, and runtime components, emphasizing the first three here.
- Syntax is designed to be familiar to users of OCL and is easily extensible, allowing adaptation to different needs.
- Semantics are statically typed, promoting type safety, but also forgiving regarding null or unset values and collections.
- Tooling is embeddable and supports static typing with advanced type inference, enhancing integration and usability.
- The overall intent is to present a language framework that balances familiarity, extensibility, safety, and tooling flexibility.
- The runtime aspect is mentioned but not detailed, leaving some…

## Page 9
- The page defines a "Language" as a combination of syntax, semantics, tooling, and runtime components, focusing on the first three here.
- Syntax is designed to be familiar to users of OCL and is easily extensible to adapt to various needs.
- Semantics are statically typed but forgiving, allowing null or unset values and collections.
- Tooling is embeddable and supports static typing with rich type inference.
- Runtime is described as fast, small, and interpreted, emphasizing efficiency.
- The page implicitly promotes a language framework that balances strict typing with flexibility and performance.

## Page 10
- The page illustrates a model query using a syntax similar to OCL, selecting elements whose names start with "I" from a UML model of a travel agency.
- It shows a hierarchical structure of the model, including packages, components, use cases, and a class named "Invoice" with its properties.
- The example emphasizes how to navigate and filter model elements programmatically using the language's syntax.
- The diagram highlights relationships such as packaged elements, use cases, and attributes within the model.
- The intent is to demonstrate practical usage of the language for querying and manipulating UML models.
- The exact semantics of the query or the broader context of its application…

## Page 11
- The page explains differences between the query language used (AQL) and standard OCL, highlighting syntax and type handling variations.
- It notes that AQL implicitly applies collect() and flatten() in select() operations, avoiding nested collections.
- Variable denotation is optional in AQL, unlike OCL where every expression requires a variable name.
- AQL supports only Lists and Sets with stable order, not other collection types like Bag or OrderedSet.
- Types in AQL are optional in lambdas, support union types, are inferred at validation, and do not require explicit casting.
- The intent is to clarify that while similar to OCL, AQL offers more flexibility and simplifications for…

## Page 12
- The page describes a process flow for handling input strings through parsing, optional validation, and evaluation stages, emphasizing speed and intelligence in these steps.
- Input strings are parsed into an Abstract Syntax Tree (AST), which is then optionally validated to produce validation results or directly evaluated using model and variable bindings.
- Validation produces an AST and a validation result, while evaluation produces an execution log and evaluation result, highlighting that validation is not mandatory.
- The diagram shows dependencies on EPackages, Java services, and model bindings, indicating integration with external resources.
- The key message is that the system…

## Page 13
- The page highlights performance aspects of query implementation, focusing on speed during evaluation and intelligence during validation.
- A bar chart compares time spent on different query types refreshing a large diagram (3,267 elements), breaking down interpreter dispatch, variable management, and external code calls.
- Raw interpreter dispatch dominates time in some queries (up to ~31%), while others show more balanced time across tasks, with external calls and variable management also significant.
- The intent is to show that evaluation is optimized for speed, while validation is designed to be smart and efficient.
- A note mentions further optimizations after October 2015,…

## Page 14
- The page discusses query execution performance using a profiler to isolate execution time across different model sizes (small, medium, large).
- AQL queries show good performance with low memory usage, while IncQuery offers very fast recalculations (<50 ms) but requires up to twice the memory (~1.2 GB for large models).
- A bar chart compares execution times for three query types (MTL, AQL, EIQ) across model sizes, showing IncQuery (EIQ) generally faster on recalculation but with higher initial execution times and memory cost.
- The data implies a trade-off between speed and memory, favoring IncQuery for responsiveness in large models.
- Exact memory profiling details and some…

## Page 15
- The page explains a predicate-based analysis approach for type inference in node creation, focusing on union types like "Participant" or "Interaction."
- It shows a decision tree where context changes based on whether the current element (`self`) is an Interaction or Participant, adjusting features like `executions` or `type`.
- The logic uses conditional checks (`oclIsKindOf`) to differentiate types and update context accordingly, ensuring correct type assignment during model processing.
- The diagram clarifies how predicates guide the flow of type inference, supporting accurate variable and feature management.
- The intent is to demonstrate a structured method for handling union types…

## Page 16
- The page demonstrates how the system can be extended using Java by including custom methods, operator semantics, and domain-specific services.
- It provides a Java example of an absolute value method (`abs`) with documentation and usage examples, showing how to integrate Java code for functionality extension.
- Operator semantics are illustrated with a simple string concatenation example, indicating how operators can be customized.
- A domain-specific service example calculates the number of cousins for a given person by traversing family relationships, highlighting practical use cases.
- The intent is to show flexibility and ease of extending the platform with Java code for various…

## Page 17
- The page outlines the runtime dependencies required, listing specific libraries such as Eclipse Acceleo, Google Guava, ANTLR runtime, and Eclipse EMF components.
- It highlights that the runtime consists of 13,000 lines of manually written Java code, with a total of 21,000 lines including generated code, primarily for the EMF API handling the abstract syntax tree (AST).
- The runtime is explicitly noted as not being implemented as a singleton, implying multiple instances can exist.
- The focus is on providing a clear overview of the runtime’s composition and dependencies without detailing its internal workings or usage.
- There is no explicit explanation of why the runtime is not a…

## Page 18
- The page explains how to obtain the technology, noting it has been shipped since 2015 as part of the Acceleo project.
- It provides a direct link to the official documentation for further guidance.
- Lists other technologies already using this technology, including Eclipse Sirius, M2doc (for generating .docx files from models), and ALE (Action Language for EMF).
- The presence of a "Part of The Release Train" stamp implies it is integrated into a larger, coordinated release cycle.
- The content is straightforward with no evident uncertainties or ambiguities.

