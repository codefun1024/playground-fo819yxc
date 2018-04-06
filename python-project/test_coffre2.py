import builtins
import inspect

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
    if len(params) == 0:
        fail()
        échec = True
        send_msg(
            "«print()» une ligne vide. On peut s'en débarasser complètement.", "Réessayez.")
    else:
        fail()
        échec = True
        send_msg(
            "Vous voyez la ligne qui contient le mot «print»? Faites-la disparaître!", "Réessayez.")
    anc_print(*params)


builtins.print = nouv_print
import coffre2

if not échec and "# Affichage de la combinaison" in inspect.getsource(coffre2):
    fail()
    échec = True
    send_msg("Encore un peu de ménage!", "C'est bien mais il reste un détail. Les lignes qui commencent par # sont des «commentaires», ils servent à indiquer ce que fait le programme à un point particulier. Si vous enlevez la ligne d'affichage, il faudrait aussi enlever le commentaire qui allait avec")

if not échec:
    success()
    send_msg("Parfait!", "La combinaison restera désormais secrète.")
