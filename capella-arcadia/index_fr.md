---
layout: page
title: "Comprendre Capella, Arcadia et leur place dans le MBSE"
seoTitle: "Capella et Arcadia : guide pratique d'un MBSE méthodologique"
description: "Comprendre comment Arcadia et Eclipse Capella fonctionnent ensemble, leurs différences avec SysML et leur place dans une pratique MBSE industrielle."
permalink: /fr/capella-arcadia/
canonical: https://cedric.brun.io/fr/capella-arcadia/
lang: fr
translation_en: /capella-arcadia/
tags:
  - capella
  - mbse
  - obeo
  - sirius-web
cluster: capella-arcadia
intent: "Comprendre Arcadia et Capella, puis évaluer si une approche MBSE guidée par la méthode convient à une organisation d'ingénierie"
primaryQuery: "Capella Arcadia MBSE"
secondaryQueries:
  - "qu'est-ce que la méthode Arcadia"
  - "qu'est-ce qu'Eclipse Capella"
  - "Capella ou SysML"
  - "Arcadia et SysML v2"
  - "collaboration web Capella"
audience: "Responsables de l'ingénierie système, architectes système, praticiens MBSE, équipes outillage et organisations évaluant Capella ou Arcadia"
maturityStage: "compréhension et évaluation"
pagePromise: "Distinguer méthode, langage, outil et plateforme, puis proposer un chemin pratique pour adopter Capella et Arcadia"
proof:
  - "déploiements industriels d'Arcadia et Capella dans des domaines d'ingénierie complexes"
  - "expérience de contribution à Capella, Sirius et leur écosystème"
  - "retours de la communauté à travers Capella Days, les formations et les projets d'intégration"
businessGoal: "Établir un point de référence stable pour le cluster consacré à Capella, Arcadia et au MBSE guidé par la méthode"
nextStep:
  - "/eclipse/adoption-croissante-MBSE-capella/"
  - "/modeling/capella-days-2024/"
  - "/mbse/ia-pour-capella-ia-agentique-comme-premier-pas/"
  - "/fr/syson/"
image:
  thumb: blog/2026/capella-arcadia/arcadia-engineering-perspectives.webp
---

> Cette version française a été traduite automatiquement à partir de l'article original en anglais, puis adaptée pour préserver son ton et son sens.

Capella et Arcadia sont souvent cités ensemble, au point de parfois donner l'impression qu'il s'agit de deux variantes de la même chose. Ce n'est pas le cas.

**Arcadia est une méthode d'ingénierie basée sur les modèles. Eclipse Capella est l'atelier open source qui implémente et soutient cette méthode.** La méthode structure les questions que se posent les ingénieurs, les perspectives qu'ils construisent et le raisonnement qui relie les besoins opérationnels à une architecture physique. L'outil fournit le langage, les vues, le guidage, la validation et l'environnement d'ingénierie nécessaires pour mettre cette approche en pratique.

Cette distinction ne relève pas seulement du vocabulaire. Un langage de modélisation peut définir ce qu'il est possible d'exprimer sans expliquer quand l'exprimer, dans quel ordre explorer un problème ou comment faire travailler ensemble plusieurs métiers de l'ingénierie. Un outil peut dessiner des diagrammes sans créer une pratique cohérente. Arcadia et Capella ont été conçus pour que méthode, langage et outil se renforcent mutuellement.

Cette approche est déployée depuis des années dans des contextes industriels exigeants. Elle soulève aussi de nouvelles questions à mesure que SysML v2, la modélisation web, les fils numériques et l'ingénierie assistée par l'IA gagnent en maturité. Une organisation doit-elle adopter Capella, un outil SysML, ou les deux ? Peut-on utiliser Arcadia avec SysML v2 ? Comment une pratique de modélisation desktop peut-elle évoluer vers des environnements plus connectés et collaboratifs ?

Cette page propose un cadre pour répondre à ces questions sans confondre méthode, standard et produit.

