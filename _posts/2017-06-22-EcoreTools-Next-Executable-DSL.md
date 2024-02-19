---
layout: post
title: "EcoreTools-Next: Executable DSL made (more) accessible"
categories: [talk]
tags: [emf, ecoretools, executable, simulation, dsl, xtext]
---
Hello there! I'm Cédric Brun, CTO at Obeo, and I'm excited to talk at the next EclipseCon France about making Executable Domain-Specific Languages (DSLs) more accessible through our latest innovation: ALE (Action Language for EMF), integrated into Ecore Tools.

Our journey begins with the challenge of adding execution capabilities to DSLs. Traditional methods are complex, involving modification or configuration of generated code, delegation mechanisms, or model transformations. This complexity hinders rapid iteration and optimal solutions.

Enter ALE – our solution to simplify and expedite DSL execution. ALE allows you to annotate Ecore with runtime data and implement E operations, making it possible to define behavior outside the Ecore model. This separation of semantic and static data is crucial for flexibility and ease of use.

We've made sure ALE is intuitive, with a syntax close to OCL, enhanced by features like type inference in conditionals. Plus, it supports open classes, allowing you to add behavior to any class, even those not originally defined by you.

The coolest part? ALE is interpreted, not compiled, removing the need for complex classpaths or dependencies. This makes testing and iterating on your DSL as simple as running it directly in your environment.

Through our demos, you'll see how ALE enables the creation and execution of a finite state machine DSL from scratch, without the hassle of compiling and generating code. You'll witness the dynamic addition of behavior to Ecore models and the real-time execution of state machines.

Looking ahead, we're excited about the potential to run executions step-by-step and to explore the performance trade-offs between interpreting code with ALE and generating Java code.

Remember, we're still refining ALE, and your feedback is crucial for its evolution. And yes, while I’m presenting solo today, this is a team effort with the brilliant minds at the Diverse team and Rennes 1 University. 

So, brace yourselves for a dive into the world of executable DSLs with ALE – making the complex, accessible!

<iframe width="560" height="315" src="https://www.youtube.com/embed/x4viqEFN7PU?si=wPAzy9LR7ODHaxNp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

[EcoreTools-Next: Executable DSL made (more) accessible](https://cedric.brun.io/talks/EclipseConFR2017/ALE_talk.pdf) at EclipseCon France 2017, Toulouse  [video](https://www.youtube.com/watch?v=x4viqEFN7PU)

Here are five key questions answered in the talk:

**Does the behavior work for enums or enumerations?**
   - Answer: Yes, AQL works perfectly with enumerations. You can use existing enumerations in expressions without any problem. While you can't add a method to an enumeration, you can define and override the behavior of existing operations or define a new operation in the AL file that takes the enumeration as a parameter.

**Can you talk about generating Java code in the perspective of deploying the behavior added to an income model?**
   - Answer: There's no need to generate Java code for deployment. You can deploy the behavior as is. To start with an action, you just load the AL file, which is part of your plugin.

**What are the available types when you begin to code?**
   - Answer: The available types are those that are part of Ecore, and all the data types in Ecore are supported by the AQL syntax. There's also the possibility to extend your AL file with Java services to add more functions into your language, allowing the use of your own data types.

**Is there a feature to run the execution step-by-step?**
   - Answer: Currently, the ability to run executions step-by-step is missing but is planned as the next addition. This feature is desired for better debugging and understanding the execution flow.

**What about the experiment of generating Java code and its performance comparison with AQL interpretation?**
   - Answer: There's an ongoing experiment to generate Java code to validate and compare its performance and use against AQL interpretation. This comparison will help understand the trade-offs, like whether being three or four times slower is acceptable or if it's significantly slower.
