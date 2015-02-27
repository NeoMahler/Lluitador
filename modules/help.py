# -*- coding: utf-8 -*-

import json
import web
import time
import re
import urllib2
import socket

def ajuda(phenny, input):
    phenny.reply(u"Hola! Sóc un bot (robot) programat per ajudar els usuaris que ho necessiten. Escriu \".normes\" per un link a les normes bàsiques de Vikidia, o \".ordres\" per una llista de les meves ordres.")

ajuda.commands = ['ajuda']

def normes(phenny, input):
##    url = u'http://ca.vikidia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=Vikidia:Principis_b%C3%A0sics'
##    tmp = web.get(url)
##    extracte = json.loads(tmp)
##    ajuda = extracte['query']['pages']['*']
    phenny.reply(u"Llegeix les normes bàsiques a http://ca.vikidia.org/wiki/Vikidia:Principis_bàsics")

normes.commands = ['normes']
