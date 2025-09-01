---
layout: post
title: Checklist de conception de métamodèle (Ecore) - partie 1
categories: [modeling]
tags:
  - ecore
  - emf
  - eclipse
permalink: /eclipse/checklist-conception-ecore-partie1/
lang: fr
translation_en: /eclipse/ecore-design-checklist-part1/
excerpt: "Une checklist pratique pour concevoir un métamodèle Ecore (partie 1) : pour créateurs d’outils EMF/Sirius; pourquoi maintenant—poser de bonnes bases pour éviter des refactorings coûteux."
---

**Soyez méticuleux avec le modèle décrivant votre domaine !**
Tellement d'aspects de votre outil découlent de votre modèle Ecore qu'il est très bénéfique de s'arrêter un moment pour effectuer quelques vérifications de base.

<figure>
    <a href="{{ site.url }}/images/blog/ecore-middle-big.png"><img src="{{ site.url }}/images/blog/ecore-middle.png"></a>    
    <figcaption>Le modèle Ecore au centre est la base de tant de choses !</figcaption>
</figure>

**Les technologies de modélisation Eclipse** vous permettent de construire des éditeurs graphiques, arborescents ou textuels, des connecteurs pour importer ou exporter des données, des générateurs de code et toutes ces fonctionnalités dans votre outil sont directement liées ou déduites d'un modèle Ecore. Mieux vaut bien le faire.

J'ai compilé la liste de contrôle suivante basée sur mon expérience personnelle, celle-ci n'est pas exhaustive et je m'attends à ce qu'elle évolue et s'enrichisse avec le temps.

> La plupart des vérifications indiquées ici sont très faciles à respecter si elles sont prises en compte dès le début. 
> Plus tard, il est nécessaire d'évaluer le rapport gain/risque car certains changements peuvent nécessiter la mise à jour de certains codes, fichiers, ou peuvent simplement être trop de travail pour en valoir la peine.
> Pour cette raison et parce que nous avons parfois appris à la dure, vous pourriez facilement trouver certains modèles Ecore que j'ai rédigés qui ne sont pas à 100% conformes à cette liste ;).

Au fait, n'hésitez pas à [me parler de vos propres règles](https://twitter.com/bruncedric), je pourrais les ajouter à la liste !

---

## Règles de base

### ☑ Le but et la cible des modèles sont clairs et affirmés

Un modèle est une représentation d'un système **pour un but donné**. Tout comme la programmation orientée objet n'a jamais été conçue pour aider à "structurer le code de manière à ce qu'il soit proche du monde réel", un métamodèle n'a pas à correspondre au monde réel.

D'autre part, un métamodèle devrait répondre à un ensemble spécifique de questions. Commencez par énoncer ces questions. Et pour qui.

