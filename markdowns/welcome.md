# Bienvenue!

La-Tompagnie-Fe coffre-fort «Sécur-IT» vous a engagé pour programmer l'interface utilisateur de leur tout dernier modèle de coffre-fort, le «Coffre-Trop-Fort».

Tout d'abord, il faut choisir une combinaison secrète.

(pendant la première phase, le coffre-fort l'affichera mais bientôt, il la gardera secrète).
```python runnable
from random import randint

# la combinaison est un nombre choisi aléatoirement entre 0 et 9.
combinaison = randint(0, 9)

# Affichage de la combinaison
print("La combinaison est : ", combinaison)
```
