---
layout: page
title: "Rendre l'open source durable pour l'industrie"
seoTitle: "Open source industriel : gouvernance, financement et confiance"
description: "Un guide pour évaluer la gouvernance, le financement, la maintenance, la sécurité et la réversibilité d'une infrastructure open source industrielle."
permalink: /fr/open-source-industrial/
canonical: https://cedric.brun.io/fr/open-source-industrial/
lang: fr
translation_en: /open-source-industrial/
tags:
  - obeo
  - mbse
  - sirius-web
  - capella
cluster: open-source-industrial
intent: "Évaluer si un projet open source peut devenir une infrastructure industrielle fiable"
primaryQuery: "open source industriel"
secondaryQueries:
  - "gouvernance open source"
  - "modèle économique open source durable"
  - "open source dépendance fournisseur"
  - "gouvernance Fondation Eclipse"
  - "Cyber Resilience Act open source"
audience: "Directions de l'ingénierie, responsables produit, architectes, équipes achats et organisations dépendant de logiciels open source stratégiques"
maturityStage: "évaluation et conception du modèle opérationnel"
pagePromise: "Fournir un cadre pratique pour évaluer et pérenniser les logiciels open source employés dans des systèmes industriels à longue durée de vie"
proof:
  - "vingt ans de construction et de maintenance de projets open source Eclipse"
  - "adoption industrielle de technologies de modélisation telles que Sirius, Capella et SysON"
  - "expérience de l'alignement entre projets communautaires, produits commerciaux et services"
businessGoal: "Établir un point de référence stable pour le cluster consacré à l'open source industriel et à la gouvernance Eclipse"
nextStep:
  - "/on-being-open-and-transparent/"
  - "/eclipse/obeo-dix-ans/"
  - "/eclipse/ocx-open-community-experience-2024-fr/"
image:
  thumb: blog/2026/open-source-industrial/open-innovation-industrial-ecosystem.webp
---

> Cette version française a été traduite automatiquement à partir de l'article original en anglais, puis adaptée pour préserver son ton et son sens.

Publier du code source sous une licence open source est une décision importante. Ce n'est pas, à lui seul, une stratégie industrielle.

L'industrie ne dépend pas d'un dépôt de code. Elle dépend d'un logiciel que l'on peut comprendre, maintenir, sécuriser, intégrer, mettre à jour et accompagner pendant de nombreuses années. Elle dépend aussi de personnes et d'organisations capables de prendre des décisions lorsque les priorités divergent ou que l'équipe d'origine passe à autre chose.

C'est là que beaucoup de discussions sur l'open source s'égarent. Elles comparent le prix des licences, les listes de fonctionnalités ou l'accès au code. Une question est bien plus utile : **qu'est-ce qui rend ce logiciel fiable au-delà du fournisseur, de l'équipe projet et du cycle budgétaire actuels ?**

Après vingt ans passés à construire des produits et des services autour des technologies Eclipse, ma réponse est que la pérennité d'un open source industriel repose sur six fondations liées entre elles :

- un produit utile et un projet techniquement sain ;
- une gouvernance explicite et transparente ;
- un effort continu de maintenance et de sécurité ;
- un modèle économique qui finance cet effort ;
- un écosystème auquel plusieurs acteurs peuvent participer ;
- de véritables options de sortie pour les utilisateurs.

Retirez l'une de ces fondations : l'ouverture restera peut-être juridiquement réelle, mais pourra devenir sans intérêt en pratique.

<figure>
    <a href="{{ site.url }}/images/blog/2026/open-source-industrial/open-innovation-industrial-ecosystem.webp">
      <img src="{{ site.url }}/images/blog/2026/open-source-industrial/open-innovation-industrial-ecosystem.webp" alt="Présentation à OCX 2024 de la boucle positive entre investissement industriel, maintenance amont, adoption, formation et services commerciaux">
    </a>
    <figcaption>À OCX 2024, j'ai représenté l'open source industriel comme une boucle positive : l'investissement entretient la technologie commune, une adoption plus large crée des opportunités et ces opportunités financent de nouveaux travaux.</figcaption>
