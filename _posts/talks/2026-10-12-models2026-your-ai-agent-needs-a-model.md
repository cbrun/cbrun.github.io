---
layout: post
title: "Your AI Agent Needs a Model: Practical Examples from MODELS 2026"
categories:
  - talk
tags:
  - talk
  - modeling
  - capella
  - mbse
  - arcadia
  - ai
  - sirius-web
  - syson
  - obeo
permalink: /talks/models-2026-your-ai-agent-needs-a-model/
excerpt: "Practical examples from MODELS 2026 of how systems engineers can use AI for Capella today to explore architectures, question designs, and prepare changes for review."
draft: true
talk:
  event: "MODELS 2026 Industry Day"
  location: "Málaga, Spain"
  slides: "/talks/Models2026/"
  image: "/images/blog/2026/models2026/title.png"
  image_alt: "Your AI agent needs a model: title slide from MODELS 2026 Industry Day."
---

I came back from [MODELS 2026](https://conf.researchr.org/home/models-2026) in Málaga with plenty to think about. Thank you to Lola and the organizing team for a great conference. Everything was so well organized, and it was a pleasure to catch up with people I have known in the academic modeling community for years, and to meet new people getting involved.

I was particularly happy to see so many people at Industry Day. My presentation, **“Your AI Agent Needs a Model,”** led to many interesting questions. I had brought a few practical examples of what systems engineers can do with AI and models **right now**.

<figure>
    <a href="{{ site.url }}/talks/Models2026/">
      <img src="{{ site.url }}/images/blog/2026/models2026/title.png" alt="Your AI agent needs a model: Cédric Brun, Obeo, at MODELS 2026 Industry Day in Málaga." width="1600" height="900">
    </a>
    <figcaption>Your AI agent needs a model. Click to explore the slides and recorded demonstrations.</figcaption>
</figure>

At [Obeo](https://www.obeosoft.com/en/), we have been exploring these interactions across our modeling tools. For this talk, I focused on [Capella](https://mbse-capella.org/), a mature environment with an established engineering method. [AI for Capella](https://www.obeosoft.com/en/products/ai-for-capella/) is our commercial add-on connecting it to AI agents through MCP, the Model Context Protocol. It is available today.

In June, I wrote about [making Capella accessible to AI agents]({{ site.url }}/mbse/ai-for-capella-agentic-ai-as-a-first-step/). This time, I wanted to show what engineers can actually ask them to do.

## Where does the trace stop?

The first example starts with a simple request: trace a mission in Capella's in-flight entertainment example down to the equipment that supports it.

The agent follows functions, their allocation to components, and the relationships between architectural levels. It also reports where information is missing: unfinished scenarios and functions it cannot trace down to equipment.

That is useful. An engineer gets a path to inspect, including the places where the model stops supporting an answer.

A model gives the agent relationships with engineering meaning. “This function is allocated to this component” connects what the system does to the part responsible for doing it. The effort spent making those relationships explicit becomes useful in another way: we can explore them by asking questions in everyday language.

## Can safety instructions still interrupt the game?

One of my favorite examples concerns the modes of a passenger's seat TV.

At the System Analysis level, the model describes a passenger playing a game and being interrupted by safety instructions. When the agent compares this with the Logical Architecture, it reports that the corresponding transition is missing.

The modes look similar. But has the intended behavior survived the refinement?

<figure>
    <a href="{{ site.url }}/talks/Models2026/#/consistency-result">
      <img src="{{ site.url }}/images/blog/2026/models2026/safety-transition.png" alt="Safety instructions can interrupt a game in System Analysis, but the corresponding transition is reported missing in Logical Architecture." width="1600" height="900" loading="lazy">
    </a>
    <figcaption>The agent reports a missing transition between architectural levels: a specific finding for an engineer to check.</figcaption>
</figure>

That is a very practical question for a model review. The agent points to a specific place where an engineer should look more closely. Other demonstrations follow the same idea: what depends on a processor if it fails, or whether the response to cabin decompression is described all the way down to the equipment.

These are findings to review. In a later correction sequence, the agent revises some of its conclusions and leaves issues unresolved. The useful workflow is to explore the model, question it, prepare changes, and check the result.

## A spreadsheet, an architecture, and 26 milliseconds

Another example starts outside Capella, with supplier data and targets for an Automatic Emergency Braking system in a spreadsheet.

I give the agent instructions about how to turn parts into components, derive functions, attach properties, and connect the architecture. One rule specifies which traffic must pass through the central gateway.

The agent builds the architecture in Capella. Then I ask it to check the design against the targets.

Its report says mass and power are within budget, but end-to-end latency is **146 ms against a target of 120 ms**. It also flags a controller below the requested safety integrity level.

<figure>
    <a href="{{ site.url }}/images/blog/2026/models2026/braking-architecture-results.jpg">
      <img src="{{ site.url }}/images/blog/2026/models2026/braking-architecture-results.jpg" alt="AI for Capella demonstration with the agent's latency report on the left, showing 146 ms against a 120 ms target, and the braking architecture in Capella on the right." width="1920" height="1080" loading="lazy">
    </a>
    <figcaption>The reported latency exceeds the target by 26 ms. The calculation and its assumptions are visible beside the model. <a href="{{ site.url }}/talks/Models2026/#/aeb-demo">Watch the demonstration.</a></figcaption>
</figure>

Now we have an engineering question: where could we recover those 26 milliseconds, and what else would that change affect?

The report distinguishes values read back from the model from information still taken from the spreadsheet. Some allocations remain manual. There is still work to do, but we have an architecture whose elements, values, and relationships an engineer can inspect and challenge.

## The method matters too

Those instructions are part of the engineering work. The agent needs to know what we expect, which constraints apply, and how we intend to check the result.

The [Arcadia method](https://mbse-capella.org/arcadia.html) provides guidance through the engineering stages. In another demonstration, a newcomer modeling an optical mouse asks where to start, then what to do next. The agent explains the available steps using the method and the model already built. I have written more about [how Capella and Arcadia fit together]({{ site.url }}/capella-arcadia/).

The same principles are being explored on the web. I showed a short demonstration of [Capella for SysON](https://blog.obeosoft.com/capella-for-syson), bringing Arcadia to [SysON](https://mbse-syson.org/) on a SysML v2 foundation. SysON is built on [Sirius Web](https://eclipse.dev/sirius/sirius-web.html). Capella for SysON is still an early project; the AI capabilities belong to Obeo's enterprise offering.

## Plenty left to explore together

I hope these examples give the research community something concrete to work with. We can already ask useful questions of engineering models using available tools. How do we make the answers more dependable? How should agents expose missing information, follow project conventions, and combine their suggestions with deterministic checks?

The limits are interesting too. In one experiment, generated requirements bundled several obligations together and omitted a measurable deadline. Access to the architecture alone did not tell the agent what a good requirement should look like.

Models give engineers and agents something shared to inspect, modify, and validate. There is plenty of research to do around how we use that common ground.

One conversation even led to another experiment. I met Susanne Göbel, who told me about her work on EMFular and KEML tooling. That scratched an itch: I couldn't resist trying to bring KEML to Sirius Web. The result is a [demonstration project](https://github.com/cbrun/keml-on-sirius), built from the existing Ecore model and EMF tooling. The original language and tools are developed by the [KEML project](https://github.com/keml-group). This is one of the things I enjoy about these conferences: a conversation gives you something new to try.

<figure>
    <a href="{{ site.url }}/images/blog/2026/models2026/keml-sirius-web.png">
      <img src="{{ site.url }}/images/blog/2026/models2026/keml-sirius-web.png" alt="KEML running in Sirius Web, with a conversation between an author, an LLM, and a browser represented alongside knowledge and argument links." width="2310" height="1565" loading="lazy">
    </a>
    <figcaption>A conference conversation turned into a <a href="https://github.com/cbrun/keml-on-sirius">Sirius Web experiment</a>, reusing the <a href="https://github.com/keml-group">KEML project's</a> Ecore model and EMF tooling.</figcaption>
</figure>

The [slides and recorded demonstrations are available here]({{ site.url }}/talks/Models2026/). Try these kinds of questions on your own models, challenge the results, and tell us what you find!
