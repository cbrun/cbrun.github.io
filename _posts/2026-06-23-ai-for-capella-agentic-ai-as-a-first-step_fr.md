---
layout: post
title: "IA pour Capella : l'IA agentique comme premier pas"
categories:
  - modeling
tags:
  - capella
  - mbse
  - obeo
  - ai
  - arcadia
permalink: /mbse/ia-pour-capella-ia-agentique-comme-premier-pas/
translation_en: /mbse/ai-for-capella-agentic-ai-as-a-first-step/
excerpt: "Un regard concret sur l'IA pour Capella pour les équipes MBSE, avec un premier pas autour d'agents contrôlés qui laissent les ingénieurs responsables des décisions de modèle."
---

> Cet article a été traduit automatiquement depuis la version anglaise.

Ces derniers mois, nous avons expérimenté plusieurs façons dont l'IA pourrait être utile dans de vrais workflows Capella. Un point est devenu très clair, très vite : la valeur n'est pas de laisser l'IA *faire de l'ingénierie système*, mais d'aider les ingénieurs à interagir plus efficacement avec les modèles, tout en gardant le contrôle des décisions d'ingénierie.

En ingénierie système, les décisions demandent de l'expertise, du jugement, de la responsabilité et de la collaboration. L'IA peut aider les ingénieurs à mieux comprendre les modèles, à naviguer dans la complexité, à accéder à l'information et à automatiser des tâches répétitives. Mais les ingénieurs doivent rester aux commandes des décisions.