</figure>

## Que signifie « open source industriel » ?

« Industriel » ne signifie pas que chaque projet doit ressembler à un énorme produit commercial. Cela signifie que des organisations peuvent prendre des engagements importants et durables autour de ce projet en comprenant clairement les risques.

Pour un composant logiciel ou un outil d'ingénierie, cela suppose généralement :

- des versions documentées et des engagements de compatibilité compréhensibles ;
- des builds reproductibles et des dépendances maîtrisées ;
- des mainteneurs disposant du temps et de l'autorité nécessaires pour examiner les contributions ;
- un processus de signalement et de correction des vulnérabilités ;
- une propriété intellectuelle et des licences traçables ;
- des chemins de migration pour les données, les API et les extensions ;
- un support ou une expertise que l'on peut contractualiser si nécessaire ;
- une gouvernance qui reste compréhensible lorsque les organisations ne sont pas d'accord ;
- la preuve que le savoir n'est pas concentré entre les mains d'une seule personne indisponible.

Ces propriétés ne sont pas produites par la licence. Elles sont le résultat d'un travail répété.

Un projet open source peut être innovant, populaire, et rester une mauvaise fondation pour un programme industriel de dix ans. À l'inverse, un projet modeste, porté par une communauté ciblée, une gouvernance prévisible et des utilisateurs engagés peut constituer un actif stratégique fiable.

## Distinguer le projet, le produit et le service

Les discussions deviennent plus claires lorsque l'on distingue trois niveaux.

Le **projet open source** est le bien commun technique : code source, tickets, versions, processus de contribution, décisions publiques et communauté. Sa gouvernance détermine qui peut l'influencer, et comment.

Un **produit** assemble des fonctionnalités pour un groupe d'utilisateurs précis. Il peut ajouter l'installation, l'administration, des intégrations, des configurations testées, un support à long terme, des certifications ou des fonctions qui n'appartiennent pas au projet commun.

Un **service** apporte de l'expertise et de la responsabilité : support, formation, architecture, migration, personnalisation, exploitation ou développement sponsorisé.

Ces trois niveaux peuvent être fournis par une seule organisation ou par plusieurs. Leurs frontières varient selon les écosystèmes. L'essentiel est que les utilisateurs les comprennent. Un dépôt public ne doit pas servir à laisser croire à un niveau de finition ou de support qui n'existe pas. Une offre commerciale ne doit pas masquer les améliorations reversées au projet ni les dépendances propres à un fournisseur.

Chez Obeo, le lien entre ces niveaux est central depuis le début. Comme je l'écrivais pour [les dix ans d'Obeo]({{ site.url }}/eclipse/obeo-dix-ans/), le succès de nos technologies open source et notre capacité à travailler au sein de leurs communautés sont devenus des facteurs clés du succès de nos produits commerciaux. La relation fonctionne lorsque l'activité commerciale renforce la fondation commune, et que cette fondation démultiplie ce que les produits et les services peuvent accomplir.

## La gouvernance est le système d'exploitation de la communauté

La gouvernance répond aux questions laissées ouvertes par la licence :

- Qui décide d'accepter ou non une contribution ?
- Comment acquiert-on une autorité technique ?
- Où les décisions de roadmap sont-elles discutées ?
- Que se passe-t-il lorsque deux employeurs poursuivent des objectifs différents ?
- Qui peut publier une version ou traiter une vulnérabilité ?
- Comment une nouvelle organisation peut-elle acquérir une véritable influence ?
- Que se passe-t-il si le principal contributeur se retire ?

Un modèle de gouvernance mature rend ces réponses publiques et prévisibles. Il ne supprime pas les désaccords. Il leur donne un cadre légitime pour être résolus.

