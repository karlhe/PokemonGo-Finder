#!/usr/bin/python
# -*- coding: utf-8 -*-

from notifier import Notifier

def debug(message):
    print(message)

origin = (38.898, -77.037)
pokemon = { "lat": 38.8977, "lng": -77.0365, "name": u'Nidoran♀', "id": 29, "disappear_time": 1469053206 }

notifier = Notifier(origin, debug)
notifier.pokemon_found(pokemon)
