# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:07:01 2025

@author: SEFO
"""

import numpy as np

def beregne_areal_omkrets_figur(a, b):
    
    # Beregn hypotenusen og radius for halvsirkelen
    
    c = np.sqrt(a**2 + b**2)
    r = c / 2

    # Beregn areal og omkrets til halvsirkel
    
    areal_halvsirkel = (np.pi * r**2) / 2
    omkrets_halvsirkel = np.pi * r

    # Beregn areal og omkrets til trekant
    areal_trekant = (a * b) / 2
    omkrets_trekant = a + b + c

    # Beregn areal og omkrets til figur
    areal_figur = areal_halvsirkel + areal_trekant
    omkrets_figur = omkrets_halvsirkel + omkrets_trekant
    
    return areal_figur, omkrets_figur

#Angi legedene til trekanten

a = int(input("Skriv inn kantlengden til a: "))
b = int(input("Skriv inn kantlengden til b: "))

areal, omkrets = beregne_areal_omkrets_figur(a, b)

print("Arealet til figuren er:", areal)
print("Den ytre omkretsen til figuren er:", omkrets)
