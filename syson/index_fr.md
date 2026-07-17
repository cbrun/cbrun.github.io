---
layout: page
title: "Eclipse SysON : un environnement de modélisation SysML v2 open source"
seoTitle: "Eclipse SysON : le modeleur SysML v2 open source"
description: "Découvrez Eclipse SysON, son environnement web SysML v2 open source, son architecture et les critères pour l'évaluer dans un contexte MBSE industriel."
permalink: /fr/syson/
canonical: https://cedric.brun.io/fr/syson/
lang: fr
translation_en: /syson/
tags:
  - mbse
  - sysmlv2
  - syson
  - sirius-web
  - capella
  - obeo
cluster: syson
intent: "Comprendre ce que propose Eclipse SysON et déterminer s'il convient à une initiative SysML v2"
primaryQuery: "Eclipse SysON"
secondaryQueries:
  - "outil SysML v2 open source"
  - "modélisation SysML v2 web"
  - "fonctionnalités SysON"
  - "SysON et Capella"
audience: "Responsables MBSE, architectes système, ingénieurs système et équipes de plateformes de modélisation"
maturityStage: "évaluation"
pagePromise: "Distinguer le projet open source, ses capacités actuelles, son architecture et les services industriels disponibles autour de lui"
proof:
  - "projet et gouvernance de la Fondation Eclipse"
  - "code source, documentation, versions et suivi des tickets publics"
  - "expérience dans la construction de SysON et Sirius Web"
businessGoal: "Établir un point de référence stable pour le cluster éditorial Eclipse SysON"
nextStep:
  - "/fr/sysml-v2/"
  - "/modeling/conference-models2024/"
  - "/talk/IEEE-ISSE25/"
image:
  thumb: blog/2026/syson/syson-modeling-environment.webp
---

> Cette page a été traduite automatiquement depuis la version anglaise.

Eclipse SysON est un environnement de modélisation web et open source pour créer, éditer et visualiser des modèles SysML v2. Il est construit sur Eclipse Sirius Web et développé comme un projet de la Fondation Eclipse, avec un code source, une documentation, des versions, des discussions et une gouvernance publics.

Cette courte définition compte, car plusieurs questions différentes sont souvent mélangées. SysON est l'implémentation d'un environnement de modélisation, pas le standard SysML v2 lui-même. C'est un projet open source, pas une méthode. Et si les organisations peuvent utiliser et étendre directement le projet, elles peuvent aussi obtenir des services d'industrialisation, de déploiement, de personnalisation et de support auprès d'entreprises qui participent à son développement.

Si vous cherchez d'abord à comprendre le langage plutôt qu'à évaluer un outil, commencez par [ce que SysML v2 change pour le MBSE]({{ site.url }}/fr/sysml-v2/). Cette page se concentre sur SysON : pourquoi il existe, comment il fonctionne, ce qu'il permet déjà et ce qu'il faut vérifier avant de l'adopter.

<figure>
    <a href="{{ site.url }}/images/blog/2026/syson/syson-modeling-environment.webp">
      <img src="{{ site.url }}/images/blog/2026/syson/syson-modeling-environment.webp" alt="Interface web d'Eclipse SysON montrant l'explorateur d'un modèle SysML v2, une vue graphique et le panneau de propriétés">
    </a>
    <figcaption>Un modèle SysML v2 dans Eclipse SysON, avec l'explorateur, une représentation graphique et les propriétés contextuelles réunis dans le même environnement web.</figcaption>
</figure>

## Pourquoi Eclipse SysON existe

SysML v2 change bien plus que les symboles disponibles dans un diagramme. Sa fondation KerML, ses notations textuelle et graphique, ses bibliothèques standard et la Systems Modeling API créent les bases de modèles que l'on peut exposer à travers plusieurs vues et connecter à un système d'ingénierie plus large.

Cette promesse a besoin d'une implémentation que chacun puisse inspecter, tester, adapter et améliorer collectivement. Obeo et le CEA ont lancé SysON pour fournir une telle implémentation open source à la communauté MBSE. Le CEA a apporté son expérience de Papyrus et des standards ; Obeo, son expérience de Sirius, Capella et des plateformes de modélisation web. Le projet vit désormais sous la gouvernance de la Fondation Eclipse.

