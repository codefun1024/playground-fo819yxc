from random import randint

# la combinaison est un nombre entre 0 et 9.
combinaison = randint(100, 999)

# Affichage de la combinaison
print("Bienvenue au CTF (Coffre-Trop-Fort). Confiez-moi tous vos biens!")

# Combinaison saisie par l'utilisateur
entrée = ""

# Faites répéter les actions suivantes :
entrée = input("Entrez la combinaison du coffre : ")
if entrée == combinaison:
    print("C'est la bonne combinaison!")
else:
    print("Mauvaise combinaison!")
