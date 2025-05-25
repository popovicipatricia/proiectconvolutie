import numpy as np
import matplotlib.pyplot
"""
Proiect - Convoluția semnalelor sinusoidale
Tema: D4-T2 | Convoluția semnalelor
Echipa: 31-E7
Studenți: MĂCIUCĂ M. ANDREEA-CORINA, POPOVICI P. PATRICIA

Surse folosite:
- https://numpy.org/doc/stable/reference/generated/numpy.sin.html
- https://numpy.org/doc/stable/reference/generated/numpy.convolve.html
- https://docs.scipy.org/doc/scipy/reference/signal.html
- https://matplotlib.org/
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Generează un semnal sinusoidal
def genereaza_sinus(amplitudine, frecventa, faza, durata, rata_esantionare):
    t = np.linspace(0, durata, int(rata_esantionare * durata), endpoint=False)
    y = amplitudine * np.sin(2 * np.pi * frecventa * t + faza)
    return t, y

# Citim parametrii de la utilizator
amp1 = float(input("Amplitudine semnal 1: "))
freq1 = float(input("Frecvență semnal 1 (Hz): "))
fase1 = float(input("Fază semnal 1 (radiani): "))

amp2 = float(input("Amplitudine semnal 2: "))
freq2 = float(input("Frecvență semnal 2 (Hz): "))
fase2 = float(input("Fază semnal 2 (radiani): "))

durata = 2  # secunde
rata_esantionare = 1000  # Hz

# Generăm semnalele
t1, y1 = genereaza_sinus(amp1, freq1, fase1, durata, rata_esantionare)
t2, y2 = genereaza_sinus(amp2, freq2, fase2, durata, rata_esantionare)

# Calculăm convoluția
convolutie = signal.convolve(y1, y2, mode='full')
t_conv = np.linspace(0, 2 * durata, len(convolutie), endpoint=False)

# Afișăm semnalele și convoluția
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t1, y1, color="blue")
plt.title("Semnal 1")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t2, y2, color="green")
plt.title("Semnal 2")
plt.grid(True)
plt.subplot(3, 1, 3)
plt.plot(t_conv, convolutie, color="red")
plt.title("Convoluția")
plt.grid(True)

plt.tight_layout()
plt.show()
