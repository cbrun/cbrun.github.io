---
layout: post
title: "AI for Capella: Agentic AI as a First Step"
categories:
  - modeling
tags:
  - capella
  - mbse
  - obeo
  - ai
  - arcadia
permalink: /mbse/ai-for-capella-agentic-ai-as-a-first-step/
translation_fr: /mbse/ia-pour-capella-ia-agentique-comme-premier-pas/
excerpt: "A practical look at AI for Capella for MBSE teams, starting with controlled agent access that keeps engineers responsible for model decisions."
draft: true
---

Over the last months, we have been experimenting with how AI could be useful in real Capella workflows. One point became clear very quickly: the value is not in letting AI *do systems engineering*, but in helping engineers interact more efficiently with models, while keeping control of engineering decisions.

In systems engineering, decisions require expertise, judgment, responsibility, and collaboration. AI can help engineers better understand models, navigate complexity, access information, and automate repetitive tasks. But engineers must remain in control of decisions.

This is where the [Capella](https://mbse-capella.org/) tool and the Arcadia method make a real difference. They provide a structured engineering context in which AI can be useful without becoming uncontrolled. AI may help formulate a query, prepare an action, or suggest a next step. Capella remains the environment where the model is accessed and modified. The engineer remains responsible for validation.

Over the past months, we have been exploring several AI use cases around Capella. Among them, one has emerged as a particularly promising first step: enabling AI agents to interact with Capella in a controlled and secure way.

In this article, I would like to share where we are heading, and why our first product-oriented step is to **make Capella accessible to AI agents** in a controlled, explicit, and secure way. This work is intended to become available progressively through a **commercial offering available from the end of July 2026**.

## Our Vision Behind AI for Capella

As systems become increasingly complex, models are no longer just graphical documentation artifacts. They have become shared engineering assets that capture architectures, requirements, analyses, interfaces, viewpoints, and design decisions.

At the same time, the growing importance of models introduces new challenges:

- **Learning** MBSE methods and tools remains difficult for newcomers.
- Large models can be hard to **understand** and **navigate**.
- Information exists within the model but is not always easy to **locate**.
- **Maintaining** consistency across evolving architectures requires continuous effort.
- **Producing documentation** and **communicating** engineering decisions remains time-consuming.

These challenges make AI particularly relevant. Not because it can replace systems engineering, but because **it can help engineers interact more effectively with their models.**

<figure>
    <a href="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-driven-mbse.png">
      <img src="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-driven-mbse.png" alt="AI-driven MBSE">
    </a>
</figure>

Capella models also provide a **valuable foundation for AI**: they contain structured, traceable engineering knowledge that gives AI access to a reliable context, enabling more relevant and useful assistance than would be possible from unstructured information alone.

To be useful in an industrial context, however, AI needs to satisfy several key requirements:

- **Contextualized**, with access to relevant engineering information.
- **Controlled**, operating within defined boundaries.
- **Auditable**, allowing engineers to understand and justify outcomes.
- **Integrated**, fitting naturally into existing workflows.
- **Human-validated**, with engineers retaining final responsibility.

<figure>
    <a href="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/integrated-ai.png">
      <img src="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/integrated-ai.png" alt="Integrated AI for engineering workflows">
    </a>
</figure>

These principles help us sort the AI use cases that are interesting in a demo from those that can realistically become useful in an engineering environment. Several directions are worth exploring:

- Onboarding and Methodological Guidance.
- Natural Language Queries.
- Assisted Documentation.
- Contextual Assistance Inside the Editor.
- Model Review and Consistency Checking.
- Navigation Assistance.

These are the areas where we currently see the greatest potential to help engineers work more effectively with their models.

To support this vision, we are starting with a foundational capability: enabling external AI agents to interact with Capella through a controlled set of services, aka Agentic AI for Capella. Instead of building one assistant for one predefined scenario, this approach gives organizations a way to connect their own AI environment to Capella. Technically, this relies on APIs, MCP, and similar integration mechanisms.

Functionally, the objective is simple: expose selected Capella capabilities to agents, without giving them unrestricted access to models.

This creates a secure and extensible foundation on top of which multiple AI-assisted capabilities can be built over time, while preserving the governance, traceability, and engineering rigor required in industrial environments.

## Capella as an Agent-Ready Platform

Our first **AI for Capella** offering will focus on a simple idea: making Capella an agent-ready platform.

Rather than embedding a specific AI assistant into Capella, we enable Capella to interact with the AI ecosystem chosen by each organization, whether it is Claude, Codex, Mistral, a locally hosted model, or future agent platforms.

The first step is to **connect** Capella with external AI agents through MCP, APIs, and similar integration mechanisms.

<figure>
    <a href="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-agent-for-capella.png">
      <img src="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-agent-for-capella.png" alt="AI agent for Capella">
    </a>
</figure>

An agent could, for example, ask Capella for information about selected model elements, retrieve architectural context, help navigate dependencies, prepare a query, or draft a proposed model change. These actions remain limited to the capabilities explicitly exposed by Capella. Combined with access to documents, knowledge bases, repositories, and enterprise tools, this gives agents a much richer engineering context.

But connectivity alone is not enough. In industrial environments, control is essential: AI can assist engineers, but engineers remain responsible for decisions. That is why the capabilities exposed to agents must be explicit and limited.

Delivered as a lightweight, configurable, and supported add-on for Capella Desktop, AI for Capella will enable organizations to connect their preferred AI agents while benefiting from a secure, maintainable, and enterprise-ready integration.

<figure>
    <a href="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-for-capella.png">
      <img src="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-for-capella.png" alt="AI for Capella">
    </a>
</figure>

## Stay tuned!

This first release planned for the **end of July 2026** will establish the foundation of our broader **AI for Capella** roadmap and the future AI-assisted capabilities we plan to introduce over time.

We are still at the beginning of this journey, and the most useful capabilities will not come from technology alone. They will come from a close understanding of real engineering practices, deployment constraints, security expectations, and the level of trust required by industrial teams.

If these questions resonate with your own MBSE initiatives, we would be glad to exchange with you, share what we are building, and gather feedback on the first AI for Capella capabilities.

Feel free to [contact us](https://www.obeosoft.com/en/contact/) to continue the conversation.
