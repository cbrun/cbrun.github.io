---
layout: post
title: "Combien de temps me faut-il pour faire du café ?"
categories:
  - modeling
tags:
  - modeling
  - eclipse
  - sirius
  - opensource
lang: fr
permalink : /modeling/guesstimate-modelisation-probabilite/
translation_en : /modeling/guesstimate-probability-modeling/
excerpt: "Démo courte d’un prototype Sirius Web pour des « guesstimates » Monte Carlo — pour modélisateurs et ingénieurs — montrant comment créer rapidement des outils métier."
---
Alors que vous profitez peut-être de votre été et que vous naviguez par ici, laissez-moi vous montrer un petit prototype sur lequel j'ai travaillé par intermittence à travers plusieurs versions de Sirius Web.

Il est maintenant basé sur la dernière version de Sirius Web. Bravo à l'équipe Sirius pour leurs sorties toutes les 8 semaines comme sur des roulettes !

L'idée a été inspirée par Guesstimate :
> *Un tableur pour les choses qui ne sont pas certaines !*

C'est un outil que j'ai toujours aimé, et je voulais voir jusqu'où nous pouvions aller avec Sirius.

Ce prototype est un outil spécifique au domaine pour la « guesstimation » utilisant des simulations de Monte Carlo. Ce n'est qu'une preuve de concept, mais il met vraiment en valeur certaines fonctionnalités sympas de Sirius Web :
- Toute la logique spécifique au domaine est conservée dans un métamodèle basé sur EMF et l'implémentation Java correspondante. Il n'y a que 11 fichiers et 1 028 lignes de code non généré.
- J'utilise le widget de graphiques dans la vue des détails, ce qui ajoute une touche agréable.
- L'intégration avec les bibliothèques Java est super facile – ici, j'ai utilisé Apache Common Maths et PetitParser.

Regardez la vidéo pour le voir en action !
<video  width="640" height="360" controls><source src="{{ site.url }}/media/2024-08-08-Guesstimate.mp4">Your browser does not support the video tag.</video>
