import builtins

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

    print("TECHIO> terminal -i 'bash -c \'cat>/tmp/entree\''")
    f = open("/tmp/entree")
    ligne = f.readline()[:-1]
    f.close()
    return ligne


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
