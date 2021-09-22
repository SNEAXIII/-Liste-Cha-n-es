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


## Exercice 7
"""à compléter dans la classe"""

#1
print(len(maListe))

#2

##Exercice 8

"""A compléter dans la classe Liste"""



##Exercice 9

#1
def listeN(n):



#2


def occurences(x,lst):


#3
def trouve(x,lst):


#4

def egalite(l1,l2):

#5 A faire dans la classe


#6

def suppr(rg,lst):



#7 A faire  dans la classe Listeclass Cellule:
    """ définit la classe Cellule
    valeur : attribut qui contient le premier élément
    suivante : attribut qui contient la suite de la liste"""
    def __init__(self,v,s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        return str(self.valeur)

# Constuire maListe qui contient 1-2-4-||


##Exercice 1

#1
resTarot =

#2
"""resTarot.valeur renvoie      """

#3
"""resTarot.suivante renvoie      """

##
def estVide(l):
    """fonction qui teste si une liste est vide """
    return l==None


def afficheListe(l):
    """fonction qui renvoie uen chaien de caractères avec les éléments de la liste"""

    res = '| '
    while not estVide(l):
        res+=str(l.valeur)+' '
        l=l.suivante
    return res+'|'

##Exercice 2



def afficheListeRecur(l):



##

def longueurListe(l):

    if l==None:
        return 0
    return 1+longueurListe(l.suivante)

lst=Cellule(1,Cellule(2,Cellule(3,None)))


##Exercice 3
def longueurListeIterat(l):



##

def nIemeElementListe(l,n):

    long = longueurListe(l)
    assert (n<long and n>=0),"index en dehors du rang"

    for k in range(n):
        l=l.suivante
    return l.valeur

##Exercice 4
#1 à faire dans le script

#2
def nIemeElementListeWhile(l,n):


#3
def nIemeElementListeRecur(l,n):



##
def concatenerListe(l1,l2):

    if l1 is None:
        return l2
    return Cellule(l1.valeur,concatenerListe(l1.suivante,l2))

liste1= Cellule(1,Cellule(2,Cellule(3,Cellule(2,Cellule(7,None)))))
liste2 = Cellule(4,Cellule(5,Cellule(6,None)))

## Exercice 5

#1
def renverserListe(l):
    """renvoie la liste renversée de celle de l"""

    res = None
    while not l is None:
        res=Cellule()



    return res
#2(a)



#2(b)
"""Pour 1000 éléménts...."""

#2(c)
"""La complexité est en ...."""




##Exercice 6

#1

#2





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


## Exercice 7
"""à compléter dans la classe"""

#1
print(len(maListe))

#2

##Exercice 8

"""A compléter dans la classe Liste"""



##Exercice 9

#1
def listeN(n):



#2


def occurences(x,lst):


#3
def trouve(x,lst):


#4

def egalite(l1,l2):

#5 A faire dans la classe


#6

def suppr(rg,lst):



#7 A faire  dans la classe Liste