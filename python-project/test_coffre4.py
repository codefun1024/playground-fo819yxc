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


def nouv_input(*params):
    global échec
    échec = False
    if len(params) > 0:
        send_msg("Très bien!"
                 "Remarquez que le texte mis entre les parenthèses sert de question posée à l'utilisateur.")

    # \'read in && echo $in > /tmp/entree \''")
    print("TECHIO> terminal -i 'python3 /project/target/coffre4.py'")


builtins.input = nouv_input
try:
    import coffre4
except Exception as e:
    échec = True
    print(e)

if échec:
    fail()
    send_msg("Il manque quelque chose!",
             "Placez «entrée = input()» après le message de bienvenue.")
