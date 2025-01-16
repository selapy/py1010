# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:34:03 2025

@author: SEFO
"""

"""
Lag et program med en funksjon som regner om fra grader til radianer. Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....
"""

import numpy as np

# angi grader

v_grad = float(input('Skriv inn gradtallet:' ))

# Radiantallet til vinkelen regnes  som

v_rad = v_grad*np.pi/180

print("det er", v_rad,"radianer")