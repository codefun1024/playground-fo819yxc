import random
import builtins
import time
import os

anc_input = builtins.input
anc_randint = random.randint
anc_print = builtins.print

échec = True

entrées = []


def nouv_random(a, b):
    global entrées
    entrées = [anc_randint(a, b) for i in range(100)]

    return str(entrées[-2])


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


nb_msg = 0


def nouv_print(*params):
    global échec
    global nb_msg

    if len(params) == 1 and params[0] == "C'est la bonne combinaison!":
        send_msg(
            "Bravo!", "Le coffre s'ouvre lorsqu'on entre la bonne combinaison")
        nb_msg += 1
    if len(params) == 1 and params[0] == "Mauvaise combinaison!":
        send_msg(
            "Bravo!", "Le coffre détecte les mauvaises combinaisons")
        nb_msg += 1

    if nb_msg == 2:
        échec = False

    anc_print(*params)


builtins.input = nouv_input
builtins.print = nouv_print
random.randint = nouv_random


try:
    import coffre7
    del coffre7
    import coffre7

    if échec:
        fail()
        send_msg("Pas tout à fait",
                 "Avez-vous bien placé «else» puis un affichage du message «Mauvaise combinaison!»?")

    else:
        success()

except Exception as e:
    fail()
    échec = True
    send_msg("Pas tout à fait",
             'Quelque chose ne va pas. Avez-vous bien aligné «else:» avec «if» et placé un print en-dessous? N\'oubliez pas les deux-points après else.')
    send_msg("Erreur", e)
