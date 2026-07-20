---
layout: page
title: "Making open source durable for industry"
seoTitle: "Industrial open source: governance, funding, and trust"
description: "A decision guide to the governance, funding, maintenance, security, and reversibility that turn open-source software into durable industrial infrastructure."
permalink: /open-source-industrial/
canonical: https://cedric.brun.io/open-source-industrial/
lang: en
translation_fr: /fr/open-source-industrial/
tags:
  - obeo
  - mbse
  - sirius-web
  - capella
cluster: open-source-industrial
intent: "Assess whether an open-source project can become dependable industrial infrastructure"
primaryQuery: "industrial open source"
secondaryQueries:
  - "open source governance"
  - "sustainable open source business model"
  - "open source vendor lock-in"
  - "Eclipse Foundation governance"
  - "Cyber Resilience Act open source"
audience: "Engineering executives, product leaders, architects, procurement teams, and organizations depending on strategic open-source software"
maturityStage: "evaluation and operating-model design"
pagePromise: "Provide a practical framework for evaluating and sustaining open-source software used in long-lived industrial systems"
proof:
  - "twenty years building and maintaining Eclipse open-source projects"
  - "industrial adoption of modeling technologies including Sirius, Capella, and SysON"
  - "experience aligning community projects with commercial products and services"
businessGoal: "Establish a stable reference point for the industrial open-source and Eclipse governance content cluster"
nextStep:
  - "/on-being-open-and-transparent/"
  - "/obeo/ten-years/"
  - "/talk/ocx-open-innovation/"
image:
  thumb: blog/2026/open-source-industrial/open-innovation-industrial-ecosystem.webp
---

Publishing source code under an open-source license is an important decision. It is not, by itself, an industrial strategy.

Industry does not depend on a repository. It depends on software that can be understood, maintained, secured, integrated, upgraded, and supported over many years. It also depends on people and organizations able to make decisions when priorities conflict or when the original team moves on.

This is where many discussions about open source go wrong. They compare license costs, feature lists, or access to code. The more useful question is: **what makes this software dependable beyond the current vendor, project team, and budget cycle?**

After twenty years of building products and services around Eclipse technologies, my answer is that durable industrial open source rests on six connected foundations:

- a useful product and a technically healthy project;
- explicit, transparent governance;
- sustained maintenance and security work;
- an economic model that funds this work;
- an ecosystem in which several actors can participate;
- practical exit options for adopters.

Remove any one of these and openness may remain legally true while becoming operationally irrelevant.

<figure>
    <a href="{{ site.url }}/images/blog/2026/open-source-industrial/open-innovation-industrial-ecosystem.webp">
      <img src="{{ site.url }}/images/blog/2026/open-source-industrial/open-innovation-industrial-ecosystem.webp" alt="Presentation at OCX 2024 showing the positive feedback loop between industrial investment, upstream maintenance, adoption, education, and commercial services">
    </a>
    <figcaption>At OCX 2024, I represented industrial open source as a positive feedback loop: investment maintains the common technology, broader adoption creates opportunities, and those opportunities fund further work.</figcaption>
</figure>

## What does industrial open source mean?

"Industrial" does not mean that every project must look like a large commercial product. It means that organizations can make consequential, long-term commitments around it with a clear understanding of the risks.

For a software component or engineering tool, that usually requires:

- documented releases and compatibility expectations;
- repeatable builds and controlled dependencies;
- maintainers with the time and authority to review contributions;
- a vulnerability-reporting and remediation process;
- traceable intellectual property and licensing;
- migration paths for data, APIs, and extensions;
- support or expertise that can be contracted when needed;
- governance that remains understandable when organizations disagree;
- evidence that knowledge is not concentrated in one unavailable person.

These properties are not produced by the license. They are produced by repeated work.

An open-source project can be innovative, popular, and still be a poor foundation for a ten-year industrial program. Conversely, a modest project with a focused community, predictable stewardship, and committed adopters can be a dependable strategic asset.

## Separate the project, product, and service

Discussions become clearer when three layers are distinguished.

