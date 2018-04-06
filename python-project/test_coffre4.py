import builtins
import time
import os

anc_input = builtins.input
échec = True


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def nouv_input(*params)
    if len(params) > 1:
        fail()
        send_msg("Quelque chose cloche", "Avez-vous bien utilisé «input»?")

    print(params)

    échec = False
    return entrées.pop()


builtins.input = nouv_input

try:
    import coffre4

    if not échec:
        success()
        send_msg(
            "Bravo!", "L'entrée de l'utilisateur est maintenant stockée sous le nom «entrée».")

except Exception as e:
    fail()
    échec = True
    send_msg("Pas tout à fait",
             'Quelque chose ne va pas. Utilisez «entrées = input()» après le message de bienvenue.')
