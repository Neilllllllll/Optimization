import numpy as np
import matplotlib.pyplot as plt

# Fonction objective
def f(x):
    return x**4 - 4*x**2

x = np.linspace(-3, 3, 100)

# Initilisation
x_init = np.random.uniform(-3, 3)
T = 10
alpha = 0.95
Tmin = 0.01

history = []
while T > Tmin:
    history.append((x_init, f(x_init)))

    # Générer une solution voisine
    x_new = x_init + alpha

    # Calculer la variation d'énergie
    delta = f(x_new) - f(x_init)

    # Condition d'acceptation
    if delta < 0:
        x_init = x_new
    else:
        p = np.exp(-delta / T)
        if np.random.rand() < p:
            x_init = x_new

    # Refroidissement
    T *= alpha

plt.plot(x, f(x))
plt.scatter(*zip(*history), color='red')
plt.title("Simulated Annealing")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()