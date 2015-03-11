---
layout: post
title: Eclipse Sirius and Obeo Designer
categories: [eclipse]
excerpt: "Now that one of the major Obeo Designer Technologies is Open-Source you might wonder how we get to employ close to 60 people. [..]"
---

<figure>
    <img src="/images/open.png">
   <figcaption> Image credits <a href="https://www.flickr.com/photos/opensourceway/">opensourceway</a></figcaption>
</figure>

Now that one of the [majors Obeo Designer Technologies](http://www.eclipse.org/sirius/) is Open-Source you might wonder how we get to employ close to 60 people. It's actually quite straightforward:

* We sell domain-dedicated products notably SmartEA, [focused on Enterprise Architecture](http://www.obeosmartea.com/)
* We sell [support subscriptions](http://www.obeodesigner.com/support) offering you simplicity and safety when leveraging Sirius.
* We sell software bringing [repository based collaboration](http://www.obeodesigner.com/collaborative-features) on top of EMF and Sirius.
* We offer open-innovation services to develop features or adapt open-source technologies within the Eclipse eco-system.
* We offer training, expertise and development services when you want to build your own tooling.

and this gets reflected in the products related to Sirius:

## Obeo Designer Community Edition

This is the *go to* package to build your domain-specific tooling. We make sure you get the technologies you need in a consistent and compatible way, all in a single download (**Sirius**, **Ecore Tools**, **EMF Compare**...).
Starting with this package you get to build graphical modelers, table or tree editors without having to assemble a list of technologies working nicely together.

We provide regular updates and maintenance on this package even if its main focus is the latest releases.

This product is now **100% free**, as in **completely under the Eclipse Public License**. You have the rights to adapt or redistribute it if you wish to, but you don't have to 
do it alone; we've [got you covered](http://www.obeodesigner.com/buy) with a subscription matching the level of other tool vendors (and **per organization pricing**.)

I'm often asked how is that making us different from service companies. It makes us *completely different*. 

* It gives use deep incentives to have a strong quality in the products or the business model collapse. We are able to provide support at such a small price only if the number of fixes we have to make post release is reduced too. Furthermore, as I mentioned earlier we are also distributing products based on Sirius on our own.

* We have no choice than investing in the technology in a sustainable way. Evolving the technologies to offer more and more value for the users while keeping the risks under complete control and having a clear and cheap migration path.
As an example, that's why Sirius will migrate your Viewpoint and Representations models from version to version or that upgrading is actually fairly easy despite some internal refafactorings.


Of course every organization out there want to ship products which a high level of quality and add new features now and then but in our case **such decisions in Sirius directly affect a decent part of our income**.

## Obeo Designer Team Edition

Once you defined your tooling it's time to deploy it. [Obeo Designer Team Edition](http://www.obeodesigner.com/collaborative-features) brings collaborative features to your tooling in a straightforward way for end users. 
No need for *checkout*, *commit*, *compare* or *merge* actions: the technology automatically takes fine grained short-lived locks and publish the changes. In essence, **Google doc for models** within your firewall.

Obeo Designer **Team Edition** targets the deployment phase of your tooling, and as such has a different life cycle. One major release a year is more than enough, pricing depends on the number of seats you need.

## How does that affect Sirius?

For a start, it means we do have [regular maintenance releases](https://projects.eclipse.org/projects/modeling.sirius/governance): we released Sirius [2.0.0](https://projects.eclipse.org/projects/modeling.sirius/releases/2.0.0) 
at the end of October and are now at [2.0.4](https://projects.eclipse.org/projects/modeling.sirius/releases/2.0.4/bugs), each version bringing from 2 to 16 fixes.

It also means changes are not done lightly: we review, qualify and test the changes to achieve the level of quality we aim for.
For example, [Locating anchors on the border of images instead of the bounding box](https://bugs.eclipse.org/bugs/show_bug.cgi?id=452294) led to four changesets some of them being refined up to 16 times.

In the end everybody wins, users have access to an evolving technology with vendor's guarantees and reach out to Obeo to sponsor features, get access to expertise, training or to the collaborative feature, and that in itself funds further open-source developments.

That being said you don't have to take my word, give it a try and **[download Obeo Designer Community](http://www.obeodesigner.com/download), it's 100% EPL.**
