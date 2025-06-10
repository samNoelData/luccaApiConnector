### Cas pratique Reflect - Lucca API - Sam NOEL
## Structure du projet

- ### http/
  Client HTTP générique permettant de faire les appels API avec gestion centralisée des erreurs.

- ### lucca/
  Client spécifique pour l’API Lucca. C’est ici que sont implémentées les fonctions pour récupérer les données des différents endpoints.

- ### schemas/
  Définition des schémas attendus pour chaque endpoint.
  Ces fichiers permettent de figer les schémas dans l'objectif de faciliter l'intégration des données dans BigQuery

- ### helpers/
  Fonctions utilitaires nécessaires au projet

- ### main.py
  Point d’entrée du projet. C’est ici que les extractions sont orchestrées.

- ### config.yaml
  Fichier de configuration principal. Il contient la liste des endpoints à extract, les champs à extraire et autre paramètres.

## Mise en place

### Clonage du dépôt

```bash
git clone https://github.com/samNoelData/luccaApiConnector.git
cd luccaApiConnector
```

### Requirements
```bash
pip install -r requirements.txt
```

### Création du .env
```
API_KEY="X"
API_HOST="X"
STORAGE_FOLDER="./storage/"
CONFIG_FILE="config.yaml"
```