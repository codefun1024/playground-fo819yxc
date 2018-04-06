from random import randint

# la combinaison est un nombre entre 0 et 9.
combinaison = randint(100, 999)

# Affichage de la combinaison
print("Bienvenue au CTF (Coffre-Trop-Fort). Confiez-moi tous vos biens!")

entrée = input("Entrez la combinaison du coffre : ")

if entrée == combinaison:
    print("C'est la bonne combinaison!")
