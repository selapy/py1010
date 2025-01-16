# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:04:49 2025

@author: SEFO
"""

# Arbeidskrav 2-oppgave 1
# Dette programmet regner ut hvor gammel personnen blir i løpet av 2024 gitt fødselsår

# skriv inn fødselsår


alder = int(input('Hvilket år er du født? ') )
print("du var født i år", alder)
# Regn ut alder i år 2024

benchmark_aar = 2024

# validering og beregning

if alder > benchmark_aar:
   print("ugyldig alder")

else:

  alder_i_benchmark_aar = benchmark_aar - alder
  print("I løpet av 2024 blir du", alder_i_benchmark_aar)
