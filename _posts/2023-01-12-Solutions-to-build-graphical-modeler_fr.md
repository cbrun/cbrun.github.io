--- 
layout: post 
title: Construire des Outils de Modélisation Graphique, Approches pour Réduire la Complexité 
categories: [modeling] 
tags: [modeling, emf, eclipse, sirius] 
lang: fr
permalink : /modeling/guesstimate-modelisation-probabilite/
translation_en: /modeling/Solutions-to-build-graphical-modeler/
---

Construire des outils de modélisation graphique peut être une entreprise complexe, surtout s'ils doivent prendre en charge de nombreuses fonctionnalités et fonctions. Chez Obeo, nous avons une vaste expérience dans ce domaine et nous nous efforçons de rendre le processus aussi simple et accessible que possible. Pour y parvenir, nous nous appuyons sur plusieurs stratégies, y compris la conception modulaire, les abstractions de plus haut niveau, et la capacité à itérer rapidement sur la définition d'un outil. Ces dernières années, nous avons conservé ces principes tout en faisant migrer les technologies vers le Web.

## La Communauté des Modules

Tout comme la quête pour détruire l'Anneau Unique dans Le Seigneur des Anneaux a été simplifiée en la divisant en tâches plus petites et en les déléguant à divers membres de la communauté, nous utilisons les technologies de modélisation Eclipse avec une conception modulaire pour gérer la complexité dans notre logiciel. Chaque projet est responsable d'une tâche spécifique, fournissant des composants qui peuvent être réutilisés et intégrés dans un outil pour l'utilisateur final. Par exemple,
- [EMF](https://www.eclipse.dev/modeling/emf/) gère les données du modèle et son API,
- [Sirius](https://www.eclipse.dev/sirius) se concentre sur les éditeurs et les outils,
- [EMF Compare](https://www.eclipse.dev/emf/compare/) permet la comparaison, la fusion et la résolution de conflits de différentes versions de modèles,
- [Acceleo](https://www.eclipse.dev/acceleo/) permet la génération de code ou de texte à partir des modèles,
- [M2Doc](https://www.m2doc.org/) produit des rapports et des documents en utilisant des modèles et des diagrammes comme entrées.

Cette conception modulaire a plusieurs avantages. Elle rend le logiciel plus facile à comprendre et à travailler, car vous pouvez vous concentrer sur un module à la fois plutôt que d'essayer de comprendre l'ensemble du système d'un seul coup. La conception modulaire facilite également la réutilisation du code et des fonctionnalités. Si vous construisez un module qui fait quelque chose d'utile, vous pouvez l'utiliser dans d'autres projets. Le projet Sirius est un bon exemple de cela, car il fournit un ensemble complet de fonctionnalités qui sont réutilisées et exposées à travers des centaines de modeleurs graphiques. Vous pouvez voir quelques exemples dans la [Galerie Sirius](https://www.eclipse.dev/sirius/gallery.html).

Bien que la conception modulaire soit utile, elle n'est pas une solution parfaite et présente certains défis. Un défi est de s'assurer que les modules fonctionnent bien ensemble et n'ont pas de conflits ou de dépendances. Cela peut être particulièrement difficile lorsque les modules évoluent indépendamment au sein de leurs propres projets. Pour résoudre ce problème, nous nous coordonnons avec d'autres projets au sein de l'Eclipse Release Train et construisons une suite intégrée appelée le "Obeo Designer Community," qui est un packaging prêt à l'emploi.

<figure> 
<a href="https://www.obeodesigner.com/en/download"><img src="{{ site.url }}/images/blog/2023/od.png"></a> 
<figcaption>Téléchargement d'Obeo Designer</figcaption> 
</figure>

## Inception : L'Édition de l'Abstraction de Plus Haut Niveau 

Tout comme Cobb et son équipe dans Inception, nous utilisons des abstractions de plus haut niveau pour masquer la complexité sous-jacente de la construction d'un logiciel de modélisation graphique et rendre le processus plus gérable pour nos utilisateurs. Les abstractions de plus haut niveau peuvent prendre de nombreuses formes, comme des bibliothèques, des frameworks ou des langages spécifiques au domaine (DSLs). Chez Obeo, nous utilisons les DSLs comme choix d'abstractions de plus haut niveau. Un exemple de cela est Sirius. Lorsque vous définissez un outil en utilisant Sirius, vous spécifiez le modélisateur graphique que vous souhaitez obtenir en termes de formes graphiques et comment ces formes sont mappées au modèle de domaine. Vous pouvez également spécifier un ensemble d'éditeurs, d'actions et d'assistants qui peuvent être lancés par l'utilisateur final, sans avoir à gérer les détails de codage de ces fonctionnalités sur la plateforme sous-jacente. Sirius gère ces détails en coulisse.

<figure> 
<img src="{{ site.url }}/images/blog/2016-2017/1capture.png"> 
<figcaption>Partie d'une définition d'outil et le résultat correspondant pour le DSL "Family".</figcaption> 
</figure>

Cependant, les abstractions de plus haut niveau ont aussi leurs défis. Un défi est qu'elles peuvent ajouter une couche supplémentaire de complexité au logiciel. Les développeurs doivent comprendre comment fonctionne l'abstraction et comment l'utiliser correctement. Pour aider à cela, nous offrons un support et une expertise, des formations et des tutoriels pour bien démarrer avec Sirius. Nous organisons également la conférence SiriusCon chaque année depuis 2015 pour aider notre communauté à découvrir ce qu'elle peut faire avec Sirius. Un autre défi est que les abstractions de plus haut niveau peuvent être limitantes. Elles peuvent ne pas fournir toutes les fonctionnalités et toute la flexibilité dont les développeurs ont besoin, ou elles peuvent rendre difficile de faire les choses d'une manière différente. Pour répondre à cela, nous permettons que le comportement de l'outil soit étendu avec du code Java lorsque cela est nécessaire. Cela est utile lorsque l'outil doit interagir directement avec un autre outil, plutôt que par des échanges de fichiers, ou lorsque des calculs spécifiques ou des interfaces utilisateur sont requis. La plateforme Eclipse Modeling est généralement extensible, et EMF, Compare, Acceleo, Sirius, et d'autres projets fournissent des points d'extension dédiés pour permettre à leur comportement d'être personnalisé en utilisant du code Java et des APIs. De plus, Sirius et Acceleo permettent de se ramifier à un simple code Java directement, sans avoir besoin de comprendre complètement la plateforme Eclipse.

# The Fast and the Furious des Outils de Modélisation Graphique : Rechargement à Chaud

Comme l'équipe dans la franchise Fast and Furious, nous visons à réduire la complexité de la construction d'un logiciel de modélisation graphique en permettant une itération rapide et un retour rapide. Une itération rapide signifie être capable de faire des changements au logiciel rapidement et facilement, et de voir les résultats de ces changements immédiatement. Dans le cas de Sirius, deux facteurs permettent cela, d'abord en fournissant une abstraction de plus haut niveau pour définir un outil de modélisation, on peut exprimer plus vite et avec plus de précision ce à quoi l'outil doit ressembler et faire. Le deuxième facteur, et celui-ci ressort assez bien par rapport aux autres frameworks que vous pouvez utiliser pour construire un outil graphique, est que Sirius rechargera à chaud votre définition d'outil, vous êtes capable de voir instantanément l'outil en action, d'adapter sa définition, de voir le résultat, et d'itérer. C'est une révolution, car alors le coût d'essayer une autre manière de représenter le domaine et d'interagir avec lui n'est que de quelques minutes, et revenir à la version précédente de l'outil n'est qu'à un CTRL-Z. 

<figure> 
<img src="{{ site.url }}/talks/ModelingAvengers/pics/dynamic-shapes-vsm.png"> 
<figcaption>Partie d'une définition d'outil et le résultat correspondant pour un DSL lié à l'agriculture.</figcaption> 
</figure>

Avec Sirius Web, nous allons même un pas plus loin en réduisant cette boucle de feedback : vous adaptez l'outil, il est instantanément utilisable par tous les ingénieurs y accédant directement depuis leur navigateur web.

<video width="640" height="360" controls><source src="{{ site.url }}/media/SiriusWeb and JupyterNotebook.mp4">Votre navigateur ne supporte pas la balise vidéo.</video>

----

Pour résumer, construire un outil de modélisation graphique peut être complexe, mais il existe plusieurs façons d'aborder cette complexité. La conception modulaire permet une meilleure compréhension et réutilisation du code, tandis que les abstractions de plus haut niveau peuvent masquer la complexité sous-jacente à l'utilisateur. L'itération et le retour rapide est également important pour un développement efficace. Obeo travaille sur ces technologies pour rendre la construction d'outils de modélisation graphique plus accessible depuis de nombreuses années maintenant, et nous sommes enthousiasmés par les perspectives de ce qui est à venir sur ce chemin : tandis que Sirius sur le bureau a prouvé que c'est un moyen efficace de s'attaquer à cette complexité, [Sirius on the Web](https://www.eclipse.dev/sirius/sirius-web.html) va même un pas plus loin pour rendre de tels outils accessibles à tous.
```
