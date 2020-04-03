
##Methode d'Euler
import numpy as np
import matplotlib.pyplot as plt

#Euler seconde methode avec des listes sans indices:
def euler(f, t0, y0, T, N):
    h = (T-t0)/N
    #initialisation a la liste vide:
    X = []
    Y = []
    #conditions initiales:
    x = t0
    y = y0
    for k in range(N):
        X.append(x)
        Y.append(y)
        y = y + h*f(x, y) #attention l'ordre entre les lignes compte
        x = x + h
    return X, Y
#definition de f:
def f(x, y):
    return x*y
#application de la seconde methode:
X, Y = euler(f, 0, 1, 4, 1000)
#la solution theorique decalee de 200:
def g(x):
    return np.exp((x**2)/2 + 200)
#trace des courbes
T = np.linspace(0, 4, 1000)
U = g(T)
plt.plot(T, U)
plt.plot(X, Y)
plt.title("solution theorique decalee de 200 vers le haut \n" "et solution d'Euler de l'E.D. y' = xy ")
plt.xlabel("abscisse x")
plt.ylabel("fonction y(x)")
plt.legend(["solution theorique decalee de 200 vers le haut", "solution d'Euler seconde methode"])
plt.show()
