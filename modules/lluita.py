# -*- coding:utf-8 -*-

import random

jugadors = []
desafiador = None
segon = None
torn = None
perdedor = None
guanyador = None
vida1 = 100
vida2 = 100

def desafiar(phenny, input):
    global desafiador
    if not jugadors == []:
        if input.nick in jugadors:
            phenny.reply(u"Ja estàs a la llista de jugadors!")
            return
        else:
            phenny.reply(u"Pots acceptar el desafiament, però no desafiar a un altre jugador. El jugador que ha llançat el desafiament és " + "".join(desafiador))
    else:
        jugadors.append(input.nick)
        desafiador = input.nick
        phenny.reply(u"Has llançat el desafiamemnt")
        #phenny.say(str(jugadors))

desafiar.commands = ['desafiar', 'inici']

def acceptar(phenny, input):
    global segon
    if len(jugadors) > 0:
        jugadors.append(input.nick)
        segon = input.nick
        phenny.say(u"Has acceptat el desafiament")
        instruccions(phenny, input)
        return
    else:
        phenny.reply(u"Ningú ha llançat cap desafiament. Fes-ho escrivint '.desafiar'.")
        return

acceptar.commands = ['accepta', 'acceptar', 'lluitar']

def instruccions(phenny, input):
    global torn
    phenny.say(u"Els jugadors " + " i ".join(jugadors) + u" han començat a lluitar.")
    phenny.say(u"Instruccions:")
    phenny.say(u" ")
    phenny.say(u".pega - pega a l'altre jugador")
    phenny.say(u" ")
    phenny.say(u"No es permet sortir del canal per evitar perdre.")
##    phenny.say(u"Si perds seras kickejat... però ja no hi ha marxa enrere! :)")
    phenny.say(u" ")
    phenny.say(u"Que començi el combat!")
    phenny.say(u" ")
    torn = desafiador
    phenny.say(u"Torn de " + torn)
def pega(phenny, input):
    global vida1
    global vida2
    global perdedor
    global guanyador
    global torn
    if not input.nick == torn:
        phenny.reply(u"No és el teu torn!")
        return
    elif input.nick == torn:
        rang = random.choice(range(10, 30))
        mal = random.choice([rang, 50])
        if mal == 50:
            mal2 = random.choice([1,2])
            if mal2 == 1:
                mal = 50
            else:
                mal = 20
    if jugadors.index(input.nick) == 0:
        novavida = vida2 - mal
        vida2 = novavida
        if vida2 <= 0:
            perdedor = segon
            guanyador = desafiador
            final(phenny, input)
            return
        phenny.say(input.nick + " ha tret " + str(mal) + " punts de vida a \x02" + str(segon) + " (" + str(vida2) + " punts)\x02")
    elif jugadors.index(input.nick) == 1:
        novavida = vida1 - mal
        vida1 = novavida
        if vida1 <= 0:
            perdedor = desafiador
            guanyador = segon
            final(phenny, input)
            return
        phenny.say(input.nick + " ha tret " + str(mal) + " punts de vida a \x02" + str(desafiador) + " (" + str(vida1) + " punts)\x02")
    if torn == desafiador:
        torn = segon
    elif torn == segon:
        torn = desafiador
    phenny.say(u"Torn de " + torn)
        
pega.commands = ['pega']

def final(phenny, input):
    global perdedor
    global guanyador
    global torn
    global desafiador
    global segon
    global jugadors
    phenny.say(guanyador + u" ha \x02guanyat\x02 a " + perdedor + ". Moltes felicitats!!")
    del jugadors[:]
    torn = None
    desafiador = None
    segon = None
    guanyador = None
    perdedor = None
    return
