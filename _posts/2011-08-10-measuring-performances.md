---
layout: post
title: "Measuring Performances"
date: '2011-08-10T01:26:00.000-07:00'
categories: [eclipse]
tags:
  - performance
  - obeo
  - emf compare
  - eclipse
modified_time: '2011-08-10T04:57:50.981-07:00'
thumbnail: https://3.bp.blogspot.com/-FdR-1a_XLBs/TkJTMoasu4I/AAAAAAAAAiM/FtGlBhOvdE4/s72-c/perfsingletest.png
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-1396678905777386614
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/08/measuring-performances.html
---

Performance is a feature — your users need it and so does your product. The code is changing, always; keeping track of the effect of those changes on performance is not easy but it is as important as fixing bugs.

You don't control what you don't measure. The Eclipse Platform built a performance measurement framework for their own needs. The API is pretty simple but the implementation, on the other hand, is quite complex (querying system-specific commands to retrieve the memory state depending on the platform). Launching a performance test built with this is not easy, neither is getting the result in a human-readable way.

Our needs were not as complex as the platform's ones. We're not trying to measure the number of microseconds a Shell needs to be instantiated on every platform; we're not trying to launch thousands of performance tests for each of our components.

We decided to write a small framework to measure performance. [Pierre-Charles](https://github.com/pcdavid) did the first iteration and I'm applying it on EMF Compare now. This framework uses JUnit4 annotations so that one can easily transform an end user scenario into a performance test. First warning: this framework is not suited for micro-benchmarking at all!

Second warning: this framework is not without overhead either. It fills an EMF model with the measures (which might take a bit of memory if you write thousands of tests).

On the other hand, the output of the test suite execution is this EMF model, allowing us to quite easily browse the results, generate reports, and even more interestingly to compare two snapshots! It's completely standalone and does not require more than Java, JUnit, and the EMF Core Runtime.

In a nutshell, this framework is convenient if you want to measure tasks in the order of seconds, and memory usage if you're looking at megabytes.

So far it's giving you memory usage (through JMX) and system time for each test; it runs the tests several times with a "warmup" phase launching the test but not measuring.

A test looks like this:

![Single test]({{ site.url }}/images/blog/2011/measuring-performances/s400_perfsingletest.png)

The test class:

![Test class]({{ site.url }}/images/blog/2011/measuring-performances/s400_perftestclass.png)

And the test suite:

![Test suite]({{ site.url }}/images/blog/2011/measuring-performances/s400_perfsuite.png)

It's here if you want to give it a try — it's EPL, it's on GitHub, feel free to fork it: https://github.com/Obeo/fr.obeo.performance

