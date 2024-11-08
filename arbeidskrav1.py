# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:28:58 2024

@author: Selapy
"""
# Dette er min første Python-program 
# Abridskraft 1

# Dette programmet vil sammenligne ålige kostandene mellom elbil og besibil 
# Det gir meg forslag hvilken type bil jeg bør kjøpe


# antall kilometer jeg kjører per år
antall_km_per_ar = 10000    

# forskringavgit for elbil og bensinbil
forskring_elbil = 50000 # NOK per år
forskring_besnsibbil= 7500 # NOK per år

# trafikkforsikringsavgift  for elbil og bensinbil
trafikkforsikringsavgift_elbil = 8.38 # NOK per dag
trafikkforsikringsavgift_bessinbil = 8.38 # NOK per dag

# strøm og bensinavgift for elbil og bensinbil
stømpris_elbil = 2.00 # NOK per km
bensinpris_bensinbil = 1.0 # NOK per km

# bomavgift for elbil og bensinbil
bommavgift_elbil = 0.1 # NOK per km
bommavgift_bensinbil = 0.3 # NOK per km


# Beregning av årlig bensinpris og bomavgift for bensinbil

bensinpris_bensinbil_ar = bensinpris_bensinbil * antall_km_per_ar
bomavgift_bensinbil_ar = bommavgift_bensinbil * antall_km_per_ar

print(bensinpris_bensinbil_ar)
print(bomavgift_bensinbil_ar)

# Beregning av årlig stømpris og bomavgift for elbil

stømpris_elbil_ar = stømpris_elbil * antall_km_per_ar
bommavgift_elbil_ar = bommavgift_elbil * antall_km_per_ar

print(stømpris_elbil_ar)
print(bommavgift_elbil_ar)

# Beregning av årlig  trafikkforsikringsavgift  for elbil og bensinbil

trafikkforsikringsavgift_elbil_ar = trafikkforsikringsavgift_elbil * 365
trafikkforsikringsavgift_bessinbil_ar = trafikkforsikringsavgift_bessinbil *365

print(trafikkforsikringsavgift_elbil_ar)
print(trafikkforsikringsavgift_bessinbil_ar)

# årlig kostander for elbil

kostnader_elbil_ar = forskring_elbil + trafikkforsikringsavgift_elbil_ar + stømpris_elbil_ar +bommavgift_elbil_ar

print(kostnader_elbil_ar)

# årlig kostnader for bensinbil

kostnader_bensinbil_ar = forskring_besnsibbil + trafikkforsikringsavgift_bessinbil_ar + bensinpris_bensinbil_ar + bommavgift_elbil_ar

print(kostnader_bensinbil_ar)

print("TotalKostnadene til elbil er " + str(kostnader_elbil_ar) + "sammelignet med totalKostnadene til bensinbil som er " + str(kostnader_bensinbil_ar))