C'est là que l'outil [Capella](https://mbse-capella.org/) et la méthode Arcadia font vraiment la différence. Ils apportent un contexte d'ingénierie structuré, dans lequel l'IA peut être utile sans devenir incontrôlable. L'IA peut aider à formuler une requête, préparer une action ou suggérer une prochaine étape. Capella reste l'environnement dans lequel le modèle est consulté et modifié. L'ingénieur reste responsable de la validation.

Au cours des derniers mois, nous avons exploré plusieurs cas d'usage de l'IA autour de Capella. Parmi eux, un sujet s'est imposé comme un premier pas particulièrement prometteur : permettre à des agents IA d'interagir avec Capella de façon contrôlée et sécurisée.

Dans cet article, j'aimerais partager la direction que nous prenons, et pourquoi notre premier pas orienté produit consiste à **rendre Capella accessible aux agents IA** de manière contrôlée, explicite et sécurisée. Ce travail a vocation à devenir progressivement disponible à travers une **offre commerciale à partir de fin juillet 2026**.

## Notre vision derrière l'IA pour Capella

À mesure que les systèmes deviennent plus complexes, les modèles ne sont plus seulement des artefacts de documentation graphique. Ils deviennent des actifs d'ingénierie partagés, qui capturent des architectures, des exigences, des analyses, des interfaces, des points de vue et des décisions de conception.

Dans le même temps, l'importance croissante des modèles apporte de nouveaux défis :

- **Apprendre** les méthodes et les outils MBSE reste difficile pour les nouveaux arrivants.
- Les grands modèles peuvent être difficiles à **comprendre** et à **parcourir**.
- L'information existe dans le modèle, mais elle n'est pas toujours simple à **retrouver**.
- **Maintenir** la cohérence d'architectures qui évoluent demande un effort continu.
- **Produire de la documentation** et **communiquer** les décisions d'ingénierie prend encore beaucoup de temps.

Ces défis rendent l'IA particulièrement pertinente. Non pas parce qu'elle pourrait remplacer l'ingénierie système, mais parce qu'**elle peut aider les ingénieurs à interagir plus efficacement avec leurs modèles.**

<figure>
    <a href="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-driven-mbse.png">
      <img src="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-driven-mbse.png" alt="MBSE piloté par l'IA">
    </a>
</figure>

Les modèles Capella constituent aussi une **base précieuse pour l'IA** : ils contiennent une connaissance d'ingénierie structurée et traçable, qui donne à l'IA accès à un contexte fiable. Cela permet une assistance plus pertinente et plus utile que ce que l'on pourrait obtenir à partir d'informations non structurées seules.

Pour être utile dans un contexte industriel, l'IA doit toutefois répondre à plusieurs exigences clés :

- **Contextualisée**, avec accès aux informations d'ingénierie pertinentes.
- **Contrôlée**, en opérant dans des limites définies.
- **Auditable**, pour permettre aux ingénieurs de comprendre et de justifier les résultats.
- **Intégrée**, en s'inscrivant naturellement dans les workflows existants.
- **Validée par l'humain**, les ingénieurs conservant la responsabilité finale.

<figure>
    <a href="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/integrated-ai.png">
      <img src="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/integrated-ai.png" alt="IA intégrée aux workflows d'ingénierie">
    </a>
</figure>

Ces principes nous aident à distinguer les cas d'usage IA intéressants en démonstration de ceux qui peuvent, de façon réaliste, devenir utiles dans un environnement d'ingénierie. Plusieurs directions méritent d'être explorées :

- Onboarding et accompagnement méthodologique.
- Requêtes en langage naturel.
- Documentation assistée.
- Assistance contextualisée dans l'éditeur.
- Revue de modèle et vérification de cohérence.
- Assistance à la navigation.

Ce sont les domaines dans lesquels nous voyons aujourd'hui le plus fort potentiel pour aider les ingénieurs à travailler plus efficacement avec leurs modèles.

Pour soutenir cette vision, nous commençons par une capacité fondatrice : permettre à des agents IA externes d'interagir avec Capella via un ensemble contrôlé de services, autrement dit de l'IA agentique pour Capella. Plutôt que de construire un assistant pour un scénario prédéterminé, cette approche donne aux organisations un moyen de connecter leur propre environnement IA à Capella. Techniquement, cela repose sur des API, MCP et des mécanismes d'intégration similaires.

Fonctionnellement, l'objectif est simple : exposer certaines capacités de Capella aux agents, sans leur donner un accès illimité aux modèles.

Cela crée une fondation sécurisée et extensible, sur laquelle plusieurs capacités d'assistance par l'IA pourront être construites progressivement, tout en préservant la gouvernance, la traçabilité et la rigueur d'ingénierie attendues dans les environnements industriels.

## Capella comme plateforme prête pour les agents

Notre première offre **AI for Capella** se concentre sur une idée simple : faire de Capella une plateforme prête pour les agents.

Plutôt que d'intégrer un assistant IA spécifique dans Capella, nous permettons à Capella d'interagir avec l'écosystème IA choisi par chaque organisation, qu'il s'agisse de Claude, Codex, Mistral, d'un modèle hébergé localement ou de futures plateformes d'agents.

La première étape consiste à **connecter** Capella à des agents IA externes via MCP, des API et des mécanismes d'intégration similaires.

<figure>
    <a href="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-agent-for-capella.png">
      <img src="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-agent-for-capella.png" alt="Agent IA pour Capella">
    </a>
</figure>

Un agent pourrait, par exemple, demander à Capella des informations sur des éléments de modèle sélectionnés, récupérer du contexte architectural, aider à naviguer dans les dépendances, préparer une requête ou rédiger une proposition de modification du modèle. Ces actions restent limitées aux capacités explicitement exposées par Capella. Combiné avec l'accès à des documents, bases de connaissance, dépôts et outils d'entreprise, cela donne aux agents un contexte d'ingénierie beaucoup plus riche.

Mais la connectivité ne suffit pas. Dans les environnements industriels, le contrôle est essentiel : l'IA peut assister les ingénieurs, mais les ingénieurs restent responsables des décisions. C'est pourquoi les capacités exposées aux agents doivent être explicites et limitées.

Livrée comme un add-on léger, configurable et supporté pour Capella Desktop, AI for Capella permettra aux organisations de connecter leurs agents IA préférés, tout en bénéficiant d'une intégration sécurisée, maintenable et prête pour l'entreprise.

<figure>
    <a href="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-for-capella.png">
      <img src="{{ site.url }}/images/blog/2026/ai-for-capella-agentic-ai-as-a-first-step/ai-for-capella.png" alt="AI for Capella">
    </a>
</figure>

## À suivre !

Cette première version, prévue pour la **fin juillet 2026**, établira la fondation de notre feuille de route **AI for Capella** plus large, ainsi que des futures capacités d'assistance par l'IA que nous prévoyons d'introduire progressivement.

Nous sommes encore au début de ce chemin, et les capacités les plus utiles ne viendront pas de la technologie seule. Elles viendront d'une compréhension fine des pratiques d'ingénierie réelles, des contraintes de déploiement, des attentes de sécurité et du niveau de confiance requis par les équipes industrielles.

Si ces questions font écho à vos propres initiatives MBSE, nous serions ravis d'échanger avec vous, de partager ce que nous construisons et de recueillir vos retours sur les premières capacités AI for Capella.

N'hésitez pas à [nous contacter](https://www.obeosoft.com/en/contact/) pour poursuivre la conversation.
