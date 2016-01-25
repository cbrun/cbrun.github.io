---
layout: post
title:  Some news on the AQL front
categories: [upcoming]
---


The [Acceleo Query Language](https://www.eclipse.org/sirius/doc/specifier/general/Writing_Queries.html#aql) implementation has been [announced in August](http://cedric.brun.io/eclipse/introducing-aql/) and is the recommended interpreter starting 
with Sirius 3.1. As we prepare the Eclipse Mars.2 release I'd like to take a few minutes to share a few of the niceties AQL brings beside the raw performance. This is not an exhaustive list.


## A language extensible using Java Methods

The whole language execution semantic is defined through Java methods.

`aql:self.someMethod()`

When the `.` separator is used, the type of the current variable is used to retrieve the appropriate method.

Even the operators are actually mapped to a Java method, the following expression :

`aql:1+3`

will call the method "add":

{% highlight java%}
public Integer add(Integer a, Integer b) {
...
}
{% endhighlight %}

In the case of the `->`separator, the method is to be applied on the collection itself:

`aql:self.eContent()->size()`


This is all optionaly defined, so if you want to build your own query language with different choices for operators or the standard library you can fairly easily create an empty **query environment**: 

{% highlight java%}
IQueryEnvironment env = Query.newEnvironment(xRefProvider, rootProvider); // instead of Query.newEnvironmentWithDefaultServices(xRefProvider,rootProvider)

{% endhighlight %}

And then register your classes bringing these methods :

{% highlight java%}
env.registerServicePackage(YourOwnVersionOfEObjectService.class);

{% endhighlight %}


## 1<->1 mapping with Java classes

With AQL you are not limited to "returning the standard types the language no about".  This is especially useful when you want to return something which has a bit more structure than a primitive type.
Let's say you want to do a bit of statistic on your model. You can write a service like this, here making use of the Apache Common Math library :

{% highlight java%}
public DescriptiveStatistics getStats(Collection<Integer> iList) {
	DescriptiveStatistics stats = new DescriptiveStatistics();

	for (Integer integer : iList) {
		stats.addValue(integer.doubleValue());
	}
	return stats;
}
{% endhighlight %}

And then define other services which are applicable on the `DescriptiveStatistics` instances :

{% highlight java%}
public double getMean(DescriptiveStatistics stat) {
	return stat.getMean();
}

public double getVariance(DescriptiveStatistics stat) {
	return stat.getVariance();
}

public double getStandardDeviation(DescriptiveStatistics stat) {
	return stat.getStandardDeviation();
}

public double getPercentile(DescriptiveStatistics stat, Double p) {
	return stat.getPercentile(p);
}
{% endhighlight %}

You have to **explicitely** decide which of the methods of the `DescriptiveStatistics` class will be exposed, by default AQL will not expose any.

Once you did that you can start querying your model, here let's see what is the standard deviation of the length of a family first names:

<figure>
    <a href="{{ site.url }}/images/blog/aql-stats-service.png"><img src="{{ site.url }}/images/blog/aql-stats-service.png"></a>    
    <figcaption>Calling a service which returns an arbitrary java instance and work with it</figcaption>
</figure>


## Embedded documentation

You can specify your service documentation directly alongside the Java method so that the code completion can expose it to the user.
To do so you need to use the annotation `Documentation` which is in the `org.eclipse.acceleo.annotation` plugin.

We can extend the `getStats()` with an annotation as such :

{% highlight java%}
@Documentation(
	value = "Returns a dataset suitable for statistic queries",
	params = {				
	},
	result = "The dataset instance which can be queried..",
	examples = {
		@Example(
			expression = "self.members.name.size()->getStats()",
			result = "DescriptiveStatistics{...}"
		)
	}
)
{% endhighlight %}

And the code assist will pick up this information


<figure>
    <a href="{{ site.url }}/images/blog/aql-stats-completion.png"><img src="{{ site.url }}/images/blog/aql-stats-completion.png"></a>    
    <figcaption>Code assist dynamically extended with Annotation based documentation.</figcaption>
</figure>


## Unification of type literals

Type literals used to be handled specifically in the grammar in the first versions of AQL. We had to do this required because of the ``JustSomeType`` syntax which we supported at first.
Once we decided to drop this support and make the type prefix mandatory``someEPackage::JustSomeType``, then we could make sure AQL would handle the type literals just like any other type.

Things like :

`aql:self.eAllContents(self.eClass())`

are now possible and will return all the children of type compatible with "self".

Furthermore if you *need* a type literal as a parameter in your own service, you just have to have a first parameter with the type : `Set<EClass>`. Yes, that's an important point, any type in AQL is possibly a **union** of several existing types, hence the collection here.
As such the syntax for creating Sets or collections can be used as a substitute for type literals.

<figure>
    <a href="{{ site.url }}/images/blog/aql-typeliterals.png"><img src="{{ site.url }}/images/blog/aql-typeliterals.png"></a>    
    <figcaption>A type literal being a Set containing EClasses</figcaption>
</figure>


## Type inference at validation time

AQL is designed to apply no check during evaluation but instead capture errors if there are some. On the other hand we added pretty strong verifications at validation time and now also provide type inference based on predicates result.

Starting with the version 4.0, Sirius can leverage this type inference to be more precise in the type of the variables within an If block for instance. See the following example :

<figure>
    <a href="{{ site.url }}/images/blog/aql-tool-inference-comments.png"><img src="{{ site.url }}/images/blog/aql-tool-inference-comments.png"></a>    
    <figcaption>Use of predicates based type inference in the .odesign editor</figcaption>
</figure>

Introducing this capability means the user doesn't have to cast types using `.oclAsType()` and gets validation errors which are more useful.

## Migrating from Acceleo2 to AQL in the tests

Beside these improvements we also worked quite a lot in polishing, testing and improving the existing code. The Sirius project used to evaluate thousands of **Acceleo 2** expressions in the JUnit and swtbot tests. A large part of those expressions have been migrated to AQL and we are now quite close to a complete migration. This will open the door to a simpler and faster packaging and test story for the Sirius project (You can track progress in this regard throug [Bug 478878](https://bugs.eclipse.org/bugs/show_bug.cgi?id=478878) ) 