Le "**qui**" utilise le modèle, cela peut avoir des implications importantes sur le nommage des concepts.
Mon outil de choix pour définir le "qui" est de prendre quelques minutes et de rédiger un [Persona](https://en.wikipedia.org/wiki/Persona_(user_experience)) afin que je puisse m'y référer lorsque j'ai besoin de justifier un choix donné. La description du persona doit documenter le contexte de l'utilisateur, le vocabulaire avec lequel il est à l'aise et les outils qu'il utilise habituellement.

Exemple : Les modèles de ce métamodèle permettront à *des chercheurs en agriculture* de répondre aux questions : *combien de ressources (eau, machines, humains) sont nécessaires pour une structure agricole donnée, dans une région donnée, et pour un ensemble de cultures (blé, sorgho, etc.) ?*

<br>
<br>

Exemple : Les modèles de ce métamodèle permettront à *des architectes logiciels* de répondre aux questions : *quels sont les services existants dans mon système, quelles sont leurs caractéristiques non fonctionnelles, leur signature, qui les possède et comment sont-ils liés les uns aux autres ?*

<img src="{{ site.url }}/images/blog/my-little-pony.jpg" style="float: right;">
<br>
<br>
ou même
<br>
<br>
Exemple : Les modèles de ce métamodèle permettront aux *auteurs de My Little Pony* de répondre aux questions *comment l'histoire et les personnages évoluent-ils pendant le spectacle, quand chaque personnage est-il introduit et est-ce cohérent avec les épisodes précédemment diffusés ?*


---

### ☑ Le nsURI est définitif et cohérent avec vos conventions de nommage

Dans cette première étape de création d'une carte d'identité pour votre métamodèle, vous **devez** vous arrêter un instant pour trouver le nsURI de l'EPackage.
Ce nsURI identifiera votre modèle Ecore, dès maintenant et pour toujours. Il est utilisé dans de nombreux endroits, dans le code Java généré, dans le fichier ``plugin.xml`` de votre projet, mais plus important encore, d'autres outils ou modèles Ecore sont susceptibles d'utiliser ce URI pour identifier votre modèle Ecore (dans les générateurs de code, les transformateurs de modèles...).

Changer cela est douloureux. Assurez-vous que le ``nsURI`` que vous avez choisi est sensé et correspond à vos conventions de nommage à cet égard.

La chose la plus importante est d'être cohérent et ce n'est pas évident ; voyez comment nous échouons à avoir une dénomination cohérente dans Eclipse lui-même.

<figure>
    <a href="{{ site.url }}/images/blog/nsURIs.png"><img src="{{ site.url }}/images/blog/nsURIs.png"></a>    
    <figcaption>NsUris dans le package de modélisation.</figcaption>
</figure>

Le même niveau de soin doit être utilisé pour votre **nom de projet**. Assurez-vous de bien le faire rapidement ou préparez-vous à bidouiller avec des identifiants dans de nombreux fichiers différents.

### ☑ Les EPackages imbriqués ne sont pas utilisés

Il n'existe pas de **sous**-EPackage dans un EPackage. Faisons comme si cette capacité n'avait jamais existé dans Ecore (et d'ailleurs, vous ne pouvez pas le faire dans Xcore).

> --- Commentaire #4 de Ed Merks <Ed.Merks@gmail.com> ---
> Oui, cela ne fonctionne tout simplement pas. Il n'est pas possible de représenter un Ecore Package imbriqué dans Xcore.

Autoriser la définition de sous-packages au sein d'un EPackage était, avec le recul, une mauvaise décision car cela a introduit plusieurs manières différentes de référencer un même domaine. Nous devrions avoir une correspondance un à un entre un domaine et un EPackage, celui-ci clairement identifié par son `nsURI`. La notion d'EPackage imbriqué rompt cette correspondance car vous avez alors plusieurs manières différentes d'accéder à un EPackage. Cela conduit à des interprétations légèrement différentes de ceci parmi les outils ; un outil pourrait déclarer un sous-package si un parent est déclaré, ou l'inverse, ou pas du tout.

En résumé, un EPackage, un fichier `.ecore`, et votre vie sera plus simple.
### ☑ Les noms sont réels, précis et cohérents

Nommer les choses est difficile, et comme dans toute activité de conception, c'est d'une importance cruciale. Pour les non-anglophones, cela devient encore plus difficile car nous pouvons manquer de vocabulaire ou certaines interprétations subtiles peuvent nous échapper.

<img src="{{ site.url }}/images/blog/dictionary___spike___osx_icon_by_glitch452-d4ixe2u.png" style="float: right;">

Astuces et conseils :

* utilisez [PowerThesaurus](https://www.powerthesaurus.org/), assurez-vous que le nom est le plus précis possible.
* utilisez le contexte de l'utilisateur pour choisir le bon nom (avoir défini le Persona est utile)
* essayez d'éviter des noms trop généraux ou abstraits qui pourraient être interprétés de différentes manières par vos utilisateurs cibles. « Artifact », « Element » sont probablement de mauvais noms (mais encore une fois, utilisez le contexte pour décider).

> dans le monde de MyLittlePony, un **Element** se réfère aux "*Elements of Harmony*" et a une définition très précise. Le contexte compte.

### ☑ Les noms de références et d'attributs sont cohérents

Vérifiez que vous suivez une convention cohérente pour vos références. Les principales décisions qui s'offrent à vous :

* pluralisez-vous les références avec une borne supérieure **many** ?
* ajoutez-vous un préfixe comme `owned` pour toute référence de contenu ?
* ajoutez-vous un préfixe comme `parent` pour toute référence de conteneur ?
* ajoutez-vous un préfixe pour toute référence ou attribut `dérivé` ?

### ☑ Toutes les EClasses non-abstraites sont supposées être instanciées

Dans les premières phases, il arrive souvent que vous commenciez par un concept sous forme d'EClass et à un moment donné, vous le spécialisez, aboutissant à une EClass abstraite mais vous oubliez de la rendre abstraite, permettant ainsi son instanciation.

Prenez le temps de passer en revue tous les concepts que vous ne voulez pas instanciables et assurez-vous qu'ils sont "abstract" ou "interface".

<figure>
    <a href="{{ site.url }}/images/blog/abstractness.gif"><img src="{{ site.url }}/images/blog/abstractness.gif"></a>    
    <figcaption>Introduction de sous-classes</figcaption>
</figure>

### ☑ Les cardinalités 0..1 et 1..1 ont été revues

Passez en revue tous les attributs et références et réfléchissez à nouveau : est-ce qu'une instance a **un sens** si cet attribut n'est pas valorisé ?

<figure>
    <a href="{{ site.url }}/images/blog/mandatory.png"><img src="{{ site.url }}/images/blog/mandatory.png"></a>    
    <figcaption>EcoreTools utilise des polices en gras pour tout élément requis</figcaption>
</figure>

### ☑ Les relations de contenance ont été revues

Ecore fournit une notion de **contenance** qui réifie le cycle de vie de base d'une instance. Si un objet `A` est contenu dans un objet `B`, alors lorsque l'objet `B` est supprimé, l'objet 'A' l'est également. Penser à votre modèle comme à un arbre aide dans ces cas : soit votre objet est censé être à la racine d'une ressource, soit il doit être contenu par un autre objet.

L'objectif est de prendre une décision consciente sur le moment où une instance doit disparaître du modèle et d'identifier clairement le type d'éléments que vous attendez en tant que racine d'un fichier de modèle.
> Notez également que cette relation de contenance peut être utilisée dans le cadre de la référence d'un élément.

### ☑ Chaque règle de validation qui n'est pas imposée par la structure du modèle Ecore elle-même est nommée.

Lors de la conception, capturez et nommez chaque règle de validation qui se présente. Vous devriez être en mesure de proposer un nom et, espérons-le, une description des cas valides et invalides.

<figure>
    <a href="{{ site.url }}/images/blog/constraints.png"><img src="{{ site.url }}/images/blog/constraints.png"></a>    
    <figcaption>Annotations de contraintes dans EcoreTools.</figcaption>
</figure>

### ☑ Les concepts sont tous documentés.

Assurez-vous d'avoir documenté toutes les EClasses ou relations qui ne sont pas complètement évidentes. Nous utilisons des annotations directement dans Ecore pour capturer la documentation destinée aux développeurs ou aux spécificateurs.

<figure>
    <a href="{{ site.url }}/images/blog/doc-diag.png"><img src="{{ site.url }}/images/blog/doc-diag.png"></a>    
    <figcaption>L'annotation de doc de conception peut être ajoutée dans un diagramme en utilisant EcoreTools</figcaption>
</figure>

<figure>
    <a href="{{ site.url }}/images/blog/doc-table.png"><img src="{{ site.url }}/images/blog/doc-table.png"></a>    
    <figcaption>Un éditeur de table est également fourni pour plus de commodité</figcaption>
</figure>

Notez que vous pouvez également valoriser un attribut dans le Genmodel pour la documentation utilisateur et que cette information sera directement utilisée par EMF dans l'éditeur arborescent.

### ☑ Il n'y a pas de monstres Booléens en devenir

Avec le temps, une simple EClass avec quelques EAttributes peut devenir un monstre avec bien plus, chacun agissant comme un "drapeau" de configuration. Identifiez ces monstres en devenir. Passez en revue toutes les combinaisons possibles de valeurs d'attributs et assurez-vous qu'elles sont toutes valides, et confirmez également qu'il n'y a que deux résultats possibles : vrai ou faux, mais pas plus. Parfois, une paire d'EEnumerations est meilleure pour capturer les caractéristiques transversales.

<figure>
    <a href="{{ site.url }}/images/blog/booleans.png"><img src="{{ site.url }}/images/blog/booleans.png"></a>    
    <figcaption>Monstre Booléen</figcaption>
</figure>

Vérifiez également le nommage de vos attributs booléens. Le générateur Java EMF ajoutera un préfixe "is" à votre API, vous n'avez pas besoin de le faire, mais assurez-vous que ``isMyName`` est lisible.
## Monde extérieur

### ☑ J'ai décidé comment les instances doivent être référencées de l'extérieur

Tout EObject contenu dans une ressource a une URI et peut être référencé par d'autres. Mais il existe tellement de manières d'identifier une instance. Vous devez globalement décider entre : une identification spécifique à la ressource comme les XMI-IDs, ou une identification liée au domaine en définissant un attribut **id** EAttribute ou en utilisant les **eKeys** de l'EReference.

Le comportement par défaut utilise la relation de contenance et l'indice de l'objet dans sa référence contenant. Cette solution n'est pas adaptée dans 99% des cas car tout ajout ou suppression dans une référence pourrait rompre les références (mais c'est la solution par défaut dans EMF car c'est la seule qui ne présume rien du format de sérialisation ou des EClasses).

<figure>
    <a href="{{ site.url }}/images/blog/ekey.png"><img src="{{ site.url }}/images/blog/ekey.png"></a>    
    <figcaption>EcoreTools affiche la eKey avec une petite étiquette bleue à l'extrémité cible</figcaption>
</figure>

### ☑ Un utilisateur ne peut pas introduire de références cycliques entre fragments de modèle

Si vous prévoyez de diviser votre modèle en plusieurs fichiers ou si une partie doit être référencée par d'autres modèles, alors vous devez vous assurer que l'introduction de telles références ne doit pas modifier l'instance référencée. Ces situations peuvent facilement survenir lors de l'utilisation de références EOpposite.

Gardez à l'esprit que de nombreuses technologies EMF vous fourniront un moyen facile et efficace de naviguer sur des références inverses qui ne sont pas conçues comme telles dans le modèle Ecore.

Par exemple, en utilisant Sirius, vous pourriez écrire des requêtes comme :
`aql:self.eInverse(some::Type)` pour récupérer toute instance de `Type` référençant l'objet `self`
ou `aql:self.eInverse(anEReferenceName)` pour naviguer sur l'inverse de la référence `anEReferenceName` de l'objet `self`.

### ☑ Les dépendances entre les EPackages sont maîtrisées

L'héritage ou les références entre EPackages peuvent rapidement devenir compliqués (et le premier encore plus que le second). Il est si facile de le faire en utilisant les outils de modélisation que l'on peut facilement en abuser, mais en fin de compte, votre modèle Ecore est traduit en composants Java et OSGi, et vous devrez gérer la coordination technique.

Ainsi, n'introduisez des relations inter-EPackages que pour des raisons impérieuses et lorsque vous le faites, assurez-vous de ne référencer que des EClasses ou, si vous avez besoin de sous-classer, assurez-vous de pouvoir gérer un couplage fort sur le composant correspondant.

<figure>
    <a href="{{ site.url }}/images/blog/coupling.png"><img src="{{ site.url }}/images/blog/coupling.png"></a>    
    <figcaption>Diagramme de dépendances de paquets dans EcoreTools</figcaption>
</figure>

### ☑ Les EClasses qui pourraient être étendues par des sous-types sont clairement identifiées

Cet élément est symétrique au précédent : si l'un de vos objectifs est que d'autres fournissent des sous-types de vos EClasses, concevez-le explicitement et documentez-le.

___

C'est tout pour le moment, mais le sujet est loin d'être épuisé. La [partie 2](https://cedric.brun.io//eclipse/checklist-conception-ecore-partie2/) est plus technique avec un accent sur la scalabilité et sur la correspondance entre Ecore et Java. N'hésitez pas à donner votre avis via [Twitter](https://twitter.com/bruncedric)!
