# Tester le site localement

## Préparer l’environnement

Le projet utilise Ruby et Bundler. Installer les dépendances dans le projet :

```bash
bundle config set --local path .bundle/gems
bundle install
```

Ne pas lancer `bundle install` avec `sudo`.

## Prévisualiser le site

Depuis la racine du dépôt :

```bash
bundle exec jekyll serve --drafts --config _config.yml,_config_local.yml
```

Ouvrir ensuite <http://127.0.0.1:4000/>.

Le fichier `_config_local.yml` remplace `site.url` pendant la prévisualisation.
Les feuilles de style, images et autres ressources sont ainsi chargées depuis
le serveur local plutôt que depuis le site publié.

L’option `--drafts` permet notamment de prévisualiser les articles encore en
brouillon.

## Vérifier uniquement le build

```bash
bundle exec jekyll build --drafts --trace
```

Le site généré se trouve dans `_site/`.

## Note Ruby 3.4

Avec Ruby 3.4, le `Gemfile` inclut explicitement les gems `csv`, `bigdecimal`
et `webrick`, nécessaires à cette ancienne version de Jekyll et de
`github-pages`.
