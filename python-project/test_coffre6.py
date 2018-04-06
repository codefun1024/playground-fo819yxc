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

    return str(entrées[-1])


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
    if len(params) == 1 and params[0] == "C'est la bonne combinaison!":
        send_msg(
            "Bravo!", "Le coffre s'ouvre lorsqu'on entre la bonne combinaison")
        échec = False

    anc_print(*params)


builtins.input = nouv_input
builtins.print = nouv_print
random.randint = nouv_random


try:
    import coffre6

    if échec:
        fail()

    else:
        success()

except Exception as e:
    fail()
    échec = True
    send_msg("Pas tout à fait",
             'Quelque chose ne va pas. Avez-vous bien placé la condition «entrée == combinaison» après le mot «if» ? ')
    send_msg("Erreur", e)
