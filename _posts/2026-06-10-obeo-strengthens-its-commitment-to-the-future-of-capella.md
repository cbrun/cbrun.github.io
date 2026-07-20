---
layout: post
title: "Obeo Strengthens Its Commitment to the Future of Capella"
categories:
  - modeling
tags:
  - capella
  - mbse
  - obeo
  - sysmlv2
  - syson
  - ai
  - whatsnew
permalink: /mbse/obeo-strengthens-its-commitment-to-the-future-of-capella/
canonical: https://blog.obeosoft.com/obeo-strengthens-its-commitment-to-the-future-of-capella
excerpt: "An overview for the Capella and MBSE community of Obeo's new contributions to Capella, SysML v2 interoperability, simulation, AI, and Capella Days."
image:
  thumb: blog/2026/obeo-strengthens-its-commitment-to-the-future-of-capella/capella-jp.png
---

Originally developed by Thales, the [Capella tool](https://mbse-capella.org/) and the [Arcadia method](https://mbse-capella.org/arcadia.html) have established themselves as leading references in the open-source MBSE landscape.

Obeo has been part of this journey for many years. We have contributed to key technologies that support Capella, including Eclipse Sirius, EMF Services, GMF Runtime, and other Eclipse technologies.

Over time, our involvement has expanded beyond the platform itself to include add-on development, training, consulting and integration services, community support, and the organization of events that bring together Capella practitioners worldwide.

Today, I'm happy to share **several concrete milestones** that show how we are strengthening this commitment, with contributions to Capella itself, new open-source initiatives, ongoing work around SysML v2, simulation and AI, and the 10th edition of Capella Days.

There is a lot to share, so let me walk you through the main announcements.

## New Contributions and Improvements in Capella 7.1

At Obeo, we've been taking responsibility for several new developments within the Capella project and will keep doing so.

For years, we have contributed to several technologies that form part of Capella's foundation, including EMF Services, GMF Runtime and Eclipse Sirius. We are now extending this commitment higher in the stack, with **direct contributions to Capella itself**.

Our current focus is to reinforce the robustness, security and maintainability of the platform. One important step in that direction is the migration to Java 21.

We have also worked on enabling Capella's internationalization, making the platform more accessible to users worldwide.

As an illustration of this work, Siemens has already leveraged this capability to provide a Japanese version into the latest release of System Modeling Workbench (SMW).

<figure>
    <a href="{{ site.url }}/images/blog/2026/obeo-strengthens-its-commitment-to-the-future-of-capella/capella-jp.png">
      <img src="{{ site.url }}/images/blog/2026/obeo-strengthens-its-commitment-to-the-future-of-capella/capella-jp.png" alt="Japanese version of System Modeling Workbench using Capella internationalization">
    </a>
</figure>

These developments will be delivered in the upcoming Capella 7.1 release, scheduled for June.

This is not the most visible kind of work, but it is the kind of work that makes Capella stronger and more sustainable for everyone.

## Capella and SysMLv2 - An Arcadia Library

You probably already know that Obeo has been investing a lot in SysML v2 over the last few years, in particular through Eclipse SysON, our open-source web-based graphical modeling tool for SysML v2.

At the same time, we strongly believe in Capella and Arcadia. For us, **the convergence between Capella, Arcadia and SysML v2 is a major opportunity for the future of open MBSE**.

Together with Thales, we worked on establishing an Arcadia library for SysML v2. This library has now been published in the [project repository](https://github.com/eclipse-capella/arcadia-sysmlv2-lib). It is a first, foundational step toward interoperability between Capella and SysML v2 models, and it opens the path toward automated transformations.

This is still an early basis, but our goal is to extend it progressively and cover more of Capella.

Our goal is simple: make Capella and SysML v2 work better together, without losing what makes Arcadia and Capella so valuable today.

## Simulink® Add-On Now Open Source

In parallel, with Thales we have jointly **open-sourced the Simulink add-on** for Capella.

This add-on enables the simulation of Capella models through integration with Simulink, helping bridge system architecture and simulation activitie

<figure>
    <a href="{{ site.url }}/images/blog/2026/obeo-strengthens-its-commitment-to-the-future-of-capella/bridge-simulink.png">
      <img src="{{ site.url }}/images/blog/2026/obeo-strengthens-its-commitment-to-the-future-of-capella/bridge-simulink.png" alt="Capella Simulink add-on for architecture and simulation workflows">
    </a>
</figure>

Thanks to this add-on, engineers can check their assumptions with Simulink and make sure their architecture design matches simulation constraints. Simulation engineers can focus on higher-value tasks, with better confidence that simulation scenarios remain consistent with the system design.

By opening this component with Thales, we want to make it easier for the community to use it, improve it, and build new architecture-to-simulation workflows around Capella.

The add-on is now fully open source under the Eclipse Public License, and the [code is available here](https://github.com/eclipse-capella/capella-simulink-connector).

If your organization wants to contribute improvements to this project, feel free to reach out to us. We would be happy to explore [an open-innovation collaboration](https://www.obeosoft.com/en/company/open-innovation/).

By opening this add-on, we hope to make advanced architecture-to-simulation workflows easier to share, improve and adopt across the community.

## Agentic AI and Capella

Even in a relatively conservative domain like engineering, our experiments show that **AI agents can already be useful**. They bring a whole new way to interact with modeling tools and can contribute to use cases such as:

- Onboarding ("How do I start?"),
- Understanding ("What does this component mean?"),
- Tool guidance ("How do I perform this task?"),
- Consistency ("Is the model coherent?"),
- Impact Analysis ("What happens if this requirement changes?"),
- Automation ("How can I inject the content from my existing products?"),
- Querying ("How can I ask the model?").

There are many opportunities to simplify workflows, improve productivity and make MBSE more accessible. Yet using such agents in an engineering context, and even more in a systems engineering context, requires special care: we need to set up a controlled collaboration between the engineer and the agent.

<figure>
    <a href="{{ site.url }}/images/blog/2026/obeo-strengthens-its-commitment-to-the-future-of-capella/capella-ai.png">
      <img src="{{ site.url }}/images/blog/2026/obeo-strengthens-its-commitment-to-the-future-of-capella/capella-ai.png" alt="Agentic AI integration with Capella modeling workflows">
    </a>
</figure>

We've been developing integrations with Capella in the last few months and I'm quite excited that we are at a point where we can share results.

Stay tuned for an **upcoming webinar on this topic in September**. During this session, Stéphane Lacrampe will present the latest results of our ongoing work to bring new AI-driven capabilities and value to Capella users.

Used with the right level of control, AI agents can make Capella easier to learn, easier to query and easier to use on real engineering problems.

## Celebrating the 10th Edition of Capella Days

Before closing, I'd like to highlight another important milestone for the Capella community.

From **December 1 to 3, 2026**, we will host the 10th edition of Capella Days. Reaching a tenth edition is a remarkable achievement and a testament to the vitality of the Capella ecosystem and the commitment of its users, contributors, and partners around the world.

<figure>
    <a href="{{ site.url }}/images/blog/2026/obeo-strengthens-its-commitment-to-the-future-of-capella/capella-days-2026.png">
      <img src="{{ site.url }}/images/blog/2026/obeo-strengthens-its-commitment-to-the-future-of-capella/capella-days-2026.png" alt="Logo for the 10th edition of Capella Days in 2026">
    </a>
</figure>

Over the years, Capella Days has become the flagship event for sharing experiences, presenting innovations, and discussing the future of MBSE with Capella and Arcadia. This anniversary edition will be an opportunity to look back on the journey so far while exploring the next chapter of the ecosystem.

The [Call for Papers is now open](https://tinyurl.com/capelladays2026cfp) and will remain open **until September 6**. To encourage early submissions and help shape the program, a first selection of talks will be announced starting on August 16.

[Registration](https://www.bigmarker.com/series/capella-days-2026/series_summit?utm_bmcr_source=obeo_blog_cbr) is also already open, allowing participants to secure their place and start planning for this special edition.

Whether you are a Capella practitioner, researcher, tool developer, or systems engineering leader, we encourage you to submit your proposal and join us in celebrating this important milestone for the community.

Learn more, register, and submit your proposal on the [Capella Days page](https://mbse-capella.org/capella_days_2026.html).

This tenth edition will be a great opportunity to celebrate what the community has achieved together and to discuss where open MBSE is heading next.

## A Stronger Future for Open MBSE

All these initiatives go in the same direction: making open MBSE more robust, more connected and more accessible for industrial use.

We have been relatively quiet about some of this work so far. That probably says something about our "doing first, showing then" culture at Obeo. But I'm really glad we are now at a point where we can share concrete results and invite the community to build on them with us.

Obeo will continue to invest in Capella and in an open, industrial-grade and future-oriented MBSE ecosystem. I'm looking forward to continuing this journey with the Capella community.
