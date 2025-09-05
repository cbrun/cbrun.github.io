---
title: "Intent.pdf"
generated_at: "2025-09-02T09:53:40.059396+00:00"
model: "gpt-4.1-mini"
dpi: 144
pages: 14
---

# Slide-by-slide notes

## Page 1
- The slide introduces a presentation from EclipseCon 2011 by Cédric Brun from Obeo, France.
- It highlights the integration of Mylyn with Intent to improve documentation.
- The key message is making documentation both fun and useful, implying enhanced user engagement and practicality.
- The gears image suggests a focus on tools or processes working together smoothly.
- The slide serves as a title or opening, so detailed content or data points are not yet provided.

## Page 2
- Introduces a character named Alice who questions a design's complexity.
- Alice finds the design unnecessarily twisted or complicated.
- The slide uses Alice to represent a user or stakeholder perspective.
- Implies a need to simplify or clarify the design for better understanding.
- The tone is informal and conversational, aiming to engage the audience.
- Unclear what specific design or product Alice is referring to at this point.

## Page 3
- Bob suggests referring to a design document created three years ago for answers.
- His tone is casual and confident, implying the solution is straightforward.
- The message hints that existing documentation may already address current questions.
- This could imply a reliance on legacy materials rather than new analysis.
- Unclear if the old document is still fully relevant or up to date.

## Page 4
- The page emphasizes that existing documentation ("Doc") already covers EMF Compare functionality.
- It shows a structured developer guide and API reference for EMF Compare, highlighting key classes and methods.
- The documentation includes details on matching processes for model elements and resource sets.
- The tone suggests confidence that current questions can be answered by reviewing this legacy documentation.
- Implicitly, it encourages relying on existing materials rather than creating new explanations.
- Uncertainty remains if the old documentation fully addresses all current needs or if updates are required.

## Page 5
- The page expresses a clear desire for documentation that is easy to access and maintain.
- It emphasizes the need for the documentation to be esthetically appealing.
- The focus is on improving user experience with the documentation.
- Implicitly suggests current documentation may lack these qualities.
- No technical details or specific features are discussed here.
- The intent is to prioritize usability and visual design in future docs.

## Page 6
- The page credits "Literate Modeling" as the powering concept or methodology behind the content.
- It features two individuals, likely key contributors or proponents of Literate Modeling.
- The left image shows a man speaking into a microphone, suggesting a presentation or discussion context.
- The right image shows an older man seated, holding papers, implying a reflective or scholarly role.
- The page implies authority or endorsement by these figures but does not explain Literate Modeling itself.
- No detailed explanation or data about Literate Modeling is provided, leaving its meaning unclear.

## Page 7
- The page explains mixing documentation with model fragments using Literate Modeling syntax.
- It shows how to define the architecture of the "match" package with embedded code snippets.
- The first snippet defines a match resource with a URI pointing to an Eclipse ECore model file.
- The second snippet defines the match EPackage with a namespace URI and prefix linked to Eclipse.
- The intent is to demonstrate integrating executable model fragments directly within documentation.
- It implicitly promotes clarity and maintainability by combining code and docs in one place.
- The exact context or usage of these fragments beyond definition is not detailed here.

## Page 8
- The page illustrates a collaboration workflow integrating multiple editors with a shared repository.
- Eclipse Editor commits changes to the repository, triggering notifications to Doc WEAVER and Web Browser Editor.
- The repository can be implemented with various backends like CDO, Workspace, JGit, or ECR, indicating flexibility.
- The diagram emphasizes real-time synchronization and collaboration across different tools via repository notifications.
- Implicitly, the system aims to streamline multi-tool editing and documentation processes in a unified environment.
- Uncertainty remains about the exact choice or configuration of repository technologies (JGit and ECR are posed as questions).

## Page 9
- The page states that all components interacting with the model act as clients.
- Editors display documents in textual form as clients.
- Compilers act as clients by listening to changes in model fragments.
- Emphasizes a client-based architecture for modular interaction with the model.
- Implies flexibility in adding diverse clients for different roles in the workflow.
- No technical details on client communication or implementation are provided.

## Page 10
- The page presents a domain model diagram for extending a product with features and tests.
- It defines entities like Product, Bundle, Namespace, API, Feature, and different test types.
- Features are split into DeveloperFeature and EndUserFeature, linked to APIs and Interactions respectively.
- Bundles contain namespaces and can be tested by UnitTest and AcceptanceTest classes.
- The model emphasizes relationships such as features belonging to products and tests linked to APIs or interactions.
- The intent is to provide a structured, extensible domain model for managing product features and their testing.

## Page 11
- The page defines the intent behind extending a system or product.
- It highlights two key aspects: validation rules and synchronization logic.
- Emphasizes that extending involves adding rules to validate data or actions.
- Synchronization logic suggests managing consistency across components or states.
- The content is brief and conceptual, lacking detailed examples or context.
- The implicit takeaway is that extensions must ensure correctness and coherence.

## Page 12
- The page explains the intent behind extending features by enabling URI schemes to query the workspace.
- It highlights the use of a specific plugin, `org.eclipse.emf.compare.tests`, for testing EMFCompare features.
- Code snippet shows defining a resource with a URI using a custom protocol `retro:` to reference test project content.
- Emphasizes URI schemes and protocols as mechanisms to access and manage workspace resources programmatically.
- Implicitly suggests that extending involves configuring resource access and linking test projects via URIs.
- The exact role of the `retro:` scheme and its implementation details are not fully explained here.

## Page 13
- The slide outlines the upcoming project milestones and timeline for the next phases.
- March: project acceptance and provisioning is expected.
- June: early adopters will begin building with the project.
- Q3: planned release of version 0.7.0.
- Key future features include a functional workspace backend, an Eclipse IDE textual client, and model synchronization.
- The slide implies steady progress toward a usable release with core infrastructure and client tools.
- No detailed technical specifics or risks are mentioned, leaving some uncertainty about challenges ahead.

## Page 14
- Intent is a new open source project under Mylyn, currently in the Proposal phase awaiting feedback.
- It aims to help developers keep documentation up-to-date with development artifacts like code and models.
- Documentation will integrate with Eclipse tools, reducing developer burden and improving usefulness.
- Inspired by Donald Knuth’s Literate Programming, focusing on explaining to humans what the computer should do.
- Intent will be presented at Eclipse Con 2011 and is developed by Obeo, aligned with Eclipse 3.7 (Indigo) release.
- The project includes mission, use cases, architecture, release plans, and related articles for comprehensive overview.

