import numpy as np
import matplotlib.pyplot as plt


def genereaza_sinus(amplitudine, frecventa, faza, durata, rata_esantionare):
    t = np.arange(0, durata, 1 / rata_esantionare)
    y = amplitudine * np.sin(2 * np.pi * frecventa * t + faza)
    return t, y


def convolutioneaza_semnale(semnal1, semnal2):
    return np.convolve(semnal1, semnal2, mode='full')

def vizualizeaza_semnale(t1, y1, t2, y2, y_conv, rata_esantionare):
    t_conv = np.arange(0, len(y_conv)) / rata_esantionare

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(t1, y1, label='Semnal 1')
    plt.title('Semnal 1')
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(t2, y2, label='Semnal 2', color='orange')
    plt.title('Semnal 2')
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(t_conv, y_conv, label='Convoluție', color='green')
    plt.title('Convoluția celor două semnale')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# =======================
# Parametrii definiți de utilizator
# =======================
amplitudine1 = 1.0
frecventa1 = 5  # Hz
faza1 = 0  # rad
durata1 = 1.0  # secunde

amplitudine2 = 0.5
frecventa2 = 3  # Hz
faza2 = np.pi / 4
durata2 = 1.0  # secunde

rata_esantionare = 1000  # Hz

# Generare semnale
t1, y1 = genereaza_sinus(amplitudine1, frecventa1, faza1, durata1, rata_esantionare)
t2, y2 = genereaza_sinus(amplitudine2, frecventa2, faza2, durata2, rata_esantionare)

# Convoluție
y_conv = convolutioneaza_semnale(y1, y2)

# Vizualizare
vizualizeaza_semnale(t1, y1, t2, y2, y_conv, rata_esantionare)
