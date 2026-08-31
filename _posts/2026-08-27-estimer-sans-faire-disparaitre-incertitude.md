---
layout: post
title: "Estimer sans faire disparaître l’incertitude"
seoTitle: "Estimation à trois points : intégrer l’incertitude dans un projet logiciel"
categories:
  - obeo
tags:
  - obeo
  - software-engineering
  - agile
lang: fr
permalink: /obeo/estimation-trois-points-incertitude-projet-logiciel/
translation_en: /obeo/three-point-estimation-software-project-uncertainty/
excerpt: "Retour d’expérience sur l’estimation à trois points pour les développeurs et responsables de projet qui veulent chiffrer un effort sans masquer l’incertitude derrière un nombre unique."
---

Pendant longtemps, une bonne estimation était pour moi un chiffre précis. Si quelqu’un me répondait « entre trois et six mois », j’avais plutôt l’impression qu’il esquivait la question. Trois ou six mois, ce n’est quand même pas du tout la même chose.

Et dans l’informatique, cette question revient tout le temps. On est développeur, un besoin apparaît, et quelqu’un demande : « combien de temps pour faire ça ? »

## Quand « deux heures » signifiait « une première démo »

À [Obeo](https://www.obeosoft.com/fr/societe/), nous avons eu sur ce sujet un chemin un peu initiatique. Au début, nous étions moins d’une dizaine et nous travaillions sur les prémices de ce qui deviendrait [Eclipse Sirius](https://eclipse.dev/sirius/). J’étais alors développeur, en contact direct avec le client. On échangeait, un besoin émergeait, puis venait naturellement la question :

> Combien de temps pour faire cela ?

« Oh, je dirais deux heures. »

Si vous avez un peu trempé dans le développement logiciel, vous voyez probablement déjà où l’on va : dans le mur.

<figure>
    <a href="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_1.png"><img src="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_1.png"></a>
    <figcaption>Un point cache une étendue</figcaption>
</figure>

Mes « deux heures », c’était en gros le temps nécessaire pour avoir une première version sur mon poste. Sans avoir traité tous les cas aux limites, sans tests automatiques, sans documentation, sans les retours du client qui arriveraient après la livraison. Bref, le temps qu’il me fallait pour que vous veniez à côté de moi et que je puisse vous montrer quelque chose qui « quasi-fonctionne ».

Sauf que tout ce qui reste à faire après ce « quasi » prend au moins autant de temps, et souvent beaucoup plus.

Les premières versions de Sirius sont parfois sorties dans la douleur. La date était figée, le périmètre également, le tout sur la base de nos estimations. Quand arrivait le jour de la livraison, tout était à peu près là, mais rien n’était complètement terminé. On en a fait, des livraisons qui se terminaient à trois heures du matin, voire plus tard.

<figure>
    <a href="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_2.png"><img src="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_2.png"></a>
    <figcaption>Quand “deux heures” voulait dire “une première démo”</figcaption>
</figure>

J’ai raconté le contexte de ces premières années dans [Obeo fête ses 10 ans]({{ site.url }}/eclipse/obeo-dix-ans/).

Il nous a donc fallu réapprendre complètement à estimer une fonctionnalité ou une correction : compter la documentation, les tests, l’intégration et les retours du client après livraison. Cela paraît assez évident aujourd’hui, mais ça ne l’était pas forcément à l’époque.

Ce serait d’ailleurs une autre leçon intéressante : quand vos chiffrages font soudainement ×2 parce que vous commencez enfin à compter tout le travail, alors que vos clients étaient habitués aux anciens chiffres, la gestion du changement devient elle-même un sujet.

Je diverge. Enfin, pas complètement : tout cela illustre déjà une première chose. Estimer une tâche correctement suppose de bien la délimiter et d’identifier ce qu’elle contient réellement.

## Un chiffre devient vite un engagement

Mais une fois cela appris, un autre problème restait entier : on continuait à donner **un chiffre**.

Prenons une série de petites tâches. Pour chacune, si je dis « 0,5 jour » plutôt que « 1 jour », le total obtenu à l’échelle du projet sera très différent. Pourtant, individuellement, chacune de ces tâches peut réellement prendre une demi-journée, ou une journée, ou parfois davantage.

Et lorsqu’on demande au développeur de choisir un chiffre, ce chiffre devient immédiatement une forme d’engagement.

« Combien de temps ? »

« Un jour. »

Très bien, un jour.

Toute l’incertitude qui existait pourtant dans la tête de la personne quelques secondes auparavant vient de disparaître.

J’ai donc commencé à chercher d’autres manières de faire. Je me suis intéressé à la vélocité et aux points agiles, et surtout à l’[Evidence-Based Scheduling de Joel Spolsky](https://www.joelonsoftware.com/2007/10/26/evidence-based-scheduling/), qui avait beaucoup résonné en moi par son caractère scientifique. L’idée est d’utiliser les écarts observés entre estimations et réalisations pour construire une distribution probabiliste des dates possibles.

Le problème est que cela nécessite un suivi extrêmement précis, qui ne m’a jamais vraiment semblé réaliste à mettre en œuvre chez nous, ni même particulièrement désirable.

## Additionner tous les risques ne fonctionne pas non plus

Pour nos devis clients, nous avons alors introduit autre chose : une valeur de charge, accompagnée d’un chiffre complémentaire de « risque », représentant le nombre de jours supplémentaires que la tâche pourrait nécessiter.

Il y avait un vrai bon point : on se posait enfin explicitement la question du risque.

Mais il y avait aussi un mauvais point. Sur certains devis, nous pouvions arriver à un montant beaucoup trop élevé simplement parce que nous avions additionné tous les risques. Commercialement, il arrivait alors que nous réduisions le chiffrage, avec l’idée qu’Obeo pouvait assumer une partie du risque. C’est une décision possible, bien sûr, mais elle a une conséquence gênante : le devis commercial commence alors à s’écarter de ce que nous pensons réellement nécessaire pour réaliser le projet.

Et ce n’est pas très satisfaisant.

Cette approche avait aussi un autre effet pervers : un sujet exploratoire devenait mécaniquement beaucoup plus cher, puisque, par définition, il comportait davantage d’incertitude.

Or, chez Obeo, nous aimons plutôt les sujets exploratoires. Ce sont souvent ceux qui nous permettent d’apprendre, de pousser nos technologies plus loin et de les faire mûrir. Si tous les projets susceptibles de faire progresser une technologie sont pénalisés parce qu’ils sont incertains, et donc chiffrés très haut, tout le monde finit par être perdant.

Cette capacité à explorer tout en s’engageant sur un résultat reste au cœur des [développements spécifiques réalisés par Obeo](https://www.obeosoft.com/fr/services-fr/developpements-specifiques/). Elle rejoint aussi une question plus large que j’aborde dans mon guide sur [l’open source industriel]({{ site.url }}/fr/open-source-industrial/) : comment financer l’apprentissage, la maintenance et la maturation d’une technologie commune sans faire porter tout le risque à un seul projet ?

Et je n’évoque même pas le temps passé à réaliser des chiffrages très détaillés dans l’espoir de faire baisser la marge d’erreur. C’est beaucoup de temps passé, et généralement du temps non payé.

C’est progressivement là que mon point de vue a changé. Je reste convaincu que l’engagement est nécessaire. Mais la précision à cette granularité l’est beaucoup moins.

Le problème n’était peut-être pas de réussir à trouver **le bon chiffre**. Le problème était peut-être de vouloir absolument n’en donner qu’un.

## Trois chiffres au lieu d’un

J’ai donc cherché des pratiques existantes qui prenaient réellement en compte l’incertitude, avec de vraies mathématiques derrière. Après tout, on sait faire des calculs probabilistes. Et je suis tombé sur les [estimations à trois points](https://en.wikipedia.org/wiki/Three-point_estimation).

Le principe est assez simple : pour chaque tâche, au lieu de donner une valeur, on en donne trois : la valeur la plus probable, la valeur haute et la valeur basse.

Sur une tâche de développement, cela correspond assez naturellement à la conversation que l’on a réellement dans sa tête :

> Normalement, il me faut un jour. Mais ça fait appel à un bout du framework que je connais peu et qui ne fait peut-être pas complètement le job, donc ça peut aller jusqu’à deux jours et demi. Et je sais que je ne le ferai pas en moins d’une demi-journée.

Je l’écris simplement :

**1 ~ 2,5 ~ 0,5**

Probable, maximum, minimum.

À partir de ces estimations, on peut ensuite réaliser des calculs un peu plus solides que de simples sommes et obtenir, à l’échelle du projet, une estimation qui porte elle aussi cette notion d’incertitude.

Ce n’est d’ailleurs pas la première fois que je cherche à rendre l’incertitude manipulable : j’avais déjà exploré une approche par simulation de Monte-Carlo dans [un prototype de modélisation probabiliste construit avec Sirius Web]({{ site.url }}/modeling/guesstimate-modelisation-probabilite/).

## Ce que cela change à l’échelle du projet

Prenons un exemple :

| Tâche | Charge | Risque | Estimation à trois points |
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
| **Total** | **46** | **15** | **47,17 ~ 50,31 ~ 44,02** |
| **Charge + risques** | **61** |  | **≈ 50** |

<figure>
    <a href="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_3.png"><img src="{{ site.url }}/images/blog/2026/threepoint_estimates/estimates_3.png"></a>
    <figcaption>61 jours vs estimation à trois points</figcaption>
</figure>

Avec notre ancienne méthode, nous avions une charge de 46 jours et 15 jours de risque. En additionnant les deux, nous arrivions donc à 61 jours.

Avec le chiffrage à trois points, la valeur prévue reste très proche de notre estimation initiale, un peu plus élevée parce qu’elle tient compte du niveau d’incertitude des différentes tâches. La borne haute de l’intervalle arrive autour de 50 jours, beaucoup plus bas que les 61 jours obtenus en additionnant simplement tous les risques.

Et finalement, c’est assez logique. Pour atteindre 61 jours, il faudrait que tous les risques identifiés se matérialisent simultanément à leur maximum.

Dans cet exemple, le tableur utilise l’approximation PERT : pour chaque tâche, l’espérance vaut `(minimum + 4 × probable + maximum) / 6` et l’écart-type `(maximum - minimum) / 6`. Les variances des tâches sont ensuite additionnées, en supposant leurs incertitudes indépendantes, pour produire un intervalle d’environ 95 % autour du total attendu (`± 2 écarts-types`). **44,02 et 50,31 ne sont donc pas les minimum et maximum absolus du projet, mais les bornes de cet intervalle.**

Avec les trois chiffres — probable, minimum et maximum — on dispose donc de quelque chose qui permet beaucoup mieux de décider. On connaît la valeur autour de laquelle on pense réellement se situer, un intervalle plausible et surtout le niveau d’incertitude du projet lui-même.

La différence est déjà significative sur une dizaine de tâches. Quand il s’agit d’estimer des projets de développement sur plusieurs années, elle peut devenir massive.

## Le calcul est utile, la conversation l’est encore plus

Il y a un autre bénéfice que je trouve presque plus intéressant que le calcul lui-même : la dynamique de la discussion change complètement.

Quand on demande « donne-moi un chiffre », cela ressemble vite à un pari que l’autre doit faire. Et une fois le chiffre donné, il ressemble à un engagement.

Quand on demande une fourchette en trois points, la conversation n’est plus la même. « Combien cela devrait prendre normalement ? Qu’est-ce qui pourrait faire déborder la tâche ? Jusqu’où ? Et à l’inverse, en dessous de quoi sais-tu que tu ne descendras pas ? »

On parle alors non seulement de ce que l’on sait, mais aussi de ce que l’on ne sait pas.

Et cette information est précieuse.

Une fois le projet gagné et lancé, le chiffrage continue d’ailleurs à porter cette information pour les personnes qui vont effectivement réaliser le travail. Un **1 ~ 2,5 ~ 0,5** ne signifie pas simplement « quelqu’un avait prévu un jour ». Il signifie aussi : « cette personne pensait qu’un jour était le scénario probable, mais elle avait identifié une incertitude capable de faire monter cette tâche jusqu’à deux jours et demi ».

Je parle ici d’effort et de tâches de développement, mais cela fonctionne évidemment tout aussi bien pour des projections financières.

C’est finalement cela que j’ai appris : lorsqu’on se projette dans le futur, un chiffre unique est difficile à produire et contient assez peu d’information. Trois chiffres sont souvent beaucoup plus faciles à donner, et surtout beaucoup plus riches.

Pendant longtemps, j’ai associé la qualité d’une estimation à sa précision. Aujourd’hui, j’ai plutôt tendance à me méfier d’une estimation qui ne montre pas son incertitude.

Dans ma boîte à outils, j’ai donc maintenant quelques fichiers LibreOffice avec les macros qui vont bien pour manipuler ces chiffres simplement.

Vous pouvez télécharger ici le fichier utilisé pour cet exemple : [Estimation_Charges_3Points.ods]({{ site.url }}/posts/files/Estimation_Charges_3Points_E95-2026-v1.3.ods).

> Le classeur contient des macros LibreOffice Basic. LibreOffice peut donc vous demander de les autoriser à l’ouverture.
