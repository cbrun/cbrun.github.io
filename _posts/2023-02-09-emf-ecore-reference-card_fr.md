--- 
layout: post 
title: Connaissez-vous Ecore ? Vous cherchez une carte de référence ? 
categories: [modeling] 
tags:
  - modeling
  - emf
  - eclipse
  - sirius
  - opensource
  - ecore
lang: fr
permalink: /modeling/ecore-diagram-reference/
translation_en: /modeling/emf-ecore-reference-card/
excerpt: "Une carte de référence Ecore en une page—pratique pour les utilisateurs EMF et enseignants—pour rappeler pourquoi ces concepts clés comptent et comment les appliquer."
---


“𝐸𝑣𝑒𝑟𝑦𝑡ℎ𝑖𝑛𝑔 𝑠ℎ𝑜𝑢𝑙𝑑 𝑏𝑒 𝑚𝑎𝑑𝑒 𝑎𝑠 𝑠𝑖𝑚𝑝𝑙𝑒 𝑎𝑠 𝑝𝑜𝑠𝑠𝑖𝑏𝑙𝑒, 𝑏𝑢𝑡 𝑛𝑜𝑡 𝑠𝑖𝑚𝑝𝑙𝑒𝑟” était probablement l'un des mantras auxquels l'équipe du [Eclipse Modeling Framework](https://www.eclipse.dev/modeling/emf/) (Ed Merks, Marcelo Paternostro, Dave Steinberg, entre autres...) devait s'en tenir lorsqu'ils ont créé les concepts fondamentaux qui permettraient la définition de tous les autres outils. Ecore est un noyau, vous définissez votre modèle spécifique au domaine en utilisant ces constructions. Cela se résume à des classes, des types, des attributs et des relations, mais il y a beaucoup de beauté dans la façon dont cela a été conçu, et on peut dire sans risque que cela a passé l'épreuve du temps. En 2016, j'ai essayé de tout condenser dans une seule carte de référence. Je ne l'ai pas terminée au point de la publier, mais je le fais aujourd'hui (mieux vaut tard que jamais !)

<figure> 
<a href="{{ site.url }}/images/blog/2023/Ecore_reference_card.pdf"><img src="{{ site.url }}/images/blog/2023/Ecore_reference_card.png"></a> 
<figcaption>Carte de Référence Ecore</figcaption> 
</figure>

Pour la produire, j'ai exclusivement utilisé des outils Open-Source : 
- [Ecore Tools](https://www.eclipse.dev/ecoretools/) : éditeur de diagrammes Ecore construit sur Eclipse Sirius, 
- [Inkscape](https://inkscape.org/) : un de mes outils OSS préférés pour produire des graphiques vectoriels.

J'ai créé 4 diagrammes distincts à partir du modèle Ecore.ecore, puis utilisé la fonctionnalité "Exporter comme image" de Sirius pour obtenir des fichiers SVG. J'ai glissé-déposé ces fichiers dans Inkscape, mis à l'échelle, composé un peu, et voilà ! Voici la carte de référence. Vous pouvez maintenant décorer votre bureau ;) J'espère que vous apprécierez.
```
