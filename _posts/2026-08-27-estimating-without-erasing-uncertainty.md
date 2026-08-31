---
layout: post
title: "Estimating Without Erasing Uncertainty"
seoTitle: "Three-Point Estimation: Accounting for Uncertainty in Software Projects"
categories:
  - obeo
tags:
  - obeo
  - software-engineering
  - agile
lang: en
permalink: /obeo/three-point-estimation-software-project-uncertainty/
translation_fr: /obeo/estimation-trois-points-incertitude-projet-logiciel/
excerpt: "A practical account of three-point estimation for developers and project leaders who need to estimate effort without hiding uncertainty behind a single number."
---

> This article was automatically translated from the original French version.

For a long time, I thought a good estimate was a precise number. If someone answered “between three and six months,” I tended to feel they were dodging the question. Three months and six months are not remotely the same thing.

And in software, this question comes up all the time. You are a developer, a need emerges, and someone asks: “How long will it take to build this?”


<figure>
    <a href="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_1.png"><img src="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_1.png"></a>
    <figcaption>A point hides a range</figcaption>
</figure>


## When “two hours” meant “a first demo”

At [Obeo](https://www.obeosoft.com/en/company/), our journey with estimation was something of an initiation. In the early days, there were fewer than ten of us, working on the foundations of what would become [Eclipse Sirius](https://eclipse.dev/sirius/). I was a developer then, working directly with the customer. We would discuss their situation, a need would emerge, and then came the inevitable question:

> How long will it take to do that?

“Oh, I’d say two hours.”

If you have spent any time in software development, you can probably see where this is going: straight into a wall.

My “two hours” was roughly the time I needed to get a first version running on my machine. It did not include every edge case, automated tests, documentation, or the customer feedback that would arrive after delivery. In other words, it was the time I needed before you could stand next to me and watch something that “almost worked.”

Except that everything left after that “almost” takes at least as much time, and often much more.

<figure>
    <a href="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_2.png"><img src="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_2.png"></a>
    <figcaption>When two hours meant a first demo</figcaption>
</figure>

Some of the early Sirius releases were painful. The date was fixed, the scope was fixed, and both were based on our estimates. When delivery day came around, almost everything was there, but nothing was completely finished. We had our share of deliveries that ended at three in the morning, or later.

I described the context of those early years in [Obeo Turns 10]({{ site.url }}/obeo/ten-years/).

We had to relearn how to estimate a feature or a bug fix from the ground up: include the time needed for documentation, tests, integration, and customer feedback after delivery. It seems fairly obvious today, but it was not necessarily obvious at the time.

There is another lesson hiding in there: when your estimates suddenly double because you have finally started counting all the work, while your customers are used to the old numbers, managing that change becomes a challenge in its own right.

I digress. Well, not entirely. This already illustrates a first principle: estimating a task properly requires clear boundaries and a realistic understanding of everything it contains.

## A number quickly becomes a commitment

But even after learning that lesson, another problem remained: we still gave **one number**.

Consider a series of small tasks. For each one, choosing “half a day” rather than “one day” will produce a very different project total. Yet each individual task may genuinely take half a day, a full day, or sometimes more.

And when you ask a developer to choose one number, that number immediately becomes a form of commitment.

“How long?”

“One day.”

Fine. One day.

All the uncertainty that was still present in that person’s mind a few seconds earlier has just disappeared.

So I started looking for other approaches. I explored velocity and agile points, and especially Joel Spolsky’s [Evidence-Based Scheduling](https://www.joelonsoftware.com/2007/10/26/evidence-based-scheduling/), which appealed to me because of its scientific grounding. The idea is to use observed differences between estimates and actual delivery times to build a probability distribution of possible dates.

The problem is that it requires extremely detailed tracking. I never found that particularly realistic to implement at Obeo, nor especially desirable.

## Adding every risk does not work either

For customer proposals, we then introduced something else: an effort estimate accompanied by a separate “risk” figure, representing the number of additional days the task might require.

There was one genuinely good thing about this: we were finally discussing risk explicitly.

But there was a downside too. Some proposals became far too expensive simply because we had added every risk together. Commercially, we would sometimes reduce the estimate on the assumption that Obeo could absorb part of the risk. That is a valid decision, of course, but it has an awkward consequence: the commercial proposal starts to diverge from what we genuinely believe the project will require.

That is not very satisfying.

This approach had another perverse effect: exploratory work automatically became much more expensive because, by definition, it involved more uncertainty.

At Obeo, we rather like exploratory work. Those projects often help us learn, push our technologies further, and make them more mature. If every project capable of advancing a technology is penalized because it is uncertain, and therefore priced very high, everyone eventually loses.

That ability to explore while remaining accountable for the outcome is still central to [Obeo’s custom development work](https://www.obeosoft.com/en/services/custom-development/). It also connects to a broader question I discuss in my guide to [industrial open source]({{ site.url }}/open-source-industrial/): how do we fund learning, maintenance, and the maturation of shared technology without making a single project carry all the risk?

And I have not even mentioned the time spent producing extremely detailed estimates in the hope of reducing the margin of error. It is a great deal of work, and usually unpaid work.

That is where my perspective gradually changed. I still believe commitment is necessary. Precision at this level of granularity is much less so.

Perhaps the problem was not finding **the right number**. Perhaps the problem was insisting on giving only one.

## Three numbers instead of one

I started looking for established practices that genuinely accounted for uncertainty and had real mathematics behind them. After all, we know how to reason with probabilities. That is how I came across [three-point estimation](https://en.wikipedia.org/wiki/Three-point_estimation).

The principle is simple: instead of giving one value for each task, you give three—the most likely value, a high value, and a low value.

For a development task, this maps quite naturally to the conversation already happening in your head:

> Normally, this will take me one day. But it depends on a part of the framework I do not know very well, and it might not do everything I need, so it could take up to two and a half days. And I know I cannot do it in less than half a day.

I simply write it as:

**1 ~ 2.5 ~ 0.5**

Most likely, maximum, minimum.

From these estimates, we can perform calculations that are more robust than simple addition and obtain a project-level estimate that still carries the notion of uncertainty.

This was not the first time I had tried to make uncertainty something we could manipulate: I had already explored a Monte Carlo approach in [a probabilistic modeling prototype built with Sirius Web]({{ site.url }}/modeling/guesstimate-probability-modeling/).

## What changes at project level

Consider this example:

| Task | Effort | Risk | Three-point estimate |
| --- | ---: | ---: | ---: |
| T1 | 5 | 2 | 5 ~ 7 ~ 4 |
| T2 | 3 | 0 | 3 ~ 3 ~ 3 |
| T3 | 4 | 4 | 4 ~ 8 ~ 4 |
| T4 | 1 | 1 | 1 ~ 2 ~ 1 |
| T5 | 1 | 0 | 1 ~ 1 ~ 1 |
| T6 | 10 | 3 | 10 ~ 13 ~ 8 |
| T7 | 5 | 1 | 5 ~ 6 ~ 4 |
| T8 | 6 | — | 6 ~ 6 ~ 3 |
| T9 | 8 | 4 | 8 ~ 12 ~ 7 |
| T10 | 3 | — | 3 ~ 3 ~ 3 |
| **Total** | **46** | **15** | **47.17 ~ 50.31 ~ 44.02** |
| **Effort + risks** | **61** |  | **≈ 50** |


<figure>
    <a href="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_3.png"><img src="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_3.png"></a>
    <figcaption>61 days vs three-point estimation</figcaption>
</figure>



With our old method, we had 46 days of effort and 15 days of risk. Adding them together gave us 61 days.

With three-point estimation, the expected value remains very close to our initial estimate. It is slightly higher because it accounts for the uncertainty of the individual tasks. The upper bound of the interval is around 50 days, far below the 61 days produced by simply adding every risk.

And that makes sense. Reaching 61 days would require every identified risk to materialize at its maximum at the same time.

In this example, the spreadsheet uses the PERT approximation. For each task, the expected value is `(minimum + 4 × most likely + maximum) / 6`, and the standard deviation is `(maximum - minimum) / 6`. The variances of the tasks are then added—assuming their uncertainties are independent—to produce an interval of roughly 95% around the expected total (`± 2 standard deviations`). **The values 44.02 and 50.31 are therefore not the project’s absolute minimum and maximum, but the bounds of that interval.**

With three numbers—most likely, minimum, and maximum—we have something that supports better decisions. We know where we genuinely expect to land, we have a plausible interval, and, most importantly, we have an indication of the uncertainty of the project itself.

The difference is already significant across ten tasks. When estimating multi-year development projects, it can become massive.

## The calculation helps; the conversation helps even more

There is another benefit that I find almost more valuable than the calculation itself: it completely changes the nature of the conversation.

When you ask someone to “give me a number,” it quickly feels like a bet they are being forced to make. Once given, that number looks like a commitment.

When you ask for a three-point range, the conversation is different. “How long should this normally take? What could make the task overrun? By how much? And conversely, what is the lower bound you know you cannot beat?”

You start discussing not only what you know, but also what you do not know.

That information is valuable.

Once the project has been won and started, the estimate continues to carry that information for the people who will actually do the work. **1 ~ 2.5 ~ 0.5** does not merely mean “someone expected one day.” It also means: “this person thought one day was the most likely scenario, but they had identified an uncertainty that could push the task up to two and a half days.”

I have focused here on effort and development tasks, but the same method works just as well for financial projections.

That is ultimately what I learned: when looking into the future, a single number is hard to produce and carries very little information. Three numbers are often much easier to provide, and much richer.

For a long time, I associated the quality of an estimate with its precision. Today, I am more inclined to distrust an estimate that does not reveal its uncertainty.

So my toolbox now includes a few LibreOffice files with the macros needed to manipulate these figures easily.

You can download the file used for this example here: [Estimation_Charges_3Points.ods]({{ site.url }}/posts/files/Estimation_Charges_3Points_E95-2026-v1.3.ods).

> The workbook contains LibreOffice Basic macros. LibreOffice may therefore ask you to authorize them when opening the file.
