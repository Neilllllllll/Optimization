import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Fonction objective
def f(x, y):
    return  x**3 + y**2 + x*y + 60

# Fonctions de contraintes
def c1(x, y):
    return x + y - 10

def c2(x, y):
    return x - y - 2

# Lagrange
def lagrange(x, y, lambda1, lambda2):
    L = f(x, y) + lambda1 * c1(x, y) + lambda2 * c2(x, y)
    return L

x, y, lambda1, lambda2 = sp.symbols('x y lambda1 lambda2')

# Dérivés partielles
derivate_x = sp.diff(lagrange(x, y, lambda1, lambda2), x, 1)
eq1 = sp.Eq(derivate_x, 0)

derivate_y = sp.diff(lagrange(x, y, lambda1, lambda2), y, 1)
eq2 = sp.Eq(derivate_y, 0)

derivate_lambda1 = sp.diff(lagrange(x, y, lambda1, lambda2), lambda1, 1)
eq3 = sp.Eq(derivate_lambda1, 0)

derivate_lambda2 = sp.diff(lagrange(x, y, lambda1, lambda2), lambda2, 1)
eq4 = sp.Eq(derivate_lambda2, 0)

print("Equations à résoudre :")
print(derivate_x, "= 0")
print(derivate_y, "= 0")
print(derivate_lambda1, "= 0")
print(derivate_lambda2, "= 0")

print(" ")

# Résolution du système d'équations
solution = sp.solve([eq1, eq2, eq3, eq4], (x, y, lambda1, lambda2))

# Vérification de la solution
if(c1(solution[0][0], solution[0][1]) != 0 or c2(solution[0][0], solution[0][1]) != 0):
    print("La solution n'est pas valide")
else:
    print("La solution est valide, x =", solution[0][0], "y =", solution[0][1], "f(x, y) =", f(solution[0][0], solution[0][1]))

density = 100

_x = np.linspace(-1000, 1000, num=density)
_y = np.linspace(-1000, 1000, num=density)

X, Y = np.meshgrid(_x, _y)
Z = f(X, Y)
C1 = c1(X, Y)
C2 = c2(X, Y)
# Créer un objet Axes3D pour le graphique 3D
plt.figure("Exemple de courbe en 3D")
axes = plt.axes(projection="3d")
print(axes, type(axes))

# Tracer les lignes en 3D
axes.plot_surface(X, Y, Z, cmap='viridis')
axes.plot(X, Y, C1, color='red')
axes.plot(X, Y, C2, color='blue')
# Affichage de la solution
axes.scatter(float(solution[0][0]), float(solution[0][1]), float(f(solution[0][0], solution[0][1])), color='red', label='Solution optimale', s=100)

# Ajouter des étiquettes pour les axes
axes.set_xlabel("X")
axes.set_ylabel("Y")
axes.set_zlabel("Z")

# Afficher le graphique en 3D
plt.show()
