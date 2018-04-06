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

if not échec:
    success()
    send_msg("Parfait!", "La combinaison restera désormais secrète.")
