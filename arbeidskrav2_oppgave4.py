# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

data = {
        
        "Norge":["Oslo", 0.634],
        "England":["London", 8.982],
        "Frankrike":["Paris", 2.161],
        "Italia":["Roma", 2.873]
        
        }

# gi informasjon til brukeren fra Dictionaryen

Valgt_land = input("velg et land fra listen ovenfor: ")

if Valgt_land == "Norge":
    print("Oslo er hovedstaden i Norge og det er 0.634 mill. innbyggere i Oslo")

elif Valgt_land == "England":
    print("London er hovedstaden i England og det er 8.982 mill. innbyggere i London")

elif Valgt_land == "Frankrike":
    print("Paris er hovedstaden i Frankrike og det er 8.982 mill. innbyggere i Paris")

elif Valgt_land =="Italia":
    print("Roma er hovedstaden i Italia og det er 2,873 mill. innbyggere i Roma")

else:
    print("finns ikke i Dictionaryen")
    
# oppdater dictionaryen med et nytt land

nytt_land = input("hvis du legger til et land skriv inn  her slik vi oppdaterer dictionaryen: ")
nytt_hovestad = input("oppgi hovedstad: ")
nytt_antall_innbygger = int(input("oppgi antall innbyggere: "))

data[nytt_land] = [nytt_hovestad, nytt_antall_innbygger]

print(data.items())