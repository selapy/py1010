# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:54:23 2025

@author: SEFO
"""

# Arbeidskrav 2-oppgave 2
"""
Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive svaret til skjerm. 
Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe 5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. 
Hvordan kan sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?
"""
# angi antall elever son kommer til klassefesten

antall_elever = int(input('Skriv inn antall elever:' ))

# antall pizza en elev kan spise

Pizza_per_elev = 0.25

# regn ut hvor mange pizza det bør handles

antall_Pizza_handles = antall_elever * Pizza_per_elev

# skriv ut som heltall

antall_Pizza_handles = int(antall_Pizza_handles)
print("det må behandles inn", antall_Pizza_handles, "pizzaer")