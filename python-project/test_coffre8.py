import importlib
import random
import builtins
import time
import os

anc_input = builtins.input
anc_randint = random.randint
anc_print = builtins.print

échec = True

entrées = [anc_randint(0, 1000) for i in range(100)]


def nouv_random(a, b):
    global entrées

    aléas = str([x for x in entrées if a <= x <= b][0])
    random.shuffle(entrées)

    return aléas


def send_msg(channel, msg):
    anc_print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    anc_print("TECHIO> success true")


def fail():
    anc_print("TECHIO> success false")


def nouv_input(*params):
    global échec

    if len(params) == 0:
        échec = True

    elif len(params) > 1:
        échec = True

    elif len(params) > 0:
        anc_print(params[0], end="")

    entrée = str(entrées.pop())
    anc_print(entrée)

    return entrée


def nouv_print(*params):
    global échec
    global nb_msg

    if len(params) == 1 and params[0] == "C'est la bonne combinaison!":
        échec = False
    if len(params) == 1 and params[0] == "Mauvaise combinaison!":
        échec = True

    anc_print(*params)


builtins.input = nouv_input
builtins.print = nouv_print
random.randint = nouv_random


try:
    import coffre8

    if échec:
        fail()
        send_msg("Pas encore.",
                 "Pour répéter la saisie et la vérification, placez «while entrée != combinaison: » en haut de la vérification et décalez-la vers la droite. N'oubliez surtout pas de recommencer la saisie lorsque l'utilisateur s'est trompé!")

    else:
        success()

except Exception as e:
    fail()
    échec = True
    send_msg("Pas tout à fait",
             'Quelque chose ne va pas. Avez-vous bien aligné «if» et «else» 4 espaces à droite par rapport au while? N\'oubliez pas les deux-points après while et la condition.')
    send_msg("Erreur", e)
