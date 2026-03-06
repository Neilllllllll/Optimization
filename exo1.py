from random import randint
import matplotlib.pyplot as plt
import numpy as np

# Fonction d'étude
def f(x):
    return 4*(x - 8)**2 + 15

# Fonction pour trouver le gradient numériquement
def grad(x, h=1e-5):
    return (f(x+h) - f(x-h)) / (2*h)

x_axes = np.linspace(-10, 100, 1000)
y_axes = f(x_axes)

i = randint(0, len(x_axes) - 1)
x = x_axes[i]
alpha = 0.001
y_point = [f(x)]
x_point = [x]
for k in range(1000):
    x = x - alpha * grad(x)
    x_point.append(x)
    y_point.append(f(x))

print("Minimum trouvé : x =", x, "f(x) =", f(x))

plt.plot(x_axes, y_axes)
plt.scatter(x_point, y_point, color='red')
plt.title("Etude logistique")
plt.xlabel("Volume transporté")
plt.ylabel("Coût")
plt.show()