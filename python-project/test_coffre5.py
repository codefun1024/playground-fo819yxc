import random
import builtins
import time
import os

anc_input = builtins.input
échec = True


entrées = [random.randrange(0, 999) for i in range(10)]


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def nouv_input(*params):
    global échec

    if len(params) > 1:
        échec = True

    elif len(params) > 0:
        print(params[0], end="")
        if params[0].strip() == "Entrez la combinaison du coffre :":
            échec = False
        else:
            échec = True

    entrée = str(entrées.pop())
    print(entrée)

    return entrée


builtins.input = nouv_input

try:
    import coffre5

    if échec:
        fail()
        send_msg(
            "Attention!", "Entrez la question exacte : «Entrez la combinaison du coffre : » ")

    else:
        int(coffre5.entrée)
        success()
        send_msg(
            "Bravo!", "L'entrée de l'utilisateur (" + coffre5.entrée + ") est maintenant stockée sous le nom «entrée».")

except Exception as e:
    fail()
    échec = True
    send_msg("Pas tout à fait",
             'Quelque chose ne va pas. Avez-vous bien placé votre question entre les guillemets anglais?')
    send_msg("Erreur", e)
