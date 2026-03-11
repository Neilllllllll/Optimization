# Simulated Annealing 
C'est une méthode heuristique pour optimiser une fonction objective.
Elle est utilisé lorsque la fonction possède une grosse range avec plusieurs minimums globales.

# Inspiration physique
L'idée est de simuler le processus de refroidissement d'un métal, où les atomes se déplacent pour trouver une configuration d'énergie minimale.
Lorsque la température est forte, les atomes bougent énormément et explore plein de configurations. Plus la température baisse plus les atomes se figent dans une certaines configurations. 

# Contexte d'optimisation 

| Optimisation | Physique |
|--------------|----------|
| Agencement des atomes | Solutions candidates |
| Energie | Fonction de coût |
| Température | Paramètre d'exploration | 
| Statut minimale d'énergie | Solution optimale | 

Le but de la méthode est de minimiser une fonction de cout. 

$$ \min f(x) $$

 # Propriétés principales

 $$ P = \exp\left(-\frac{\Delta E}{T}\right) $$

 - **P** est la probabilité d'accepter une solution pire que la solution actuelle.
 - **ΔE** est la différence de coût entre la solution actuelle et la nouvelle solution.
 - **T** est la température.

 > La température est un paramètre important dans la méthode car elle contrôle la probabilité d'accepter une solution pire que la solution actuelle, ce qui a pour incidence directe sur la capacité de l'algorithme à explorer l'espace de solutions et à éviter les minima locaux.

# Algorithme de base

L'algorithme explore l'espace de solutions en diminuant la température progressivement.

## Etape 1 : Initialisation

- Choisir une solution initiale $x_0$.
- Choisir une température initiale $T_0$.

## Etape 2 : Générer un voisin

On génère une nouvelle solution $x'$ à partir de la solution actuelle : $$ x' = x + \Delta x $$

- **Δx** est une petite perturbation aléatoire.

## Etape 3 : Evalution du coût

On calcule la différence de coût entre la solution actuelle et la nouvelle solution : $$ \Delta E = f(x') - f(x) $$

## Etape 4 : Acceptation de la nouvelle solution

Si $$ \Delta E < 0 $$
- Accepter la nouvelle solution $x'$.

Si $$ \Delta E \geq 0 $$
- Accepter la nouvelle solution $x'$ avec une probabilité de $$ P = \exp\left(-\frac{\Delta E}{T}\right) $$

## Etape 5 : Mise à jour de la température

Réduire la température graduellement. 
$$ T = \alpha T $$

- **α** est un factelsur de refroidissement (0.8 < α < 1).

On appelle ce procéder le calendrier de refroidissement.

## Etape 6 : Terminaison
On arrete lorsque 
- La température est suffisamment basse.
- Un nombre maximum d'itérations est atteint.
- On détecte une convergence


