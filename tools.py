class Liste:
    """liste chainee
    tete : attribut qui contient la liste

    estVide : méthode qui teste si al liste est vide ou pas
    ajoute: méthode qui ajoute un élément à gauche de la liste"""


    def __init__(self):

        self.tete = None


    def estVide(self):
        return self.tete is None

    def ajoute(self,x):
        self.tete = Cellule(x,self.tete)

class Cellule:
    """ définit la classe Cellule
    valeur : attribut qui contient le premier élément
    suivante : attribut qui contient la suite de la liste"""
    def __init__(self,v,s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        return str(self.valeur)

def len_lstc(l):
    if l == None: return 0
    return 1 + len_lstc(l.suivante)
    
def index_lstc(l,n):

    long = len_lstc(l)
    assert (n<long and n>=0 and type(n) == int),"index en dehors du rang"

    for k in range(n):
        l=l.suivante
    return l.valeur

def empty_lstc(l):
    """fonction qui teste si une liste est vide """
    return l is None


def print_lstc(l,res=""):
    """fonction qui renvoie une chaine de caractères avec les éléments de la liste"""
    while not empty_lstc(l): res, l = res + str(f"[{l.valeur}]"), l.suivante
    return res