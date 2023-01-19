# Projet Machine Learning

L'objectif de ce projet est de créer un modèle basé sur des techniques de machine learning pour prédire le prix d'un véhicule choisi par l'utilisateur à partir de ces caractéristiques. Le modèle étant entraîné sur une bases de données.

Le programme est divisé en deux grandes parties :

- Scraping
- Estimation
## Scraping

### Données 

Le site d'origine des données est le site [Spoticar](https://www.spoticar.fr). 

Elles concernent quatre marques sur lesquelles le site est spécialisé :

- Peugeot
- Citroën
- Opel
- Fiat

Pour chaque marque, nous pouvons récupérer 600 données (soit un total de 2400) de par la construction du site qui nous impose cette contrainte.

Chaque véhicule est ainsi codé sous la forme d'une classe `Voiture` comprennant les éléments suivants :

| Variable   |      Type      | Description    |
|:-|:-|:-|
| `marque` |Catégorielle| Marque du véhicule| 
| `modele` |Catégorielle| Nom du modèle de véhicule| 
| `carburant` |Catégorielle| Type de carburant ou d'alimentation | 
| `prix` |Numérique| Prix du véhicule sur le site|
| `kilometrage` |Numérique| Kilométrage du véhicule |
| `garantie_kilometrage` |Dichotomique| Indicateur de fiabilité concernant la valeur du kilométrage |
| `boite_de_vitesse` |Catégorielle| Type de boîte de vitesse |
| `transmission` |Numérique| Nombre de roues motrices | 
| `couleur` |Catégorielle| Couleur du véhicule | 
|  `garantie` |Dichotomique| Type de garantie proposé par le site vendeur | 
| `date_mise_circulation` |Numérique| Année de mise en  circulation du véhicule| 
| `puissance` |Numérique| Puissance du moteur(en cv) |
| `silhouette` |Catégorielle| Type de véhicule | 
| `nb_places` |Numérique| Nombre de places | 
| `utilisation_pred` |Catégorielle| Précédente utilisation/propriétaire du véhicule | 
| `puissance_fiscale` |Numérique| Puissance fiscale du véhicule (en cv) |
| `critait` |Numérique| Indice Crit'air du véhicule | 
| `ptac` |Numérique| PTAC du véhicule | 
| `nb_portes` |Numérique| Nombre de portes |

### Aperçu des données

graphique à intégrer

### Traitement des données

Avant tout calcul de modèle, les données doivent subir un traitement permettant leur compatibilité avec le module `scikit-learn`. 

La première étape est la gestion des données manquantes pour lesquelles s'offrent plusieurs solutions :

- Suppression des observations
    - Le suppression d'observation réduit la taille de la base de données, chose que nous ne pouvons nous permettre de par le faible nombre d'observations. Cela les réduirait d'environ 1/3 et pourrait rendre le modèle faux.
- Suppression de variables
    - Presque toutes les variables sont concernées par ce problème, cette solution n'est donc pas viable.
- Imputation
    - C'est la solution que nous avons choisie telle que :
        - Les variables numériques sont imputées par la moyenne.
        - les variables catégorielles et dichotomiques sont imputées par la valeur la plus présente.

