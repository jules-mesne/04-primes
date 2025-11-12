"""
Module main de l'exercice 04-primes.
Vérifie si un nombre est premier.
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Vérifie si un entier est un nombre premier ou pas.
    Retourne True si p est premier, False sinon.
    """

    # votre code ici

    if (p % 1 != 0 or p <= 1):
        return False
    imax  = int(sqrt(p)) + 1
    for i in range(2, imax) :
        if p % i == 0:
            return False
    return True


#### Fonction principale


def main():
    """
    Teste et fait quelques appels à la fonction secondaire
    permettant de vérifier son bon fonctionnement.
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
