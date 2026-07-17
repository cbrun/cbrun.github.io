---
layout: page
title: "Comprendre SysML v2 et ce qu'il change pour le MBSE"
seoTitle: "SysML v2 : comprendre le standard et ses enjeux"
description: "SysML v2 est désormais un standard formel de l'OMG. Découvrez sa sémantique, ses syntaxes, son API, ses outils et une démarche d'adoption pragmatique."
permalink: /fr/sysml-v2/
canonical: https://cedric.brun.io/fr/sysml-v2/
lang: fr
translation_en: /sysml-v2/
tags:
  - mbse
  - sysmlv2
  - syson
  - sirius-web
  - capella
  - obeo
cluster: sysml-v2
intent: "Comprendre ce que SysML v2 change et comment aborder son adoption"
primaryQuery: "qu'est-ce que SysML v2"
secondaryQueries:
  - "différences SysML v1 SysML v2"
  - "API SysML v2"
  - "KerML"
  - "outils SysML v2"
audience: "Responsables MBSE, architectes système et ingénieurs système"
maturityStage: "découverte et évaluation"
pagePromise: "Expliquer le standard, son impact pratique et une démarche d'adoption crédible"
proof:
  - "spécifications formelles de l'OMG"
  - "outillage SysML v2 open source"
  - "expérience dans la construction de plateformes de modélisation industrielles"
businessGoal: "Établir un point de référence stable pour le cluster éditorial SysML v2"
nextStep:
  - "/syson/"
  - "/modeling/conference-models2024/"
  - "/talk/IEEE-ISSE25/"
image:
  thumb: blog/2026/sysml-v2/sysml-v2-language.webp
---

> Cette page a été traduite automatiquement depuis la version anglaise.

SysML v2 n'est pas une retouche cosmétique de SysML v1. Le langage a été repensé autour d'une fondation sémantique plus précise, de notations textuelle et graphique standardisées, de bibliothèques réutilisables et d'une API standard pour accéder aux modèles.

Le changement pratique dépasse largement l'arrivée de quelques nouveaux diagrammes. Avec SysML v2, le modèle système devient plus facile à traiter comme une véritable donnée d'ingénierie : quelque chose que l'on peut parcourir à travers différentes vues, que les outils peuvent interroger et transformer, et auquel d'autres services peuvent se connecter grâce à une interface partagée.

