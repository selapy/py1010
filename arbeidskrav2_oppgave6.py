# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:08:49 2025

@author: SEFO
"""

"""
Skriv en kode som plotter funksjonen 𝑓(𝑥)=−𝑥2−5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet [-10,10].

"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -x**2 - 5

x = np.linspace(-10, 10, 200)

y = f(x)

plt.plot (x,y)
plt.show()