<figure>
    <a href="{{ site.url }}/images/blog/2026/capella-arcadia/arcadia-engineering-perspectives.webp">
      <img src="{{ site.url }}/images/blog/2026/capella-arcadia/arcadia-engineering-perspectives.webp" alt="Perspectives d'ingénierie Arcadia reliant l'analyse opérationnelle, l'analyse des besoins système, l'architecture logique et l'architecture physique à travers les exigences et les viewpoints">
    </a>
    <figcaption>Arcadia relie la compréhension des besoins opérationnels aux architectures logique et physique, tandis que les exigences et les viewpoints d'ingénierie traversent l'ensemble du raisonnement.</figcaption>
</figure>

## Commencer par distinguer méthode, langage, outil et pratique

Quatre concepts sont souvent mélangés dans les discussions sur le MBSE.

Une **méthode** organise le raisonnement d'ingénierie. Elle identifie les questions auxquelles répondre, les relations à préserver, les perspectives à construire et les vérifications qui aident les équipes à passer d'un besoin à une architecture justifiée.

Un **langage de modélisation** définit des concepts et leur sémantique : fonctions, composants, échanges, interfaces, capacités, états, exigences et relations entre ces éléments. Il détermine ce qu'un modèle peut exprimer.

Un **outil** permet aux ingénieurs de créer, parcourir, valider, transformer et communiquer ces modèles. Son expérience utilisateur peut renforcer la méthode ou, au contraire, laisser les utilisateurs seuls face à un métamodèle générique.

Une **pratique d'ingénierie** correspond à ce que fait réellement l'organisation : rôles, revues, droits de décision, gouvernance des modèles, intégration avec les autres disciplines, formation, gestion de configuration et livrables attendus.

Arcadia est d'abord la méthode, accompagnée des concepts nécessaires pour l'appliquer. Capella est l'outil et l'environnement de modélisation dédié. Aucun des deux ne dispense de définir une pratique adaptée à l'organisation.

C'est pourquoi acheter ou télécharger un outil MBSE ne signifie pas adopter le MBSE. Le changement durable apparaît lorsque les équipes partagent une façon de formuler les besoins, comparer des choix d'architecture, justifier leurs décisions et connecter le modèle au reste de l'ingénierie.

## Qu'est-ce qu'Arcadia ?

