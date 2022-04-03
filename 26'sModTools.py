import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction


extension_info = {
    "title": "26'sModTools",
    "description": ":mt pla&rmute&mute",
    "version": "2.0",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

KATMER = "Chat"

MESSAGE = ":mt mute "


sc = True

sec_kod = False

def konusma(msj):
    global sc, sec_kod, sec_player, kod2, player_id, mobi_id, kod, mod, ac, font, f0nt


    text = msj.packet.read_string()

    if text == ':mt pla':
        msj.is_blocked = True
        sc = True
        sec_kod = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Click on the person you want to moderate, enter the "ambassador" section and press "unmute" from there"}{i:0}{i:30}{i:0}{i:0}')

    if text == ':mt rmute':
        msj.is_blocked = True
        sc = False
        ext.send_to_server('{out:MuteUser}{i:'+str(kod)+'}{i:7205995}{i:999999})')
        ext.send_to_client('{in:Chat}{i:123456789}{s:"'+str(kod)+' you have unmuted this person "}{i:0}{i:30}{i:0}{i:0}')

    if text.startswith(MESSAGE):
        msj.is_blocked = True
        if sc:
            mod = int(text[(len(MESSAGE)):])
            ext.send_to_server('{out:MuteUser}{i:' + str(kod) + '}{i:7205995}{i:'+str(mod)+'})')
            ext.send_to_client('{in:Chat}{i:123456789}{s:"' + str(mod) + ' you threw that much"}{i:0}{i:30}{i:0}{i:0}')


def yukle_kod(p):
    global kod, sec_kod

    if sec_kod:
        sec_kod = False
        user_id, _, _ = p.packet.read("iii")
        kod = str(user_id)
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Player: Saved v/ "}{i:0}{i:30}{i:0}{i:0}')

ext.intercept(Direction.TO_SERVER, yukle_kod, 'UnmuteUser')
ext.intercept(Direction.TO_SERVER, konusma, 'Chat')


