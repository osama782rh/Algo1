# TP Algo Python

# Exercice 1
# Cherche élément dans une liste (non triée)
def recherche_seqeuntielle(lst, x):
    for val in lst:
        if val == x:
            return True
    return False


# Cherche élément dans une liste triée
def cherche_elem_dicho(lst, x):
    debut, fin = 0, len(lst) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if lst[milieu] == x:
            return True
        elif lst[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return False


# Exercice 2
# Calcule factorielle de façon récursive
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


# Calcule suite de Fibonacci de façon récursive
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


# Vérifie si un mot est palindrome de façon récursive
def palindrome(mot):
    if len(mot) < 2:
        return True
    if mot[0] != mot[-1]:
        return False
    return palindrome(mot[1:-1])


# Exercice 3
# Vérifie tableau en zigzag
def zigzag(tab):
    for i in range(len(tab) - 1):
        if i % 2 == 0:
            if tab[i] >= tab[i + 1]:
                return False
        else:
            if tab[i] <= tab[i + 1]:
                return False
    return True


# Exercice 4
import numpy as np
import time


# Simulation simple du modèle de machine learning demandé
def simule_modele(seq):
    return np.mean(seq, axis=0, keepdims=True)


# Fonction optimisée
def optimisation_simple(M):
    n, _, _ = M.shape
    resultats = []
    for i in range(0, n - 1, 5):
        if np.all(M[i] - M[i + 1] == 10):
            pred = simule_modele(M[i])
            resultats.append(pred.tolist()[0])
    return resultats






# Menu simple pour exécuter les exercices
def menu():
    while True:
        print("\nTP Algo Python - Menu")
        print("1. Recherche sequentielle")
        print("2. Recherche dichotomiquement")
        print("3. Factorielle")
        print("4. Fibonacci")
        print("5. Tester palindrome")
        print("6. Vérifier zigzag")
        print("7. Optimiser code")
        print("8. Quitter")

        choix = input("Votre choix (1-8): ")

        if choix == '1':
            lst = [2, 4, 6, 8, 10]
            x = int(input("Nombre à chercher : "))
            print("Trouvé :", recherche_seqeuntielle(lst, x))
        elif choix == '2':
            lst = [1, 2, 3, 4, 5, 6]
            x = int(input("Nombre à chercher : "))
            print("Trouvé :", cherche_elem_dicho(lst, x))
        elif choix == '3':
            n = int(input("Entrez un nombre : "))
            print("Résultat :", fact(n))
        elif choix == '4':
            n = int(input("Terme Fibonacci : "))
            print("Résultat :", fibo(n))
        elif choix == '5':
            mot = input("Entrez un mot : ")
            print("Palindrome ?", palindrome(mot))
        elif choix == '6':
            tab = [int(i) for i in input("Éléments du tableau séparés par espace : ").split()]
            print("En zigzag ?", zigzag(tab))
        elif choix == '7':
            M = np.random.randint(0, 20, (1000, 8, 200))

            # Force la condition pour avoir un résultat visible
            for i in range(0, 995, 5):
                M[i] = M[i + 1] + 10

            debut = time.time()
            resultats = optimisation_simple(M)
            fin = time.time()

            print(f"Nombre de résultats obtenus : {len(resultats)}")
            print(f"Temps d'exécution optimisé : {fin - debut:.4f} secondes")
        elif choix == '8':
            print("Programme terminé.")
            break
        else:
            print("Erreur, choix invalide.")


if __name__ == '__main__':
    menu()