[Arcadia](https://mbse-capella.org/arcadia.html) signifie *Architecture Analysis and Design Integrated Approach*. Il s'agit d'une méthode basée sur les modèles pour l'ingénierie des architectures système, matériel et logiciel. Elle est issue de l'expérience industrielle de Thales en ingénierie système, puis a été mise à disposition au sein de l'écosystème Capella.

Arcadia structure le raisonnement d'architecture à travers des perspectives complémentaires :

1. **Analyse opérationnelle :** que doivent accomplir les utilisateurs et les autres acteurs opérationnels, dans quelles situations et sous quelles contraintes ?
2. **Analyse des besoins système :** que doit faire le système pour ces acteurs, quels services et fonctions doit-il fournir, et où se situe sa frontière ?
3. **Architecture logique :** comment le système peut-il fonctionner indépendamment des choix d'implémentation finaux, et comment organiser logiquement les responsabilités ?
4. **Architecture physique :** comment le système sera-t-il développé et construit à partir de matériel, de logiciel, de personnes, d'installations et d'autres ressources physiques ?
5. **Stratégie de réalisation :** comment organiser l'architecture en éléments de configuration et en unités d'implémentation ou d'intégration ?

Ces perspectives sont souvent présentées dans cet ordre parce que chacune fournit des éléments utiles à la suivante. Arcadia n'impose pas un cycle en cascade. Sa [foire aux questions officielle](https://mbse-capella.org/arcadia-qna.html) autorise explicitement les approches itératives, incrémentales, guidées par la réutilisation, ascendantes ou intermédiaires, tout en préservant les dépendances logiques entre les préoccupations d'ingénierie.

Les exigences ne constituent pas une phase isolée à côté de cette progression. Besoins opérationnels, attentes fonctionnelles et non fonctionnelles, choix d'architecture et exigences s'influencent mutuellement. L'objectif est de confronter suffisamment tôt les exigences à une architecture afin d'en évaluer la faisabilité et la robustesse, plutôt que de traiter le modèle comme une illustration produite après les décisions.

## Pourquoi ces perspectives sont importantes

Les perspectives provoquent des changements de question volontaires.

L'Analyse opérationnelle résiste à la tentation de définir trop tôt le système. Elle demande ce que les acteurs cherchent à accomplir avant d'affecter un comportement à une solution envisagée.

L'Analyse des besoins système identifie la contribution attendue du système et ses interactions avec les utilisateurs et les systèmes externes. Elle clarifie ce qui appartient à l'intérieur et à l'extérieur de sa frontière.

L'Architecture logique explore l'organisation possible des fonctions et des responsabilités sans s'engager prématurément sur des technologies ou des composants d'implémentation. Elle crée l'espace nécessaire aux compromis d'architecture.

L'Architecture physique alloue ensuite les comportements et les interfaces à des éléments d'implémentation concrets. Les liens entre les perspectives permettent de comprendre pourquoi un composant physique existe et quels besoins ses fonctions satisfont.

Cette progression donne aux équipes un vocabulaire commun pour les revues. Au lieu de débattre de la présence d'une boîte dans un diagramme, elles peuvent se demander si une activité opérationnelle a été traduite en une capacité système pertinente, si une responsabilité logique est justifiée ou si une allocation physique respecte les contraintes concernées.

Le modèle peut alors devenir davantage qu'un livrable. **Le modèle devient la table commune.** Des personnes aux rôles différents peuvent naviguer depuis un besoin opérationnel jusqu'à une fonction, un composant, une interface, un scénario ou une exigence, et discuter du même objet d'ingénierie plutôt que de comparer des diapositives déconnectées.

## Les viewpoints relient les préoccupations des spécialistes à l'architecture

L'architecture est façonnée par des préoccupations que l'on ne peut réduire à une seule hiérarchie : sûreté, cybersécurité, performances, coût, masse, temps réel, maintenabilité, variabilité des lignes de produits, intégration, et bien d'autres.

Arcadia est guidée par les viewpoints. Un viewpoint formalise la manière dont l'une de ces préoccupations est évaluée face à l'architecture. L'analyse des spécialistes reste ainsi connectée au modèle système partagé, tout en conservant les concepts et calculs propres à leur discipline.

L'objectif n'est pas de placer toutes les informations d'ingénierie dans un métamodèle gigantesque. Il consiste à définir des connexions maîtrisées :

- les éléments d'architecture dont dépend une préoccupation spécialisée ;
- les propriétés ou concepts supplémentaires nécessaires ;
- les analyses et règles qui peuvent être exécutées ;
- les résultats qui influencent un choix d'architecture ;
- la manière dont ce raisonnement reste traçable lors des changements.

C'est une dimension importante de l'adaptation d'Arcadia. Le cœur de la méthode fournit une structure solide, mais chaque organisation possède des contraintes métier, des standards de cycle de vie, des jalons de revue et des disciplines d'ingénierie qu'il faut intégrer délibérément.

## Qu'est-ce qu'Eclipse Capella ?

[Eclipse Capella](https://projects.eclipse.org/projects/polarsys.capella) est l'atelier graphique open source qui implémente Arcadia. La Fondation Eclipse le classe comme projet mature. Son code source, ses versions, sa gouvernance, son processus de contribution et sa licence Eclipse Public License 2.0 sont publics.

Capella fournit un langage et une expérience utilisateur dédiés à l'architecture système, plutôt qu'une surface de modélisation générique. Ses fonctionnalités comprennent :

- un navigateur méthodologique intégré et un guidage à travers les perspectives Arcadia ;
- la navigation dans le modèle sémantique et des propriétés contextuelles ;
- des représentations d'architecture, de flux de données, de chaînes fonctionnelles, de séquences, d'états, de classes, d'interfaces et d'arborescences ;
- des filtres, des calques et des simplifications calculées pour maîtriser les vues complexes ;
- des règles de validation et des transitions entre perspectives d'ingénierie ;
- des patterns, des bibliothèques, de la réutilisation et des mécanismes de transition du système vers les sous-systèmes ;
- des points d'extension pour ajouter viewpoints, représentations, règles et intégrations.

Capella est construit comme une application desktop Eclipse et s'appuie notamment sur Eclipse Sirius pour la modélisation graphique. [Capella Studio](https://mbse-capella.org/download.html) fournit un SDK pour développer des extensions et des viewpoints spécialisés.

Il faut distinguer le cœur du projet de son écosystème plus large. Des add-ons open source et commerciaux apportent la génération documentaire, la gestion des exigences, la collaboration, la simulation, la gestion de propriétés, le scripting ou les connexions avec d'autres systèmes d'ingénierie. Chaque organisation doit évaluer séparément la licence, la maintenance, la compatibilité et le modèle de support de chaque add-on.

## Mature, largement adopté et toujours en mouvement

Capella n'est pas un outil émergent en attente de ses premiers déploiements sérieux. Il a accumulé des années d'utilisation industrielle dans l'aéronautique, la défense, les transports, l'énergie, le spatial, les semi-conducteurs et d'autres domaines où les décisions d'architecture ont des conséquences durables. La méthode est enseignée, documentée et discutée à travers des livres, des formations, des webinaires, des études de cas, une communauté mondiale de praticiens et Capella Days. Cette richesse compte : les équipes peuvent apprendre non seulement de la documentation du produit, mais aussi d'organisations qui ont déjà affronté les questions d'échelle, d'intégration, de gouvernance et d'adoption.

La maturité ne doit pas être confondue avec l'immobilité. Capella reste un projet actif, avec de nouvelles versions, des investissements directs dans ses fondations et des travaux qui étendent sa place dans l'écosystème d'ingénierie. En 2026, [Obeo a renforcé son engagement pour l'avenir de Capella](https://blog.obeosoft.com/obeo-strengthens-its-commitment-to-the-future-of-capella) à travers plusieurs initiatives concrètes :

- des contributions directes à Capella 7.1 portant sur la robustesse, la sécurité, la maintenabilité, Java 21 et l'internationalisation ;
- une bibliothèque Arcadia pour SysML v2 développée avec Thales comme première fondation pour une meilleure interopérabilité ;
- le passage en open source, avec Thales, de l'add-on Capella d'intégration avec Simulink ;
- la poursuite des travaux sur l'intégration contrôlée d'une IA agentique avec Capella ;
- la préparation de la dixième édition de Capella Days, reflet d'une communauté qui continue à partager son expérience et à construire la suite.

Ce ne sont pas les signes d'un projet entrant dans un simple mode de maintenance. Ces initiatives relient l'atelier Capella éprouvé aux préoccupations actuelles : pérennité de la plateforme, adoption internationale, simulation, SysML v2, IA et collaboration ouverte.

**Capella est mature, largement adopté, toujours dynamique et là pour durer.** Cela ne signifie pas que son architecture ou son écosystème resteront figés. Cela signifie que la méthode, les modèles, les compétences, la communauté et les investissements industriels accumulés forment une base durable à partir de laquelle Capella peut continuer à évoluer.

## Pourquoi le guidage méthodologique change l'adoption

Un langage généraliste offre de la flexibilité. Il peut aussi donner à une nouvelle équipe beaucoup trop de façons valides de commencer.

Capella réduit cet espace. L'explorateur, les diagrammes, les actions disponibles, les règles de validation et les transitions reflètent les concepts et les perspectives Arcadia. Les utilisateurs n'ont pas à inventer toute une organisation de modélisation avant de décrire leur première architecture.

Ce guidage présente plusieurs avantages :

- les nouveaux arrivants apprennent une progression reconnaissable plutôt qu'un catalogue d'éléments de notation ;
- les modèles créés par différentes équipes ont davantage de chances d'utiliser des structures compatibles ;
- les revues peuvent suivre l'intention d'ingénierie plutôt que l'esthétique des diagrammes ;
- la traçabilité se construit avec l'architecture au lieu d'être reconstituée après coup ;
- les formations et les retours d'expérience peuvent être réutilisés d'une organisation à l'autre ;
- les extensions peuvent se concentrer sur les préoccupations métier tout en préservant un socle architectural commun.

Le guidage n'est pas de l'automatisation. Arcadia ne décide pas où placer la frontière du système, quelle architecture logique est la meilleure ou si un argument de sûreté est suffisant. La méthode crée un espace discipliné dans lequel les ingénieurs peuvent prendre et justifier ces décisions.

Elle doit également être adaptée avec soin. Trop peu de guidage laisse les utilisateurs produire des modèles incohérents. Trop de processus peut transformer le modèle en exercice de conformité. Un déploiement réussi identifie les principes Arcadia qui doivent rester communs et les endroits où les projets ont besoin de liberté.

## Capella et SysML ne sont pas des choix équivalents

SysML et Arcadia/Capella se recouvrent, mais n'appartiennent pas à la même catégorie.

SysML est un langage de modélisation généraliste et standardisé pour l'ingénierie système. Il fournit un large vocabulaire sémantique et, avec SysML v2, une notation textuelle et graphique moderne, une fondation KerML, des bibliothèques et une API standardisée. Il n'impose pas une méthode particulière d'ingénierie système.

Arcadia combine une méthode centrée sur l'architecture avec des concepts adaptés à cette méthode. Capella implémente ces concepts dans un atelier dédié. Il ne s'agit pas d'un profil SysML, même si son langage et ses diagrammes sont fortement influencés par UML, SysML et les cadres d'architecture. La [comparaison officielle entre Capella et SysML](https://mbse-capella.org/arcadia_capella_sysml_tool.html) explique comment Arcadia simplifie, spécialise ou enrichit certains concepts pour rester proche des pratiques de l'architecture système.

Il en résulte un compromis concret :

| Question | SysML | Arcadia et Capella |
|---|---|---|
| Rôle principal | Langage standard et généraliste de modélisation système | Ingénierie d'architecture système guidée par la méthode |
| Méthode | Aucune méthode obligatoire | Arcadia fournit des perspectives et un guidage explicites |
| Périmètre | Fondation large pour la modélisation et l'interopérabilité | Analyse opérationnelle et définition d'architecture ciblées |
| Expérience outil | Dépend de l'implémentation et de sa configuration | Capella incarne Arcadia dans son vocabulaire, ses vues et ses actions |
| Interopérabilité | Le langage et l'API standards sont des objectifs centraux | Les intégrations et transformations dépendent de la frontière recherchée |
| Adaptation | Profils, bibliothèques, viewpoints et extensions de l'outil | Adaptation d'Arcadia, viewpoints Capella, add-ons et intégrations |

La décision ne doit donc pas se réduire à compter les types de diagrammes. Demandez-vous si la priorité est une fondation sémantique et d'intégration standardisée, une pratique d'architecture éprouvée et guidée par la méthode, ou une combinaison volontaire des deux.

## Arcadia et SysML v2 peuvent être complémentaires

SysML v2 ne fait pas disparaître le besoin de méthodes. Un langage standard peut améliorer la cohérence sémantique et l'interopérabilité tout en laissant aux organisations le soin de définir comment les ingénieurs doivent l'utiliser.

Arcadia apporte précisément cette dimension : un processus de raisonnement d'architecture, une progression de perspectives, des vues dédiées et une pratique enrichie par l'expérience industrielle.

Plusieurs formes de complémentarité sont possibles :

- utiliser Capella et Arcadia pour le travail d'architecture tout en échangeant certaines informations avec un écosystème SysML plus large ;
- conserver Capella comme environnement de référence pour les programmes établis et introduire SysML v2 pour de nouvelles frontières de collaboration ou d'intégration ;
- faire correspondre certains concepts Arcadia à SysML v2 lorsqu'un objectif d'ingénierie et une équivalence sémantique clairs le justifient ;
- construire une expérience orientée Arcadia au-dessus d'une plateforme SysML v2 à l'aide de bibliothèques, de vues spécialisées, d'actions et d'un vocabulaire adapté ;
- connecter les environnements à travers des services plutôt que de rechercher une conversion complète des modèles.

Aucune de ces options n'est automatique. Des concepts qui se ressemblent ne garantissent pas une équivalence sans perte. L'identité, la décomposition, la sémantique comportementale, les données des viewpoints, l'intention graphique, les extensions et l'historique de configuration doivent tous être traités explicitement.

La bonne architecture commence par un cas d'usage : quelles équipes doivent collaborer, quelles informations doivent franchir la frontière, quel système reste la référence et quelles décisions doivent demeurer traçables ?

Pour le versant langage et standard de cette décision, voir [ce que SysML v2 change pour le MBSE]({{ site.url }}/fr/sysml-v2/).

## La place de SysON et du web

[Eclipse SysON]({{ site.url }}/fr/syson/) est un environnement de modélisation SysML v2 open source et web construit sur Sirius Web. Capella est un environnement Arcadia desktop mature. Aujourd'hui, l'un ne remplace pas directement l'autre sur le web.

La question intéressante à long terme est de préserver la valeur méthodologique acquise grâce à Capella tout en bénéficiant d'une fondation SysML v2 standard et d'une collaboration web.

Nos expérimentations autour de Sirius Web et SysON montrent une direction possible : fournir une bibliothèque orientée Arcadia et personnaliser l'explorateur, les vues, les actions et le vocabulaire présentés aux utilisateurs, tout en conservant un modèle sémantique SysML v2 sous-jacent. On peut ainsi proposer une expérience consciente de la méthode sans obliger les utilisateurs à partir d'un outil standard générique.

Ces travaux doivent être compris comme une exploration, pas comme la promesse que les modèles Capella existants peuvent déjà migrer de manière transparente vers SysON. Une adoption en production demande des réponses explicites sur la couverture sémantique, la migration, la taille des modèles, la collaboration, les extensions, la gestion de configuration et le support à long terme.

Pour les organisations disposant d'un déploiement Capella réussi, la stratégie raisonnable est généralement progressive :

1. protéger la pratique d'ingénierie actuelle et les actifs de modélisation ;
2. identifier les problèmes de collaboration ou d'intégration que le web peut résoudre ;
3. tester un échange limité ou une vue spécifique à la méthode ;
4. mesurer les pertes sémantiques, l'effort des utilisateurs et les contraintes opérationnelles ;
5. étendre uniquement là où la nouvelle frontière crée une valeur réelle.

L'avenir ne doit pas forcément imposer un choix entre une méthode utile et un standard ouvert. La valeur peut remonter vers les méthodes, les viewpoints métier, les intégrations, les analyses et l'expérience utilisateur, tandis que le socle commun de modélisation devient plus interopérable.

## Connecter Capella à l'écosystème d'ingénierie

Un modèle Capella prend davantage de valeur lorsqu'il participe au travail d'ingénierie au-delà de l'équipe d'architecture.

Les besoins d'intégration les plus courants concernent :

- les référentiels d'exigences et la traçabilité ;
- le PLM et la gestion des structures produit ;
- la simulation et l'analyse de compromis ;
- la sûreté, la cybersécurité, les performances et les disciplines spécialisées ;
- les environnements de développement logiciel et matériel ;
- la génération de documents et de rapports ;
- la revue des modèles, les baselines et la collaboration multi-utilisateur ;
- l'automatisation par scripts et services ;
- l'accès aux données pour les tableaux de bord, l'analytique et les assistants IA.

Pour chaque connexion, définissez quel système possède les données, comment les identifiants restent stables, comment les changements sont synchronisés et ce qui arrive lorsqu'une intégration échoue. Évitez de transformer le modèle Capella en copie incontrôlée de tous les référentiels externes.

Le [partenariat entre Siemens et Obeo]({{ site.url }}/obeo/siemens-obeo-partnership/) illustrait déjà en 2018 l'objectif stratégique : utiliser les modèles d'architecture tout au long du cycle de vie du produit plutôt que de les laisser comme documents isolés. À [Capella Days 2024]({{ site.url }}/modeling/capella-days-2024/), cela était devenu beaucoup plus concret à travers les fils numériques, la co-ingénierie, le diagnostic, la simulation et les cas d'usage opérationnels.

## La collaboration est une pratique avant d'être une fonctionnalité

Partager un référentiel de modèles ne produit pas automatiquement de la collaboration.

Les équipes doivent apporter des réponses explicites sur :

- la propriété du modèle et les droits de modification ;
- la décomposition entre équipes, fournisseurs et sous-systèmes ;
- les workflows de revue, d'approbation, de baseline et de publication ;
- la résolution des conflits et l'analyse d'impact ;
- la confidentialité et le contrôle d'accès ;
- la compatibilité entre les versions de Capella, des add-ons et des modèles ;
- la restauration, l'auditabilité et l'archivage à long terme ;
- la façon dont les non-modélisateurs consultent et commentent les informations d'architecture.

Le [programme de Capella Days 2025]({{ site.url }}/modeling/capella-days-2025/) montrait comment l'écosystème passe d'une adoption isolée de l'outil à un véritable socle d'entreprise : intégrations entre disciplines, réutilisation des modèles, lignes de produits, boucles de sûreté et de cybersécurité, et connaissance accessible aux non-spécialistes.

L'outil peut soutenir ces workflows, mais l'organisation doit les définir. Une petite équipe d'architecture, un programme de défense impliquant plusieurs entreprises et une organisation en ligne de produits ont besoin de modèles de collaboration différents.

## L'IA bénéficie d'un modèle conscient de la méthode

Les modèles structurés donnent aux systèmes d'IA un meilleur contexte qu'une collection de documents déconnectés. Arcadia ajoute une couche utile : le modèle ne contient pas seulement des entités et des relations, mais une progression d'ingénierie et un vocabulaire qui aident à comprendre pourquoi l'information existe.

Cela ouvre des scénarios d'assistance utiles : parcourir les dépendances, retrouver le contexte d'architecture, préparer des requêtes, rédiger de la documentation, vérifier la cohérence ou proposer des modifications limitées.

Cela ne transforme pas l'IA en ingénieur système. Les décisions sur les besoins, l'architecture, la sûreté, les compromis et l'acceptation restent sous responsabilité humaine. Toute intégration de l'IA doit préserver le contrôle d'accès, la traçabilité, la revue et des limites explicites sur ce qu'un agent peut lire ou modifier.

Nos travaux sur [l'IA agentique comme premier pas pour Capella]({{ site.url }}/mbse/ia-pour-capella-ia-agentique-comme-premier-pas/) suivent ce principe : exposer certaines capacités à travers des services contrôlés, laisser les ingénieurs valider les résultats et construire la confiance à partir d'interactions utiles et circonscrites.

## Un chemin d'adoption pragmatique

L'adoption d'Arcadia et de Capella doit être conduite comme une évolution de la pratique d'ingénierie, pas comme le déploiement d'un logiciel.

1. **Choisissez un problème de décision.** Sélectionnez une question d'architecture pour laquelle un meilleur raisonnement partagé peut créer une valeur mesurable.
2. **Définissez les objectifs de modélisation.** Précisez ce que le modèle doit aider les équipes à comprendre, décider, vérifier ou produire.
3. **Délimitez les perspectives Arcadia.** Décidez quels besoins opérationnels, système, logiques et physiques sont nécessaires pour le premier cas d'usage.
4. **Établissez les conventions.** Définissez le nommage, la décomposition, le rôle des diagrammes, les règles de revue et la traçabilité requise.
5. **Formez avec un modèle représentatif.** Enseignez ensemble la méthode et l'outil à partir d'un travail pertinent pour le domaine, pas seulement d'exercices de notation.
6. **Démontrez une intégration.** Connectez une analyse aval, une source d'exigences, un rapport ou un workflow collaboratif qui prouve la valeur opérationnelle du modèle.
7. **Planifiez la gouvernance et le support.** Attribuez la responsabilité des modèles, add-ons, versions, règles de validation, migrations et de l'assistance aux utilisateurs.
8. **Mesurez les décisions et le flux.** Suivez la qualité des revues, les incohérences découvertes, le travail évité, l'intégration des nouveaux utilisateurs et la réutilisation plutôt que le nombre de diagrammes produits.
9. **Passez à l'échelle à partir des preuves.** Étendez la pratique à davantage d'équipes et de disciplines seulement lorsque le premier périmètre résiste à de vrais changements et à de vraies revues.

Ce chemin garde le périmètre initial maîtrisable sans le réduire à une démonstration jetable.

## Comment évaluer Capella pour votre organisation

Avant de choisir Capella, évaluez l'ensemble de la solution envisagée.

### Adéquation de la méthode

- L'accent mis par Arcadia sur les besoins opérationnels et l'architecture correspond-il à vos objectifs d'ingénierie ?
- Quelles parties de la méthode doivent être adaptées et lesquelles doivent rester communes ?
- Les responsables de l'ingénierie peuvent-ils soutenir les revues et les évolutions organisationnelles nécessaires ?

### Adéquation de l'outil et du modèle

- Des modèles représentatifs peuvent-ils être parcourus, modifiés, validés et revus avec des performances acceptables ?
- Les représentations principales couvrent-elles les préoccupations d'architecture nécessaires ?
- Quels add-ons, viewpoints, scripts ou intégrations sont indispensables ?

### Adéquation au cycle de vie

- Comment les modèles seront-ils décomposés, versionnés, placés en baseline, migrés et archivés ?
- Comment les exigences, le PLM, la simulation, la sûreté, le logiciel et le matériel s'y connecteront-ils ?
- Les utilisateurs qui n'emploient pas Capella peuvent-ils accéder aux informations d'architecture dont ils ont besoin ?

### Modèle opérationnel

- Qui maintient la configuration de la méthode, les modèles, les extensions et les intégrations ?
- Quels composants sont open source, commerciaux ou propres à l'organisation ?
- Quels engagements de support, de formation et de migration sont disponibles ?

### Options futures

- Quelles données doivent rester portables ou accessibles à travers des interfaces stables ?
- Où SysML v2 pourrait-il améliorer l'interopérabilité sans perturber la pratique actuelle ?
- Quels workflows web ou assistés par l'IA résolvent un véritable problème plutôt que de suivre une tendance technologique ?

La réponse peut être d'adopter largement Capella, de l'utiliser sur un périmètre architectural limité, de l'associer à d'autres environnements de modélisation ou de conserver une pratique existante. L'important est de rendre explicites les choix de méthode et de cycle de vie.

## La méthode est ce qui survit à l'outil

Capella compte parce qu'il a rendu Arcadia concret, transmissible et utilisable à l'échelle industrielle. Arcadia compte parce qu'il donne aux ingénieurs plus qu'un vocabulaire : une progression pour transformer des besoins opérationnels en une architecture justifiée.

Autour d'eux, un écosystème de formations, de livres, d'extensions, d'intégrations, d'études de cas, d'événements, de mainteneurs et de services professionnels transmet la pratique d'une équipe à l'autre. Cette transmission est aussi importante que le métamodèle.

Lorsque l'adoption fonctionne, les personnes finissent par ne plus parler de l'outil lui-même. Elles utilisent le langage partagé pour comparer les options, poser leurs questions et prendre des décisions ensemble.

Capella a atteint le point où maturité et renouvellement se renforcent mutuellement : l'expérience industrielle stabilise les fondations, tandis que de nouveaux contributeurs, intégrations, standards et modes d'interaction maintiennent la pertinence de l'écosystème. Son avenir ne consiste pas à préserver une application desktop inchangée, mais à transmettre une méthode éprouvée et un corpus vivant de connaissances d'ingénierie.

Voilà la place durable de Capella et Arcadia dans le MBSE : non pas une notation isolée ou une usine à diagrammes, mais un environnement conscient de la méthode qui construit l'architecture comme un actif d'ingénierie partagé.
