import numpy as np
import matplotlib.pyplot as plt

# Fonction objective 
def f(x):
    return 0.2*x + np.sin(5*x)

def fitness(population):
    liste = []
    # Calcule pour toute la population
    for i in range(0, len(population)):
        liste.append((population[i], f(population[i])))

    # Trie
    liste_trie = sorted(liste, key=lambda x: x[1])

    # Selection
    selection = []
    for i in range(0, 2):
        selection.append(liste_trie[i])
 
    return selection

# Population initiale
pop_size = 20
population = np.random.uniform(-5,15, pop_size)

print(fitness(population))

# Affichage

density = 20

x = np.linspace(-5, 15, num=density)
y = []

for i in range (0, len(x)):
    y.append(f(x[i]))

plt.plot(x, y)
plt.show()
