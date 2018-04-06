import builtins

anc_print = builtins.print
échec = False


def send_msg(channel, msg):
    anc_print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    anc_print("TECHIO> success true")


def fail():
    anc_print("TECHIO> success false")


def nouv_print(*params):
    global échec
    if len(params) == 1 and params[0] == "Bienvenue au CTF (Coffre-Trop-Fort). Confiez-moi tous vos biens!":
        succes()
        send_msg(
            "Bravo!", "Vous maîtrisez maintenant l'affichage de texte")
    else:
        fail()
        échec = True
        send_msg(
            "Ce n'est pas exactement ça"."Avez-vous recopié la phrase exactement? Sélectionnez le texte de la phrase grâce à la souris puis utiliser le bouton de droite pour copier le texte et enfin le coller à l'endroit désiré.")
    anc_print(params)


builtins.print = nouv_print
try:
    import coffre2

    if not échec:
        success()
        send_msg("Parfait!", "La combinaison restera désormais secrète.")
except:
    fail()
    échec = True
    send_msg("Quelque chose cloche". "Avez-vous mis les guillemets anglais \"...\" à chaques bouts de la phrase à afficher?")