[L'OMG a publié SysML 2.0 comme spécification formelle en septembre 2025](https://www.omg.org/spec/SysML/2.0), avec [KerML 1.0](https://www.omg.org/spec/KerML/1.0) et [Systems Modeling API and Services 1.0](https://www.omg.org/spec/SystemsModelingAPI/1.0). Le standard est prêt à être lu et implémenté. Les outils et les pratiques industrielles qui l'entourent continuent toutefois de mûrir. Cette distinction compte lorsque l'on prépare une adoption.

<figure>
    <a href="{{ site.url }}/images/blog/2026/sysml-v2/sysml-v2-language.webp">
      <img src="{{ site.url }}/images/blog/2026/sysml-v2/sysml-v2-language.webp" alt="Lettrage SysML v2 dessiné à la main pour présenter le nouveau standard de modélisation système">
    </a>
    <figcaption>SysML v2 apporte une nouvelle fondation à la modélisation système, pas simplement une révision de notation.</figcaption>
</figure>

## Qu'est-ce que SysML v2 ?

SysML v2 est la deuxième génération majeure du Systems Modeling Language de l'OMG. Il sert à spécifier, concevoir, analyser et vérifier des systèmes complexes, en couvrant les exigences, la structure, le comportement, les interfaces, l'analyse et la vérification.

Son objectif sera familier à toute personne qui pratique déjà le Model-Based Systems Engineering : créer un modèle cohérent qui relie les décisions d'ingénierie, plutôt que de les disperser entre des documents et des diagrammes déconnectés. Ce qui change, c'est l'architecture du langage sous-jacente.

SysML v1 était défini comme un profil d'UML. SysML v2 repose sur **KerML**, un langage de modélisation doté d'une fondation sémantique indépendante de tout domaine d'application. SysML v2 spécialise cette fondation pour l'ingénierie système et y ajoute des concepts métier, des notations et des bibliothèques standard.

C'est important, car le sens du modèle n'appartient ni à un diagramme particulier ni à l'interface d'un fournisseur. Un diagramme, un éditeur textuel, une table, un formulaire, un service d'analyse ou un client API peuvent exposer différentes parties du même modèle sémantique.

## SysML v1 et SysML v2 sont deux générations différentes

SysML v2 conserve l'ambition d'ingénierie système de SysML v1, mais il ne préserve pas à l'identique tous ses concepts ni toutes ses habitudes de modélisation.

| Sujet | SysML v1 | SysML v2 |
|---|---|---|
| Fondation | Un profil UML | Un langage construit sur KerML |
| Sémantique | Définie par les mécanismes d'extension UML et les contraintes SysML | Ancrée dans le modèle sémantique de KerML |
| Notation | Principalement une notation graphique standardisée | Des notations graphique et textuelle standardisées |
| Style de modélisation | Concepts et stéréotypes inspirés d'UML | Concepts cohérents de définition et d'utilisation |
| Réutilisation | Profils, bibliothèques de modèles et mécanismes propres aux outils | Spécialisation au niveau du langage, imports et bibliothèques standard |
| Interopérabilité | Surtout des formats d'échange et des intégrations éditeur | Une spécification standard de services et d'API de modélisation système |
| Migration | Propre à chaque outil et organisation | Une spécification normative de transformation de SysML v1 vers SysML v2 existe |

Ce tableau donne au changement un aspect bien rangé. Les vrais modèles le sont rarement. Les organisations possèdent des profils, des conventions, des règles de validation, des générateurs de documents, des intégrations, des supports de formation et des années de pratique accumulée. La spécification de transformation fournit des correspondances utiles, mais une migration ne remplace pas, d'un simple clic, la compréhension des choix qui ont été faits.

La bonne question n'est donc pas seulement : « Peut-on convertir ce modèle ? » Il faut aussi se demander : « Quelles parties de notre pratique actuelle doivent survivre, et comment doivent-elles s'exprimer dans le nouveau langage ? »

## KerML fournit la fondation sémantique du langage

[KerML](https://www.omg.org/spec/KerML/1.0) est le Kernel Modeling Language sur lequel repose SysML v2. Il fournit des constructions indépendantes du domaine pour la classification, les relations, le comportement, la structure, les espaces de noms et d'autres besoins récurrents de modélisation.

La plupart des ingénieurs système n'ont pas besoin de commencer par apprendre chaque concept de KerML. Ils doivent en revanche comprendre pourquoi il existe.

KerML sépare la fondation sémantique réutilisable du vocabulaire d'ingénierie système construit au-dessus. SysML v2 bénéficie ainsi d'une architecture plus cohérente et laisse de la place à des langages et bibliothèques spécifiques aux domaines, tout en les gardant reliés à la même fondation.

Une conséquence visible est la distinction entre **définitions** et **utilisations**. Une définition décrit un type de chose réutilisable ; une utilisation représente la manière dont cette chose intervient dans un contexte particulier. Cette distinction s'applique de façon cohérente aux parties, actions, états, exigences et autres concepts. Elle est puissante, mais peut demander un changement d'habitude aux équipes venant de SysML v1.

## Les syntaxes textuelle et graphique servent le même modèle

La notation textuelle standard est l'un des ajouts les plus visibles de SysML v2. Elle facilite la création, la revue, la comparaison, la génération et le traitement des modèles avec des infrastructures habituées au texte. La notation graphique reste essentielle pour saisir d'un coup d'oeil une architecture, un comportement ou un ensemble de relations.

Il ne faudrait pas en faire un duel entre texte et diagrammes. Chaque représentation sert un travail différent :

- le texte est efficace pour l'édition précise, l'automatisation, les exemples et les workflows orientés versions ;
- les diagrammes révèlent la structure, le contexte et les relations ;
- les tables permettent de comparer des ensembles d'éléments ;
- les formulaires guident une édition ciblée ;
- les vues dédiées peuvent incarner une méthode ou répondre à une question d'ingénierie particulière.

Le point important est que toutes ces représentations opèrent sur le même modèle. En pratique, la qualité d'un outil dépendra autant de sa navigation, de sa synchronisation, de sa validation et de son ergonomie que du nombre de concepts SysML v2 implémentés.

## L'API standard change la donne pour les intégrations

La spécification [Systems Modeling API and Services](https://www.omg.org/spec/SystemsModelingAPI/1.0) définit un modèle de services indépendant des plateformes et des liaisons propres à certaines technologies. Elle fournit aux outils une base partagée pour exposer les projets, commits, éléments de modèle, relations, requêtes et services associés.

Cela ne rend pas l'interopérabilité automatique. Deux outils peuvent implémenter des sous-ensembles différents, prendre en charge des workflows différents ou imposer des contraintes opérationnelles différentes à l'API. Mais celle-ci crée quelque chose qui manquait cruellement à l'écosystème SysML : une frontière standard pour relier les référentiels de modèles aux services d'analyse, de simulation, de gestion des exigences, de PLM, d'ALM, de reporting et d'automatisation.

L'API compte également pour l'ingénierie assistée par IA. Un agent est plus utile lorsqu'il agit sur des éléments de modèle explicites, à travers des services contrôlés, que lorsqu'il se contente de produire un texte plausible. Le modèle donne à l'interaction une structure que les ingénieurs peuvent inspecter, comparer, valider ou rejeter. J'aborde cette évolution plus large dans [ma keynote SLE 2026, « We built the languages. That was the easy part. »]({{ site.url }}/talks/sle-2026-we-built-the-languages/).

## Ce que SysML v2 ne résout pas tout seul

Un langage standard est une infrastructure nécessaire. Ce n'est ni une méthode, ni un plan d'adoption, ni une garantie de produire des modèles utiles.

SysML v2 ne décide pas :

- à quelles questions d'ingénierie vos modèles doivent répondre ;
- quels concepts et points de vue les différents rôles doivent utiliser ;
- comment la qualité des modèles est revue et gouvernée ;
- comment les responsabilités se répartissent entre équipes et fournisseurs ;
- comment relier les actifs existants SysML v1, Capella, exigences, simulation et PLM ;
- quelle part du langage chaque praticien doit apprendre ;
- quelle expérience d'outillage rendra la pratique utilisable à grande échelle.

C'est pourquoi je reste convaincu que **langage, méthode et outil doivent être considérés ensemble**. Capella et Arcadia ont montré à maintes reprises la valeur d'un guidage méthodologique pour le MBSE industriel. SysML v2 ouvre de nouvelles possibilités pour exprimer et intégrer ce guidage, mais il ne le rend pas inutile.

## SysML v2 est-il prêt pour un usage industriel ?

Le standard est formel. La maturité industrielle est une question distincte, qui dépend du contexte.

Une équipe peut lancer dès aujourd'hui un pilote SysML v2 utile. Une grande organisation doit toutefois évaluer la maturité de tout l'environnement dont elle a besoin : couverture du langage, persistance des modèles, éditions graphique et textuelle, API, contrôle d'accès, collaboration, performances, validation, migration, reporting, déploiement, support et gouvernance à long terme.

Méfiez-vous d'une simple case à cocher « compatible SysML v2 ». La conformité a plusieurs dimensions et la couverture utile dépend de votre périmètre d'ingénierie. Demandez quels concepts du langage, bibliothèques standard, notations, services API et scénarios d'échange sont pris en charge, puis testez-les avec des modèles représentatifs.

Le [dépôt officiel des versions de SysML v2](https://github.com/Systems-Modeling/SysML-v2-Release) fournit les spécifications, des exemples, des bibliothèques et des ressources liées à l'implémentation de référence. Il complète utilement les pages normatives de l'OMG lorsque l'on évalue des comportements concrets.

## Une démarche d'adoption pragmatique

J'aborderais l'adoption comme un changement d'ingénierie, pas comme un projet de conversion de fichiers.

1. **Partir des décisions et des difficultés.** Identifiez ce qui doit devenir plus cohérent, traçable, collaboratif ou automatisable.
2. **Choisir un pilote bien délimité.** Utilisez un sous-système représentatif et une vraie question d'ingénierie, tout en gardant une portée organisationnelle maîtrisable.
3. **Cartographier la pratique existante.** Inventoriez profils, bibliothèques, points de vue, règles de validation, intégrations et livrables avant de parler d'outils de migration.
4. **Évaluer ensemble la couverture du langage et celle de l'outil.** Testez les concepts SysML v2 et les workflows réellement nécessaires au pilote.
5. **Concevoir la frontière d'intégration.** Décidez où l'API standard, l'échange textuel ou des connecteurs dédiés s'insèrent dans le système d'ingénierie.
6. **Formaliser la méthode.** Définissez un guidage, des points de vue, des exemples, des revues et des responsabilités plutôt que d'exposer tout le langage à chaque utilisateur.
7. **Passer à l'échelle à partir de preuves.** Mesurez l'ergonomie, la qualité des modèles, l'interopérabilité et l'effort d'apprentissage avant d'élargir le périmètre.

Cette démarche permet aussi aux pratiques SysML v1, Capella et SysML v2 de coexister pendant une transition. Tout remplacer d'un coup est rarement la seule stratégie crédible.

## Pourquoi un outil SysML v2 open source, c'est important

Un nouveau standard ouvre une courte période pendant laquelle les outils, pratiques, bibliothèques et intégrations sont encore en train de prendre forme. L'open source rend l'implémentation inspectable et donne aux organisations un moyen de collaborer sur la fondation commune avant que ces choix ne se figent derrière des frontières propriétaires.

[Eclipse SysON]({{ site.url }}/fr/syson/) est un projet de modélisation SysML v2 open source et web, initié par Obeo et le CEA et construit sur Sirius Web. Son objectif dépasse le dessin de diagrammes SysML v2 : des éditeurs graphiques, textuels, tabulaires et à base de formulaires opèrent sur le modèle, avec l'extensibilité et l'API standard comme préoccupations de premier plan.

Pour le projet, sa gouvernance, son code source, ses versions et les moyens d'y contribuer, le [projet Eclipse SysON](https://eclipse.dev/syson/) fait référence. Pour les organisations qui évaluent la personnalisation, le déploiement, le support ou un engagement industriel, [Obeo présente ses offres SysON et son approche d'innovation ouverte](https://www.obeosoft.com/fr/produits/syson/).

Cette distinction est volontaire. Eclipse est le lieu où vit le projet open source. Obeo est l'un des acteurs auprès desquels une organisation peut obtenir une industrialisation et un accompagnement d'ingénierie autour de ce projet.

Notre objectif chez Obeo est de proposer une plateforme SysML v2 solide et entièrement open source, car nous pensons que ses promesses d'interopérabilité et de continuité du fil numérique ne peuvent pas être tenues sans cela. La modélisation elle-même devrait être libre et accessible : un terrain commun et des règles du jeu équitables pour tous les outils. Il revient aux fournisseurs d'apporter de la valeur au-dessus de cette fondation, et les possibilités ne manquent pas.

Ce parcours est documenté dans plusieurs présentations et articles de ce site :

- [la collaboration initiale entre Obeo et le CEA autour de Sirius Web, Papyrus et SysON]({{ site.url }}/modeling/sirius-papyrus-web-une-nouvelle-ere-pour-des-outils-d-ingenierie-collaborative/) ;
- [les démonstrations de Sirius Web et SysON à MODELS 2024]({{ site.url }}/modeling/conference-models2024/) ;
- [Open Source MBSE at Scale, des outils éprouvés dans l'industrie à SysML v2 web]({{ site.url }}/talk/IEEE-ISSE25/) ;
- [la réflexion de SLE 2026 sur les langages, plateformes, pratiques et agents]({{ site.url }}/talks/sle-2026-we-built-the-languages/).

## Le but n'est pas d'adopter un langage isolément

SysML v2 apporte à l'ingénierie système une fondation moderne, une notation textuelle standard, une notation graphique, des bibliothèques réutilisables et une API standard. Ce sont des avancées importantes.

La valeur viendra de ce que les organisations construiront autour : des méthodes ciblées, des vues utilisables, des intégrations fiables, des pratiques collaboratives et des modèles qui soutiennent de vraies décisions.

Le standard est désormais formel. La prochaine étape ne consiste plus à attendre que SysML v2 existe, mais à apprendre à bien le pratiquer.
