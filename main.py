from tools import *

# Constuire maListe qui contient 1-2-4-||

##Exercice 1
print("EXERCICE 1 :")
#1
resTarot = Cellule(("Marc", 1003),
                   Cellule(("Lise", 785),
                           Cellule(("Jean", 520), Cellule(("Lou", 980),
                                                          None))))

#2
"""resTarot.valeur renvoie le Tuple"""
#3
"""resTarot.suivante renvoie la position de la liste, mais pas la valeur suivante, pour cela il faut écrire print(rezTarot.suivante) """


##
def estVide(l):
    """fonction qui teste si une liste est vide """
    return l is None


def afficheListe(l):
    """fonction qui renvoie une chaine de caractères avec les éléments de la liste"""

    rez = '| '
    while not estVide(l):
        rez, l = rez + str(f"{l.valeur} | "), l.suivante
    return rez


##Exercice 2
print("EXERCICE 2 :")


def afficheListeRecur(l):
    if l == None:
        return ''
    return f" {(l.valeur)} | {afficheListeRecur(l.suivante)}"


print(print_lstc(resTarot))

# après l'exercice 2


def longueurListe(l):

    if l == None:
        return 0
    return 1 + longueurListe(l.suivante)


lst = Cellule(1, Cellule(2, Cellule(3, None)))

print(longueurListe(lst))

## Exercice 3
print("EXERCICE 3 :")


def longueurListeIterat(l):
    rez = 0
    while not estVide(l):
        l = l.suivante
        rez += 1
    return rez


print(longueurListeIterat(resTarot))

##


def nIemeElementListe(l, n):
    long = longueurListe(l)
    assert (n < long and n >= 0), "index en dehors du rang"
    for k in range(n):
        l = l.suivante
    return l.valeur


## Exercice 4
print("EXERCICE 4 :")


def nIemeElementListeWhile(l, n):
    long = len_lstc(l)
    assert (n < long and n >= 0 and type(n) == int), "index en dehors du rang"
    while n > 0 and not estVide(l):
        l = l.suivante
        n -= 1
    return l.valeur


print(nIemeElementListeWhile(resTarot, 0))


#3
def nIemeElementListeRecur(l, n):
    if l == None or n == 0:
        return l.valeur
    return nIemeElementListeRecur(l.suivante, n - 1)


print(nIemeElementListeRecur(resTarot, 0))


##
def concatenerListe(l1, l2):
    if l1 is None:
        return l2
    return Cellule(l1.valeur, concatenerListe(l1.suivante, l2))


liste1 = Cellule(1, Cellule(2, Cellule(3, Cellule(2, Cellule(7, None)))))
liste2 = Cellule(4, Cellule(5, Cellule(6, None)))
print(concatenerListe(liste1, liste2))

##Exercice 5
print("EXERCICE 5 :")


#1
def renverserListe(l):
    """renvoie la liste renversée de celle de l"""
    rez = None
    while not l is None:
        rez = Cellule(l.valeur, rez)
        l = l.suivante
    return rez


#2(a)
def renverserListe(l):
    """ renvoie la liste renversée de l"""
    if l is None:
        return None
    return concatenerListe(renverserListe(l.suivante), Cellule(l.valeur, None))


#2(b) il faudrait 25000 opérations pour renverser la liste si elle contient 1000 éléments

#2(c) j'en déduis que cette fonction est d'une complexité importante

## Exercice 6
print("EXERCICE 6 :")

#1
maListe = Cellule(1, Cellule(2, Cellule(7, Cellule(10, None))))
maListe.suivante.valeur = 9

#2
maListe.suivante.suivante = Cellule(7, None)

# Exercice 7
print("EXERCICE 7 :")


class Liste:
    """ Liste chainée :
    tete -> attribut qui contient la liste
        Liste des méthodes :
    estVide -> méthode qui teste si la liste est vide ou non
    ajoute -> méthode qui ajoute un élément à gauche de la liste"""
    def __init__(self, _tete=None):
        self.tete = _tete

    def estVide(self):
        return self.tete is None

    def ajoute(self, x):
        self.tete = Cellule(x, self.tete)

    def __str__(self, rez=""):
        """fonction qui renvoie une chaine de caractères avec les éléments de la liste"""
        while not empty_lstc(l):
            rez, l = rez + str(f"[{l.valeur}]"), l.suivante
        return rez

    def empty_lstc(l):
        """fonction qui teste si une liste est vide """
        return l is None


liste1 = Cellule(1, Cellule(2, Cellule(3, Cellule(4, None))))
liste = Liste()
print()