The **open-source project** is the shared technical commons: source code, issues, releases, contribution process, public decisions, and community. Its governance determines who can influence it and how.

A **product** packages capabilities for a defined group of users. It may add installation, administration, integrations, tested configurations, long-term support, certifications, or features that are not part of the common project.

A **service** supplies expertise and accountability: support, training, architecture, migration, customization, operations, or sponsored development.

These layers can be delivered by one organization or several. Their boundaries vary by ecosystem. What matters is that adopters understand them. A public repository should not be used to imply a level of productization or support that does not exist. A commercial offer should not obscure which improvements are shared upstream and which create a vendor-specific dependency.

At Obeo, the connection between these layers has been central from the beginning. As I wrote when [Obeo turned ten]({{ site.url }}/obeo/ten-years/), the success of our open-source technologies and our capacity to work within their communities became a key factor in the success of our commercial products. The relationship works when commercial activity strengthens the shared foundation and the shared foundation expands what products and services can achieve.

## Governance is the operating system of the community

Governance answers questions that a license leaves open:

- Who decides whether a contribution is accepted?
- How is technical authority earned?
- Where are roadmap decisions discussed?
- What happens when two employers want different outcomes?
- Who can make a release or manage a vulnerability?
- How can a new organization gain meaningful influence?
- What happens if the principal contributor withdraws?

A mature governance model makes these answers public and predictable. It does not eliminate disagreement. It gives disagreement a legitimate place to be resolved.