Le but n'est pas simplement de reproduire un éditeur de diagrammes desktop dans un navigateur. Un environnement web peut réduire les contraintes d'installation, donner aux équipes un point d'accès commun et faciliter la collaboration autour du même référentiel de modèles. Il fournit également une fondation architecturale pour des vues spécialisées, des intégrations et des expériences adaptées à chaque organisation.

La [page du projet Eclipse SysON](https://projects.eclipse.org/projects/modeling.syson) fait référence pour la gouvernance, le statut du projet, ses participants, ses versions et ses licences. Le [code source et le suivi des tickets](https://github.com/eclipse-syson/syson) sont publics sur GitHub.

## SysON est construit sur Sirius Web

SysON utilise [Eclipse Sirius Web](https://eclipse.dev/sirius/sirius-web.html) comme plateforme de modélisation. Sirius Web fournit des capacités réutilisables pour explorer les modèles, construire des représentations graphiques, éditer des propriétés, créer des formulaires et des tables, valider les données, exécuter des opérations d'édition et bâtir une application web.

SysON ajoute par-dessus le langage et l'expérience d'ingénierie système : le métamodèle SysML v2, les concepts standard, les bibliothèques, les vues, les outils de création, les règles du domaine et les workflows nécessaires à la manipulation des modèles système.

Cette séparation est importante pour l'extensibilité. Une équipe n'a pas besoin de forker chaque partie de l'application pour introduire une représentation ciblée ou un comportement propre à son domaine. La plateforme est conçue pour que les applications basées sur les modèles puissent proposer différentes expériences au-dessus de données sémantiques structurées.

Cela signifie aussi que SysON bénéficie de capacités développées pour une famille plus large d'applications de modélisation. Dans l'autre sens, les besoins découverts lors de l'implémentation de SysML v2 peuvent renforcer Sirius Web comme plateforme.

## Que peut-on faire avec SysON ?

SysON fournit un environnement de projets et de modèles dans lequel les ingénieurs peuvent créer des éléments SysML v2, parcourir leur structure sémantique, éditer leurs propriétés et travailler à travers des représentations graphiques et structurées.

La [documentation utilisateur de SysON](https://doc.mbse-syson.org/syson/v2026.5.0/user-manual/index.html) décrit des vues répondant à différents besoins d'ingénierie : structure générale, interconnexions, flux d'actions, transitions d'états, séquences, géométrie, grilles et navigation hiérarchique. La couverture et la maturité varient selon les vues et les versions ; cette liste ne signifie donc pas que tous les concepts SysML v2 sont implémentés au même niveau.

Parmi les capacités pratiques à évaluer :

- créer et organiser des projets et des éléments de modèle SysML v2 ;
- parcourir les définitions, utilisations, relations et structures de contenance ;
- éditer à travers des vues graphiques et des panneaux de propriétés contextuels ;
- utiliser, lorsqu'ils sont disponibles, des tables, grilles, formulaires et autres représentations structurées ;
- exécuter des règles de validation et examiner les problèmes du modèle ;
- importer et exporter les formats textuels ou d'échange SysML v2 pris en charge ;
- partager l'accès à un environnement de modélisation hébergé sur le web ;
- étendre les vues et les workflows pour un contexte d'ingénierie particulier.

SysON publie fréquemment de nouvelles versions. Pour connaître précisément le niveau de support, utilisez la documentation correspondant à la version que vous prévoyez de déployer et testez-la avec un modèle représentatif. Une simple étiquette « compatible SysML v2 » n'est pas assez précise pour prendre une décision d'ingénierie.

## Modélisations graphique et textuelle sont complémentaires

SysML v2 définit des notations graphique et textuelle. La force actuelle de SysON est une expérience web intégrée avec des éditeurs graphiques et structurés. Il prend aussi en charge une partie de la syntaxe textuelle dans l'édition directe et les workflows d'échange, tandis que des capacités d'édition textuelle plus profondes continuent d'évoluer.

Ce n'est pas une raison pour choisir une notation et exclure l'autre. Le texte est utile pour les exemples précis, l'automatisation, les revues, la génération et les workflows orientés versions. Les diagrammes révèlent l'architecture et les relations. Les formulaires et les tables concentrent l'attention sur une question délimitée. La valeur vient de l'alignement de toutes ces représentations avec le même modèle sémantique.

Lorsque vous évaluez SysON, testez les passages d'une représentation à l'autre. Un ingénieur peut-il retrouver l'élément sémantique derrière un noeud de diagramme ? Une modification apparaît-elle de façon cohérente ailleurs ? Un résultat de validation permet-il de revenir à l'élément concerné ? Ces workflows comptent davantage qu'un long inventaire de symboles de notation.

## Qu'en est-il de l'API standard SysML v2 ?

La spécification Systems Modeling API and Services est stratégiquement importante pour SysON. Elle définit une frontière standard pour accéder aux référentiels de modèles et les connecter aux services d'analyse, de simulation, de gestion des exigences, de PLM, d'ALM, de reporting et d'automatisation.

Le projet implémente progressivement ce standard. La [documentation des API SysON](https://doc.mbse-syson.org/syson/v2026.5.0/developer-guide/api/api.html) distingue le travail sur l'API REST standard des API GraphQL héritées de la plateforme applicative. Elles ne sont pas interchangeables : l'une vise l'interopérabilité dans l'écosystème SysML v2, tandis que les autres répondent aux besoins de l'application et de ses extensions dans la pile SysON.

Avant de planifier une intégration, vérifiez les services API précisément pris en charge par la version que vous comptez utiliser. Si un service standard nécessaire n'est pas encore disponible, l'échange textuel ou une intégration dédiée peut fournir une frontière viable, mais ce choix doit être explicite.

## SysON est-il vraiment open source ?

Oui. SysON est développé publiquement comme un projet Eclipse. Son code source, ses tickets, ses discussions, son guide de contribution, son historique de versions et ses licences sont accessibles sans accord commercial. Le projet est principalement distribué sous Eclipse Public License 2.0, les détails des licences étant maintenus dans le dépôt.

Open source ne signifie pas que le déploiement, l'exploitation, la sécurité, l'intégration, la migration ou le support se font tout seuls. Cela signifie que la fondation commune de modélisation peut être inspectée et modifiée, et que les organisations peuvent collaborer sans faire d'un fournisseur unique le seul propriétaire de l'éditeur de modèles.

Cette distinction est au coeur du projet. SysML v2 promet une meilleure interopérabilité et un environnement d'ingénierie numérique plus connecté. Une implémentation ouverte donne à la communauté un espace partagé pour mettre ces promesses à l'épreuve et améliorer le terrain commun.

## Projet Eclipse et offres commerciales sont deux choses différentes

Le projet Eclipse est la source de référence pour le code, la gouvernance, les versions, les contributions et les discussions communautaires. Ce doit être le premier lien pour quiconque souhaite comprendre SysON lui-même ou y participer.

Les organisations ont souvent besoin de travail supplémentaire autour du projet : distributions packagées, déploiements contrôlés, intégration des identités et des accès, supervision, sauvegardes, mises à jour, engagements de support, points de vue propres à une méthode, migration ou connexions avec le reste du système d'ingénierie.

[Obeo présente ses services et ses offres autour de SysON](https://www.obeosoft.com/fr/produits/syson/) pour répondre à ces préoccupations industrielles. D'autres organisations peuvent également construire des services au-dessus du projet open source. L'existence de valeur commerciale autour de SysON ne change ni la gouvernance ni la disponibilité du code Eclipse.

## Comment SysON s'articule avec Capella et Papyrus

SysON n'a pas vocation à rendre obsolète du jour au lendemain chaque environnement MBSE existant.

Papyrus possède une longue histoire de support des standards de modélisation de l'OMG et un écosystème d'extensions d'ingénierie. Capella associe la méthode Arcadia à un environnement ciblé et a démontré que langage, méthode et outil doivent se renforcer mutuellement dans les déploiements industriels.

SysON ouvre des possibilités pour relier ces écosystèmes à SysML v2 plutôt que de considérer la migration comme un remplacement unique. Le périmètre du projet inclut explicitement l'intégration avec Papyrus et Capella. L'approche exacte dépend de l'objectif d'ingénierie : échanger des modèles, co-concevoir entre plusieurs langages, réutiliser des concepts méthodologiques, exposer des vues spécialisées ou intégrer par des services.

Dans notre présentation [Open Source MBSE at Scale]({{ site.url }}/talk/IEEE-ISSE25/), Asma Charfi et moi avons décrit cette progression depuis des outils MBSE open source éprouvés vers des environnements SysML v2 web. Les [démonstrations de MODELS 2024]({{ site.url }}/modeling/conference-models2024/) donnent une vision plus concrète de Sirius Web et SysON en action.

## Comment évaluer SysON

Commencez par une question d'ingénierie délimitée, pas par une visite générique du produit.

1. **Choisissez un modèle représentatif.** Incluez les définitions, utilisations, relations, comportements et exigences qui comptent pour votre pratique.
2. **Listez les vues nécessaires.** Identifiez quels rôles ont besoin de diagrammes, formulaires, tables, texte ou tableaux de bord ciblés.
3. **Vérifiez la couverture du langage.** Utilisez la documentation de la version évaluée et testez directement les concepts importants.
4. **Testez les workflows collaboratifs.** Examinez l'onboarding, les accès concurrents, la revue, la validation, les permissions et les attentes de restauration.
5. **Exercez les échanges et les API.** Prouvez les intégrations nécessaires avec les exigences, l'analyse, la simulation, le PLM, l'ALM et le reporting.
6. **Évaluez l'extensibilité.** Prototypez un point de vue ou une règle propre à votre organisation plutôt que de supposer que la personnalisation sera simple.
7. **Préparez l'exploitation.** Décidez qui est responsable du déploiement, des mises à jour, de l'observabilité, des sauvegardes, des correctifs de sécurité et du support utilisateur.
8. **Distinguez maturité du projet et maturité de la solution.** Un déploiement intégré et supporté peut présenter des caractéristiques opérationnelles différentes d'une construction brute du projet.

Cette démarche révèle si SysON correspond réellement à la pratique que vous souhaitez établir. Elle produit aussi des retours utiles pour le projet open source lorsqu'un élément manque.

Gardez à l'esprit que nous publions une nouvelle version toutes les huit semaines. Le projet avance donc vite et une capacité encore absente peut arriver rapidement. Vous pouvez aussi contribuer à la faire exister grâce au [développement sponsorisé et à l'innovation ouverte](https://www.obeosoft.com/fr/societe/open-innovation/).

## Comment démarrer et contribuer

Utilisez les ressources officielles selon votre besoin :

- la [page du projet Eclipse](https://projects.eclipse.org/projects/modeling.syson) pour sa gouvernance et son identité ;
- le [site de SysON](https://mbse-syson.org/) comme point d'entrée du projet ;
- la [documentation utilisateur et développeur](https://doc.mbse-syson.org/syson/v2026.5.0/) pour l'installation, les fonctionnalités, les API et les guides d'extension ;
- le [dépôt GitHub](https://github.com/eclipse-syson/syson) pour le code source, les versions, les tickets et les discussions ;
- la [page SysON d'Obeo](https://www.obeosoft.com/fr/produits/syson/) pour le support professionnel et les offres industrielles.

Vous pouvez commencer comme utilisateur, signaler un problème avec un exemple reproductible, discuter d'un cas d'usage, améliorer la documentation ou contribuer au code. Dans un écosystème émergent, un retour précis sur un vrai workflow d'ingénierie vaut autant qu'une demande de fonctionnalité isolée de plus.

## L'objectif plus large

SysON s'inscrit dans une transition plus vaste. Les outils d'ingénierie système évoluent d'applications desktop isolées vers des plateformes de modélisation partagées et connectées à l'environnement d'ingénierie numérique. SysML v2 fournit un nouveau langage et une nouvelle fondation d'interopérabilité ; SysON explore ce qu'une implémentation ouverte et web de cette fondation peut devenir.

Sa valeur ne doit pas seulement être jugée au nombre d'éléments de diagramme qu'il sait dessiner aujourd'hui. Le vrai test consiste à savoir si les équipes peuvent construire autour de lui des pratiques fiables : vues utilisables, collaboration maîtrisée, interopérabilité transparente, méthodes explicites et intégrations qui gardent le modèle relié aux décisions d'ingénierie.

Ce travail continue d'avancer. Le fait qu'il se déroule ouvertement est précisément ce qui rend SysON stratégiquement intéressant.
