#!/usr/bin/env python3
# coding: utf8

import pyxhook
import time
import autopy

k = list()
correspondance = {"cdt":"Cordialement","bye":"aurevoir","slt":"Salut","res":"Veuillez agréer mes profonds respects"}

def kbevent(event):
  global running
  k.append(event.Key)

  # On transforme
  if event.Ascii == 192: #if F3 pressed
    chaine = ""
    v = k[-4:]
    les_trois_derniers = v[:3]
    for e in les_trois_derniers:
        chaine += e

    if chaine in correspondance:
        autopy.key.type_string(correspondance[chaine])

# Create hookmanager
hookman = pyxhook.HookManager()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()

# Create a loop to keep the application running
running = True
while running:
  time.sleep(0.1)

# Close the listener when we are done
hookman.cancel()