At Eclipse, projects operate under open, transparent, and meritocratic rules. Committer status is earned through contribution and peer election rather than granted automatically by an employer. The [Eclipse Project Handbook](https://www.eclipse.org/projects/handbook/) also defines project roles, reviews, intellectual-property due diligence, public resources, and the project lifecycle.

This does not magically create a diverse community. A project may still rely heavily on one company, especially at the beginning. The important thing is to be honest about that concentration and to provide a credible path for others to participate. **Vendor-neutral governance is a possibility created by rules; diversity is an outcome created by sustained participation.**

Good governance is also lightweight enough for work to happen. Requiring a committee decision for every change is not maturity. Clear scope, delegated technical authority, public review, and an escalation path are usually more useful than ceremonial control.

## Why put a project in a foundation?

A neutral foundation makes the shared part of an ecosystem more credible. It can hold project assets and trademarks, define common rules, manage contributor and intellectual-property processes, provide infrastructure, support security practices, and arbitrate when project governance fails.

This institutional continuity matters when several organizations want to cooperate on technology that none of them should unilaterally control. The foundation creates a place where competitors can contribute under the same rules and where adopters can distinguish the project from the commercial strategy of one supplier.

The [Eclipse Development Process](https://www.eclipse.org/projects/dev_process/) goes further by requiring practices intended to keep a project viable independently of any single individual, organization, or external service. This is directly relevant to industrial risk.

However, a foundation is not an outsourced product team. It cannot invent user demand, finance every maintainer, define a coherent roadmap, or replace technical leadership. It provides legal, governance, and collaboration infrastructure. Project participants still have to do the engineering and community work.

The question is therefore not simply, "Is this project in a foundation?" Ask instead:

- Which assets and processes are actually governed there?
- Are technical discussions and project plans public?
- Are releases produced through foundation-managed processes?
- Can contributors from another employer become committers?
- Is there active oversight when a project becomes inactive or unsafe?
- Who currently pays for the maintainers' time?

Foundation hosting is a strong signal when these mechanisms are real. A logo alone is not.

## Maintenance must be funded

Open source changes who can inspect, use, modify, and redistribute software. It does not make engineering free.

Maintenance includes reviewing issues, reproducing failures, updating dependencies, improving documentation, answering contributors, running releases, migrating infrastructure, responding to vulnerabilities, and preserving compatibility. Much of this work is invisible when it succeeds. That makes it easy to value new features while treating maintenance as overhead.

A sustainable economic model makes the beneficiaries of the software fund enough of this common work. Common patterns include:

- [support and maintenance subscriptions](https://www.obeosoft.com/en/services/support-maintenance/);
- enterprise distributions or complementary products;
- managed hosting and operations;
- consulting, integration, migration, and training;
- [sponsored development of roadmap items](https://www.obeosoft.com/en/services/custom-development/);
- consortium or working-group membership;
- joint investment by organizations sharing the same infrastructure;
- public or research funding for defined outcomes.

No single pattern is universally best. A project used as a library has different economics from a collaborative engineering environment. A small developer tool has different obligations from software embedded in regulated products.

The critical test is whether revenue-producing activity and project health reinforce each other. If commercial work systematically creates private forks, bypasses upstream review, or consumes maintainers without funding them, the model accumulates debt. If paid work improves shared foundations, develops skills, and creates more capable adopters and suppliers, it can produce a positive loop.

Free riders are not necessarily a failure. Low-friction adoption is one of open source's advantages. The business model should be designed on the assumption that many users will never pay, while organizations needing assurance, influence, integration, or accountability will finance professional work.

## Sustainability is visible in ordinary engineering work

Project health is easier to judge through evidence than declarations. Look at the last year of activity:

- Are releases regular enough for the domain?
- Are pull requests reviewed by more than one person?
- Are issue and roadmap decisions explained publicly?
- Can a new contributor build the software from documented instructions?
- Are dependencies, release artifacts, and licenses traceable?
- Is there a supported-version policy?
- Are security contacts and disclosure procedures easy to find?
- Are migrations and breaking changes documented?
- Does the project test realistic integrations and upgrade paths?
- Is knowledge distributed across people and organizations?

My 2013 article [On being open and transparent]({{ site.url }}/on-being-open-and-transparent/) made a similar point from the contributor side. A visible repository is not enough. Reproducible builds, contribution guidance, public review, continuous integration, documentation, engagement, and predictable plans determine whether outsiders can genuinely participate. More than 10 years later, it still holds true.

There is also an uncomfortable but necessary question: who will maintain a major contribution after it is merged? Accepting code without a plausible maintenance path can make a project less sustainable, not more. Contribution volume is not the same as project capacity.

## Open source improves sovereignty, but does not guarantee it

Open source is a powerful component of technological sovereignty because it creates rights that proprietary licensing does not: inspection, modification, redistribution, and the ability to continue the software independently.

But sovereignty is an operational capability, not a license checkbox. An organization is not meaningfully autonomous if it has the source code but cannot build it, understand its architecture, migrate its data, operate the infrastructure, or find anyone besides the incumbent vendor with the necessary skills.

Evaluate practical control across several dimensions:

- **code:** can the complete relevant system be built from available sources?
- **data:** are formats and export paths documented and usable at scale?
- **operations:** can the software be deployed and monitored in the required environment?
- **skills:** can expertise be developed internally or sourced from several providers?
- **governance:** can the organization contribute, influence priorities, or maintain a fork if necessary?
- **dependencies:** do critical hosted services, proprietary extensions, or external APIs recreate lock-in elsewhere?

Open source does not remove supplier dependence. It changes its nature and gives adopters more leverage. A good supplier remains valuable because of expertise, responsiveness, product quality, and accumulated trust, not because leaving is technically or legally impossible.

The objective should not be "zero dependency." Complex engineering always depends on people and organizations. The objective is **dependency with visibility, influence, and credible alternatives**.

## Security and the Cyber Resilience Act raise the bar

Security makes the distinction between code availability and stewardship especially clear. Industrial adopters need to know who receives vulnerability reports, which versions are supported, how patches are coordinated, and how component information flows into the products that incorporate the software.

The EU Cyber Resilience Act (CRA) formalizes part of this responsibility for products with digital elements. It entered into force on 10 December 2024. Reporting obligations apply from 11 September 2026, and the main provisions apply from 11 December 2027, according to the [European Commission's implementation timeline](https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation).

The Act deliberately distinguishes roles. Free and open-source software developed or supplied outside a commercial activity is treated differently from a product placed on the market by a manufacturer. It also introduces the role of an **open-source software steward** for legal persons that systematically support, on a sustained basis, open-source products intended for commercial activities without placing those products on the market themselves. The Commission provides a useful [summary of the CRA's open-source provisions](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source).

This is not a reason to treat all community projects as product manufacturers, nor to assume that publishing under an open-source license removes commercial responsibilities. Organizations have to identify their actual role in the supply chain and obtain appropriate legal guidance.

Operationally, the direction is already clear: vulnerability handling, supported versions, dependency knowledge, provenance, security documentation, and coordination between upstream projects and downstream products can no longer be improvised after an incident.

This is also a case where collaboration is more efficient than every project interpreting regulation alone. The [Eclipse Open Regulatory Compliance Working Group](https://projects.eclipse.org/working-group/eclipse-open-regulatory-compliance-working-group) brings together foundations, industry, SMEs, and research actors to develop shared practices and compliance resources. I encountered this work directly at [OCX 2024]({{ site.url }}/eclipse/ocx-open-community-experience-2024/), where the CRA was a central topic across project, foundation, and industry discussions.

## Cooperation does not eliminate competition

Industrial open source works when organizations agree on what should be common and retain room to differentiate above it.

They may cooperate on a language implementation, a modeling framework, interoperability, security processes, or shared infrastructure. They can still compete through domain expertise, user experience, integrations, deployment, services, support commitments, and delivery quality.

This boundary is strategically useful. Reimplementing the same foundation in private gives every participant a cost but rarely gives users a meaningful advantage. Pooling that work can move competition toward the parts customers actually value.

It also creates an environment for learning. Engineers can discuss architecture with peers, companies can influence technologies they depend on, researchers can experiment on a production-relevant base, and users can bring needs closer to maintainers. In my [interview with Federico Tomassetti]({{ site.url }}/interview/interview-strumenta/), I described how clear Eclipse rules make it possible to collaborate on common technology while remaining commercial competitors.

This balance requires discipline. Shared governance should not become a channel for coordinating markets, and a common roadmap should not become a promise that every participant's priorities will be funded. Foundations provide antitrust policies and collaboration structures precisely because industrial cooperation needs explicit boundaries.

## A decision checklist for adopters

Before making an open-source component or tool strategic, ask for evidence in six areas.

### Product and technical fit

- Does it solve the real use case with acceptable performance and usability?
- Are architecture, extension points, data formats, and dependencies documented?
- Is there a credible upgrade and migration path?

### Project health

- Who are the active maintainers, and how is their time funded?
- How regular are releases, reviews, and community decisions?
- Could a competent new organization build and contribute to the project?

### Governance

- Who owns the project assets and trademarks?
- How are committers selected and disputes resolved?
- Can several organizations gain meaningful technical authority?

### Security and compliance

- Which versions receive security fixes, and for how long?
- Is there a private vulnerability-reporting path and a public policy?
- What provenance, dependency, and release evidence is available?
- Which CRA or sector-specific role will each organization occupy?

### Economics and support

- Which commercial or collective mechanisms finance maintenance?
- Can support and expertise be contracted at the required service level?
- Does paid work strengthen upstream software or create a private divergence?

### Reversibility

- Can you export your data and operate the software independently?
- Are alternative providers or internal skill-building realistic?
- What would a maintained fork cost if governance or strategy diverged?

No project will score perfectly. The checklist makes trade-offs visible. A young project may be acceptable for experimentation and inappropriate for a critical program. A concentrated project may still be a sound choice when the principal vendor is transparent, well funded, and actively creates paths for other participants.

## The durable asset is the ecosystem

Open source is sometimes presented as a choice between community idealism and commercial discipline. Industrial experience points in another direction. The strongest ecosystems combine public rules, serious engineering, paid work, and room for several actors to create value.

The source code matters because it establishes durable rights. Governance turns those rights into influence. Maintenance turns them into usable software. Funding gives maintenance continuity. A foundation gives collaboration an institutional home. A diverse ecosystem gives adopters alternatives and gives the technology more paths to survive.

That is the real promise of industrial open source: not software without suppliers, costs, or responsibilities, but strategic infrastructure whose dependencies can be understood, influenced, and shared.
