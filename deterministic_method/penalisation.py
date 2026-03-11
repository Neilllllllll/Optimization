import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Fonction objective
def f(x, y):
    return  x**3 + y**2 + x*y + 60

# Fonction de pénalisation 
def F(x, y, mu):
    return f(x, y) + mu*(x + y - 10)**2

# Dérivé partiel en fonction de x
def grad_x(_x,_y,_mu):
    x, y, mu = sp.symbols('x y mu')
    grad = sp.diff(F(x, y, mu), x, 1)
    val = grad.subs({x: _x, y: _y, mu: _mu})
    return val

# Dérivé partielle en fonction de y
def grad_y(_x,_y,_mu):
    x, y, mu = sp.symbols('x y mu')
    grad = sp.diff(F(x, y, mu), y, 1)
    val = grad.subs({x: _x, y: _y, mu: _mu})
    return val

x = 0
y = 0
mu = 1
alpha = 0.05
traj_x = []
traj_y = []
for k in range(60):
    x = x - alpha * float(grad_x(x, y, mu))
    y = y - alpha * float(grad_y(x, y, mu))
    traj_x.append(x)
    traj_y.append(y)