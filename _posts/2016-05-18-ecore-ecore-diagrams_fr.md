---
layout: post
title: Utilisation d'Ecore.ecore avec EcoreTools
categories: [eclipse]
tags: [ecore, eclipse, ecoretools]
translation_en : /eclipse/ecore-ecore-diagrams/
lang: fr
permalink: /eclipse/ecore-ecore-diagrammes/
---

Il y a quelques semaines, je suis tombé sur le fil suivant du [Forum EMF](https://www.eclipse.dev/forums/index.php/f/108/) demandant une [documentation formelle du méta-modèle Ecore ?](https://www.eclipse.dev/forums/index.php/t/1076719/).
Ed a pointé vers [une documentation](https://download.eclipse.org/modeling/emf/emf/javadoc/2.11/org/eclipse/emf/ecore/package-summary.html) qui inclut des diagrammes réalisés avec soin mais faits avec des outils d'une autre époque.

<figure>
    <a href="{{ site.url }}/images/blog/EObjectOperations-old.gif"><img src="{{ site.url }}/images/blog/EObjectOperations-old.gif"></a>    
    <figcaption></figcaption>
</figure>

En tant que mainteneur d'EcoreTools, je devais faire quelque chose à ce sujet, et c'est ce que j'ai fait :

<figure>
    <a href="{{ site.url }}/images/blog/eobject.jpg"><img src="{{ site.url }}/images/blog/eobject-small.jpg"></a>    
    <figcaption>Tous les participants au Framework de Modélisation Ecore implémentent l'interface EObject</figcaption>
</figure>

Tadaa !

Les diagrammes suivants ont été créés grâce à [EcoreTools](https://www.eclipse.dev/ecoretools) qui fait partie du [Package Modeling Eclipse](https://www.eclipse.dev/downloads/packages/).
Tout le travail difficile a été fait auparavant par Ed lorsqu'il a dû décider quoi afficher et comment, tout ce que j'ai fait est de reproduire ceux-ci en utilisant EcoreTools et en les exportant à une résolution assez élevée (cliquez sur les images pour obtenir la pleine résolution).

*Le patchset correspondant pour EMF est [ici](https://git.eclipse.org/r/#/c/71892/).*

Mais à côté de cette action anecdotique, il y a quelque chose d'intéressant et de plus général sur la façon dont ces diagrammes présentent le modèle Ecore.ecore.

## Composants Ecore 

Ed commence par diagrammer la hiérarchie des types, sans aucune autre information (attributs ou références). Et au moins dans le cas d'Ecore, mais je suis sûr que c'est vrai dans un sens général, cela donne une très bonne introduction à un modèle de domaine : en commençant seulement avec les types qu'il définit.

<figure>
    <a href="{{ site.url }}/images/blog/ecore-components.jpg"><img src="{{ site.url }}/images/blog/ecore-components-small.jpg"></a>    
    <figcaption>Les composants Ecore sont reliés selon cette hiérarchie</figcaption>
</figure>

Pour construire un tel diagramme en utilisant EcoreTools, importez toutes les EClasses dedans, puis activez les filtres suivants :

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-filters.png"><img src="{{ site.url }}/images/blog/ecore-ecore-filters.png"></a>    
    <figcaption>Filtres dans EcoreTool</figcaption>
</figure>

Vous pouvez également activer la couche *Contraintes* qui donne un peu plus d'informations sur ce qui rend ces types valides.

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-layers.png"><img src="{{ site.url }}/images/blog/ecore-ecore-layers.png"></a>    
    <figcaption>Couches dans EcoreTool</figcaption>
</figure>


<figure>
    <a href="{{ site.url }}/images/blog/ecore-components-constraints.jpg"><img src="{{ site.url }}/images/blog/ecore-components-constraints-small.jpg"></a>    
    <figcaption>La hiérarchie + les contraintes spécifiques</figcaption>
</figure>


Voici un diagramme général mettant en évidence les références et attributs. Il peut paraître un peu encombré au premier abord, mais il regorge d'informations. Vous pouvez comprendre comment tous les aspects principaux d'Ecore fonctionnent juste en utilisant ce diagramme.

<figure>
    <a href="{{ site.url }}/images/blog/ecore-components-detail.jpg"><img src="{{ site.url }}/images/blog/ecore-components-detail-small.jpg"></a>    
    <figcaption>Les composants Ecore ont les relations, attributs et opérations suivants</figcaption>
</figure>

Pour ce type de diagrammes, vous devez vraiment connaître quelques raccourcis clavier, parmi d'autres :

| ... | ... | ... |
|Cacher élément| ![]({{ site.url }}/images/blog/2016/computer_key_Ctrl_T.png) + ![]({{ site.url }}/images/blog/2016/computer_key_H_T.png) | [->doc](https://www.eclipse.dev/sirius/doc/user/diagrams/Diagrams.html#Hidingelements) |
|Cacher étiquette | ![]({{ site.url }}/images/blog/2016/computer_key_Ctrl_T.png) +  ![]({{ site.url }}/images/blog/2016/computer_key_L_T.png)| [->doc](https://www.eclipse.dev/sirius/doc/user/diagrams/Diagrams.html#Hidinglabels) |
|Supprimer les points de flexion | ![]({{ site.url }}/images/blog/2016/computer_key_Ctrl_T.png) + ![]({{ site.url }}/images/blog/2016/computer_key_Shift_T.png) + ![]({{ site.url }}/images/blog/2016/computer_key_Minus_T.png)  | [->doc](https://www.eclipse.dev/sirius/doc/user/diagrams/Diagrams.html#Manageedges) |
| ... | ... | ... |

Vous trouverez tous les raccourcis clavier dans [l'excellent article de blog de Mélanie](https://melb.enix.org/sirius/keyboard-shortcuts/).


## Types Génériques

Le diagramme suivant se concentre sur la façon dont les **Génériques** sont modélisés dans Ecore et fait un assez bon travail en décrivant cela en cachant tous les autres aspects.

<figure>   
    <a href="{{ site.url }}/images/blog/generics.jpg"><img src="{{ site.url }}/images/blog/generics-small.jpg"></a>    
    <figcaption>Ecore prend en charge les génériques comme suit</figcaption>
</figure>

Plus important : cela n'était pas affiché **du tout** dans le diagramme précédent et c'est une bonne chose car on n'a pas besoin de comprendre ce point spécifique pour tirer parti d'Ecore.


## Types primitifs Java

Les derniers diagrammes énumèrent les types de données.

<figure>   
    <a href="{{ site.url }}/images/blog/java-language-types.jpg"><img src="{{

 site.url }}/images/blog/java-language-types-small.jpg"></a>    
    <figcaption>Ecore définit les types de données pour les types de langage Java suivants</figcaption>
</figure>

Pour ce type de diagrammes avec de nombreuses formes non connectées, vos meilleurs amis sont les actions **Rendre de même taille**, **Distribuer** et **Aligner**.

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-samesize.png"><img src="{{ site.url }}/images/blog/ecore-ecore-samesize.png"></a>    
    <figcaption>Rendre de même taille</figcaption>
</figure>

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-align.png"><img src="{{ site.url }}/images/blog/ecore-ecore-align.png"></a>    
    <figcaption>Aligner</figcaption>
</figure>

<figure>
    <a href="{{ site.url }}/images/blog/ecore-ecore-distribute.png"><img src="{{ site.url }}/images/blog/ecore-ecore-distribute.png"></a>    
    <figcaption>Distribuer</figcaption>
</figure>

## Types Externes

<figure>   
    <a href="{{ site.url }}/images/blog/external-types.jpg"><img src="{{ site.url }}/images/blog/external-types-small.jpg"></a>    
    <figcaption>Ecore définit les types de données supplémentaires suivants</figcaption>
</figure>


Alors maintenant, qui veut une belle affiche dans son bureau ?








