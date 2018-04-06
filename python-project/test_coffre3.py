import builtins

anc_print = builtins.print
échec = True


def send_msg(channel, msg):
    anc_print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    anc_print("TECHIO> success true")


def fail():
    anc_print("TECHIO> success false")


def nouv_print(*params):
    global échec
    if len(params) == 1 and params[0] == "Bienvenue au CTF (Coffre-Trop-Fort). Confiez-moi tous vos biens!":
        success()
        send_msg(
            "Bravo!", "Vous maîtrisez maintenant l'affichage de texte")
        échec = False
    else:
        échec = True

        anc_print(*params)


builtins.print = nouv_print
try:
    import coffre3

    if échec:
        fail()
        send_msg("Pas tout à fait", 'Quelque chose ne va pas. Utilisez «print(&quot;message à afficher&quot;)» à la ligne 6 en vous assurant de bien copier le message entre les guillemets anglais.')

except Exception as e:
    fail()
    échec = True
    send_msg("Quelque chose cloche",
             'Avez-vous mis les guillemets anglais &quot;...&quot; à chaques bouts de la phrase à afficher?')
