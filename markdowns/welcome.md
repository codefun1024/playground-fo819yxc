# Bienvenue!

La compagnie de coffres-forts «Sécur-IT» vous a engagé pour programmer l'interface utilisateur de leur tout dernier modèle, le «Coffre-Trop-Fort».

Ce coffre-fort très spécial est capable de choisir sa propre combinaison secrète au hasard. Cliquez sur «Run» pour démarrer le programme et voir la combinaison choisie.

```python runnable
from random import randint

# la combinaison est un nombre choisi aléatoirement entre 0 et 9.
combinaison = randint(0, 9)

# Affichage de la combinaison
print("La combinaison est : ", combinaison)
```
