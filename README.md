# SmartTweet

## Informations générales 
Le but de ce projet est d'analyser le contenu de tweets et de les classer selon le sentiment qu'ils renvoient. Ensuite, ces résultats seront affichés dans une page web.

## Prérequis
- Installer Python3 ainsi que les librairies présentes dans le fichier requirements.txt

- Une instance de ElephantSQL

## Installation
- Copiez le contenu du repository sur votre ordinateur

- Pour créer la base de données, rendez vous dans le browser d'Elephant SQL et entrez les commandes présentes  dans le fichier [creationBDD.sql](https://github.com/Groupe01/SmartTweet/blob/master/database_install/creationBDD.sql)

- Pour charger vos différents produits dans la base de données, éxécutez le fichier main.py autant de fois qu'il y a de produits à tester. La base de données fournie est préchargée avec les produits PS5, XBOXSERIESX, Iphone11 et GalaxyZFold2.

- Pour finir, lancez le fichier app.py pour démarrer le serveur.

## Utilisation
Il vous suffit de vous rendre sur la page http://localhost:8080 ou sur la page index.html présente dans le dossier templates.
Pour voir le résultat des différentes analyses, il suffit de cliquer sur le bouton contenant le nom du produit choisi une première fois afin de demander les résultats. Ensuite, appuyez sur ce bouton une deuxième fois afin d'afficher les graphiques.

## Développé par
- Mohamed
- Orkaëlle 
- Farida
- David