Chez Eclipse, les projets fonctionnent selon des règles ouvertes, transparentes et méritocratiques. Le statut de committer se gagne par les contributions et l'élection par ses pairs ; il n'est pas automatiquement accordé par un employeur. Le [manuel des projets Eclipse](https://www.eclipse.org/projects/handbook/) définit également les rôles, les revues, la vérification de la propriété intellectuelle, les ressources publiques et le cycle de vie des projets.

Cela ne fait pas apparaître par magie une communauté diverse. Un projet peut rester très dépendant d'une seule entreprise, surtout à ses débuts. L'important est d'être honnête sur cette concentration et d'offrir aux autres un chemin crédible pour participer. **Une gouvernance neutre vis-à-vis des fournisseurs est une possibilité créée par les règles ; la diversité est un résultat produit par une participation durable.**

Une bonne gouvernance doit aussi être assez légère pour que le travail avance. Exiger une décision de comité pour chaque modification n'est pas un signe de maturité. Un périmètre clair, une autorité technique déléguée, des revues publiques et un mécanisme d'escalade sont généralement plus utiles qu'un contrôle de façade.

## Pourquoi placer un projet dans une fondation ?

Une fondation neutre rend la partie commune d'un écosystème plus crédible. Elle peut détenir les actifs et les marques du projet, définir des règles communes, encadrer les contributions et la propriété intellectuelle, fournir l'infrastructure, soutenir les pratiques de sécurité et arbitrer lorsque la gouvernance du projet échoue.

Cette continuité institutionnelle compte lorsque plusieurs organisations veulent coopérer sur une technologie qu'aucune ne devrait contrôler seule. La fondation crée un lieu où des concurrents peuvent contribuer selon les mêmes règles et où les utilisateurs peuvent distinguer le projet de la stratégie commerciale d'un fournisseur particulier.

Le [processus de développement Eclipse](https://www.eclipse.org/projects/dev_process/) va plus loin en imposant des pratiques destinées à préserver la viabilité d'un projet indépendamment d'une personne, d'une organisation ou d'un service externe donné. C'est directement pertinent pour la maîtrise du risque industriel.

Mais une fondation n'est pas une équipe produit que l'on aurait externalisée. Elle ne peut ni inventer la demande, ni financer tous les mainteneurs, ni définir à leur place une roadmap cohérente, ni remplacer le leadership technique. Elle fournit une infrastructure juridique, organisationnelle et collaborative. Les participants doivent toujours assurer le travail d'ingénierie et d'animation de la communauté.

La bonne question n'est donc pas simplement : « Ce projet est-il hébergé dans une fondation ? » Demandez plutôt :

- Quels actifs et quels processus y sont réellement gouvernés ?
- Les discussions techniques et les plans du projet sont-ils publics ?
- Les versions sont-elles produites à travers les processus de la fondation ?
- Les contributeurs d'un autre employeur peuvent-ils devenir committers ?
- Existe-t-il une supervision active lorsqu'un projet devient inactif ou dangereux ?
- Qui finance aujourd'hui le temps des mainteneurs ?

L'hébergement par une fondation est un signal fort lorsque ces mécanismes sont réels. Un logo ne suffit pas.

## La maintenance doit être financée

L'open source change qui peut examiner, utiliser, modifier et redistribuer un logiciel. Il ne rend pas l'ingénierie gratuite.

La maintenance consiste à examiner les tickets, reproduire les erreurs, mettre à jour les dépendances, améliorer la documentation, répondre aux contributeurs, produire les versions, migrer l'infrastructure, traiter les vulnérabilités et préserver la compatibilité. Une grande partie de ce travail devient invisible lorsqu'il est bien fait. Il est alors facile de valoriser les nouvelles fonctionnalités tout en traitant la maintenance comme un simple coût.

Un modèle économique durable conduit les bénéficiaires du logiciel à financer une part suffisante de ce travail commun. Plusieurs approches sont possibles :

- [abonnements de support et de maintenance](https://www.obeosoft.com/en/services/support-maintenance/) ;
- distributions d'entreprise ou produits complémentaires ;
- hébergement et exploitation managés ;
- conseil, intégration, migration et formation ;
- [développement sponsorisé de fonctionnalités prévues dans la roadmap](https://www.obeosoft.com/en/services/custom-development/) ;
- adhésion à un consortium ou à un groupe de travail ;
- investissement commun d'organisations partageant la même infrastructure ;
- financement public ou de recherche pour des résultats définis.

Aucun modèle n'est universellement supérieur aux autres. L'économie d'un projet utilisé comme bibliothèque n'est pas celle d'un environnement d'ingénierie collaborative. Un petit outil pour développeurs n'a pas les mêmes obligations qu'un logiciel intégré à des produits réglementés.

Le test décisif consiste à vérifier si l'activité qui génère des revenus et la santé du projet se renforcent mutuellement. Lorsque les travaux commerciaux créent systématiquement des forks privés, contournent les revues amont ou consomment le temps des mainteneurs sans le financer, le modèle accumule de la dette. Lorsque le travail rémunéré améliore les fondations communes, développe les compétences et fait émerger des utilisateurs et des fournisseurs plus capables, il peut produire une boucle positive.

Les utilisateurs qui ne contribuent pas financièrement ne sont pas forcément un échec. La facilité d'adoption est justement l'un des avantages de l'open source. Le modèle économique doit partir du principe que beaucoup d'utilisateurs ne paieront jamais, tandis que les organisations qui ont besoin de garanties, d'influence, d'intégration ou de responsabilité financeront un travail professionnel.

## La durabilité se voit dans le travail d'ingénierie ordinaire

La santé d'un projet se juge plus facilement sur des preuves que sur des déclarations. Regardez son activité pendant l'année écoulée :

- Les versions sortent-elles à un rythme adapté au domaine ?
- Les pull requests sont-elles examinées par plusieurs personnes ?
- Les décisions sur les tickets et la roadmap sont-elles expliquées publiquement ?
- Un nouveau contributeur peut-il construire le logiciel à partir d'une documentation accessible ?
- Les dépendances, les artefacts publiés et les licences sont-ils traçables ?
- Existe-t-il une politique sur les versions maintenues ?
- Les contacts et procédures de signalement des vulnérabilités sont-ils faciles à trouver ?
- Les migrations et les ruptures de compatibilité sont-elles documentées ?
- Le projet teste-t-il des intégrations et des mises à jour réalistes ?
- Les connaissances sont-elles réparties entre plusieurs personnes et organisations ?

Mon article de 2013, [On being open and transparent]({{ site.url }}/on-being-open-and-transparent/), formulait déjà la même idée du point de vue des contributeurs. Un dépôt visible ne suffit pas. Des builds reproductibles, un guide de contribution, des revues publiques, de l'intégration continue, de la documentation, de l'animation et des plans prévisibles déterminent si des personnes extérieures peuvent réellement participer. Plus de dix ans plus tard, cela reste vrai.

Une question inconfortable, mais nécessaire, demeure : qui maintiendra une contribution importante après son intégration ? Accepter du code sans chemin de maintenance crédible peut rendre un projet moins durable, pas davantage. Le volume de contributions ne mesure pas la capacité du projet.

## L'open source améliore la souveraineté, mais ne la garantit pas

L'open source est une composante puissante de la souveraineté technologique parce qu'il crée des droits que les licences propriétaires n'offrent pas : examiner, modifier, redistribuer et poursuivre indépendamment le développement du logiciel.

Mais la souveraineté est une capacité opérationnelle, pas une case cochée dans un contrat de licence. Une organisation n'est pas réellement autonome si elle possède le code source mais ne peut pas le construire, comprendre son architecture, migrer ses données, exploiter son infrastructure ou trouver des compétences en dehors du fournisseur en place.

Évaluez la maîtrise réelle selon plusieurs dimensions :

- **code :** le système pertinent peut-il être entièrement construit à partir des sources disponibles ?
- **données :** les formats et les mécanismes d'export sont-ils documentés et utilisables à grande échelle ?
- **exploitation :** le logiciel peut-il être déployé et supervisé dans l'environnement requis ?
- **compétences :** peut-on développer l'expertise en interne ou la trouver chez plusieurs prestataires ?
- **gouvernance :** l'organisation peut-elle contribuer, influencer les priorités ou maintenir un fork si nécessaire ?
- **dépendances :** des services hébergés, des extensions propriétaires ou des API externes recréent-ils un verrouillage ailleurs ?

L'open source ne supprime pas la dépendance à un fournisseur. Il en change la nature et donne davantage de levier aux utilisateurs. Un bon fournisseur reste précieux par son expertise, sa réactivité, la qualité de son produit et la confiance accumulée, et non parce qu'il serait techniquement ou juridiquement impossible de le quitter.

L'objectif ne doit pas être la « dépendance zéro ». L'ingénierie complexe dépend toujours de personnes et d'organisations. L'objectif est **une dépendance visible, influençable et assortie d'alternatives crédibles**.

## La sécurité et le Cyber Resilience Act relèvent le niveau d'exigence

La sécurité rend particulièrement nette la différence entre disponibilité du code et responsabilité dans la durée. Les utilisateurs industriels doivent savoir qui reçoit les signalements de vulnérabilités, quelles versions sont maintenues, comment les correctifs sont coordonnés et comment les informations sur les composants circulent jusqu'aux produits qui les intègrent.

Le règlement européen sur la cyberrésilience, ou Cyber Resilience Act (CRA), formalise une partie de cette responsabilité pour les produits comportant des éléments numériques. Il est entré en vigueur le 10 décembre 2024. Les obligations de notification s'appliquent à partir du 11 septembre 2026 et les principales dispositions à partir du 11 décembre 2027, selon le [calendrier de mise en œuvre de la Commission européenne](https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation).

Le règlement distingue volontairement les rôles. Un logiciel libre et open source développé ou fourni en dehors d'une activité commerciale est traité différemment d'un produit mis sur le marché par un fabricant. Le texte introduit également le rôle de **gestionnaire de logiciels libres et ouverts** (*open-source software steward*) pour les personnes morales qui soutiennent systématiquement et durablement des produits open source destinés à des activités commerciales, sans les mettre elles-mêmes sur le marché. La Commission fournit une [synthèse utile des dispositions du CRA concernant l'open source](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source).

Cela ne justifie ni de traiter tous les projets communautaires comme des fabricants, ni de supposer qu'une licence open source efface les responsabilités commerciales. Chaque organisation doit identifier son rôle réel dans la chaîne d'approvisionnement et obtenir le conseil juridique approprié.

Sur le plan opérationnel, la direction est déjà claire : la gestion des vulnérabilités, les versions maintenues, la connaissance des dépendances, la provenance, la documentation de sécurité et la coordination entre projets amont et produits aval ne peuvent plus être improvisées après un incident.

C'est aussi un domaine où la collaboration est plus efficace que l'interprétation isolée du règlement par chaque projet. Le [groupe de travail Eclipse Open Regulatory Compliance](https://projects.eclipse.org/working-group/eclipse-open-regulatory-compliance-working-group) réunit fondations, industriels, PME et acteurs de la recherche pour développer des pratiques et des ressources communes. J'ai directement rencontré ces travaux à [OCX 2024]({{ site.url }}/eclipse/ocx-open-community-experience-2024-fr/), où le CRA occupait une place centrale dans les discussions entre projets, fondations et industriels.

## Coopérer n'élimine pas la concurrence

L'open source industriel fonctionne lorsque des organisations s'accordent sur ce qui doit être commun tout en conservant la possibilité de se différencier au-dessus de ce socle.

Elles peuvent coopérer sur l'implémentation d'un langage, un framework de modélisation, l'interopérabilité, les processus de sécurité ou une infrastructure partagée. Elles peuvent toujours se distinguer par leur expertise métier, l'expérience utilisateur, les intégrations, le déploiement, les services, les engagements de support et la qualité d'exécution.

Cette frontière est stratégiquement utile. Réimplémenter en privé la même fondation impose un coût à chaque participant sans procurer, la plupart du temps, d'avantage significatif aux utilisateurs. Mutualiser ce travail permet de déplacer la concurrence vers les domaines auxquels les clients accordent réellement de la valeur.

Cela crée aussi un environnement propice à l'apprentissage. Les ingénieurs peuvent discuter d'architecture avec leurs pairs, les entreprises influencer les technologies dont elles dépendent, les chercheurs expérimenter sur une base pertinente pour la production, et les utilisateurs rapprocher leurs besoins des mainteneurs. Dans mon [entretien avec Federico Tomassetti]({{ site.url }}/interview/interview-strumenta/), j'expliquais comment des règles Eclipse claires permettent de collaborer sur une technologie commune tout en restant concurrents sur le plan commercial.

Cet équilibre demande de la discipline. La gouvernance partagée ne doit pas devenir un canal de coordination des marchés, et une roadmap commune ne constitue pas la promesse que les priorités de chaque participant seront financées. Les fondations disposent précisément de politiques antitrust et de structures de collaboration parce que la coopération industrielle exige des frontières explicites.

## Une grille de décision pour les utilisateurs

Avant de rendre stratégique un composant ou un outil open source, demandez des preuves dans six domaines.

### Adéquation produit et technique

- Résout-il le cas d'usage réel avec des performances et une ergonomie acceptables ?
- L'architecture, les points d'extension, les formats de données et les dépendances sont-ils documentés ?
- Existe-t-il un chemin crédible de mise à jour et de migration ?

### Santé du projet

- Qui sont les mainteneurs actifs et comment leur temps est-il financé ?
- À quel rythme les versions, les revues et les décisions communautaires sont-elles produites ?
- Une nouvelle organisation compétente pourrait-elle construire le projet et y contribuer ?

### Gouvernance

- Qui détient les actifs et les marques du projet ?
- Comment les committers sont-ils sélectionnés et les différends résolus ?
- Plusieurs organisations peuvent-elles acquérir une véritable autorité technique ?

### Sécurité et conformité

- Quelles versions reçoivent des correctifs de sécurité, et pendant combien de temps ?
- Existe-t-il un canal privé de signalement des vulnérabilités et une politique publique ?
- Quelles preuves de provenance, de dépendances et de publication sont disponibles ?
- Quel rôle lié au CRA ou aux réglementations sectorielles chaque organisation occupera-t-elle ?

### Économie et support

- Quels mécanismes commerciaux ou collectifs financent la maintenance ?
- Le support et l'expertise peuvent-ils être contractualisés au niveau de service requis ?
- Le travail rémunéré renforce-t-il le projet amont ou crée-t-il une divergence privée ?

### Réversibilité

- Pouvez-vous exporter vos données et exploiter le logiciel de manière indépendante ?
- Existe-t-il des fournisseurs alternatifs crédibles, ou pouvez-vous développer les compétences en interne ?
- Combien coûterait la maintenance d'un fork si la gouvernance ou la stratégie divergeait ?

Aucun projet n'obtiendra un score parfait. Cette grille rend les compromis visibles. Un jeune projet peut convenir à une expérimentation et être inadapté à un programme critique. Un projet concentré autour d'un acteur peut rester un choix solide lorsque le fournisseur principal est transparent, correctement financé et ouvre activement des chemins de participation à d'autres acteurs.

## L'actif durable, c'est l'écosystème

L'open source est parfois présenté comme un choix entre idéalisme communautaire et discipline commerciale. L'expérience industrielle indique une autre direction. Les écosystèmes les plus solides combinent des règles publiques, une ingénierie sérieuse, du travail rémunéré et de l'espace pour que plusieurs acteurs créent de la valeur.

Le code source compte parce qu'il établit des droits durables. La gouvernance transforme ces droits en influence. La maintenance les transforme en logiciel utilisable. Le financement donne de la continuité à cette maintenance. Une fondation offre un foyer institutionnel à la collaboration. Un écosystème diversifié donne des alternatives aux utilisateurs et davantage de chemins de survie à la technologie.

Voilà la véritable promesse de l'open source industriel : non pas un logiciel sans fournisseurs, sans coûts ni responsabilités, mais une infrastructure stratégique dont les dépendances peuvent être comprises, influencées et partagées.
