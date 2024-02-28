"""SECTION1: LES VARIABLES
  __auteur__: Mamadou Sadio Diallo
"""

#Declaration de variable

titre = "Registre de presence au cours"
annee_academique = "2023-2024"
group = "PR G19"
date_cours = "25/02/2024"
prix_unitaire = 555.5
celibataire = False
jour_ferie = True
nom_du_pere = None

#Affichage des valeurs
#On utilise le formatage des chaines de caractere avec cette methode
print("Titre: " + titre)
print("annee academique: " + annee_academique)
print("group: "+ group)
print("Date cours: " + date_cours)
print("Prix Unitaire: " + str(prix_unitaire))
print("Celibataire" + str(celibataire))
print("Jour ferie: " + str(jour_ferie))
print("Nom du pere: " + str(nom_du_pere))

print()

"""
Les types de variable en python
Nombre = nombre entier: int
          nombre reels: float
          chaine de caractere: str
          booleen: TRUE/FALSE
          Null: NONE
"""

"""
Formatage des chaines de caracteres
Voici une autre mnethode
"""
print(f"titre: {titre}")
print(f"Annee Academique: {annee_academique}")
print(f"Groupe: {group}")
print(f"Date Cours: {date_cours}")
print(f"Prix Unitaire: {prix_unitaire}")
print(f"Celibataire: {celibataire}")
print(f"Jour Ferie: {jour_ferie}")
print(f"Nom Du Pere: {nom_du_pere}")

"""SECTION1: LES VARIABLES V2
  __auteur__: Mamadou Sadio Diallo
"""

def main():
  """
  Fonction principale
  """
  titre = "registre de presence au cours"
  annee_academique = "2023-2024"
  group = "PR G19"
  date_cours = "25/02/2024"
  prix_unitaires = 2026.02
  Celibataire = False
  jour_ferie = True
  nom_du_pere = None


#Affichage des variables
print(f"Titre: {titre}")
print(f"Annee Academique: {annee_academique}")
print(f"Groupe: {group}")
print(f"Date cours: {date_cours}")
print(f"prix unitaire: {prix_unitaire}")
print(f"Celibataire: {celibataire}")
print(f"Jour ferie: {jour_ferie}")
print(f"Nom Du pere: {nom_du_pere}")

main()

from ast import Module
"""SECTION3: User_Input
  __auteur__: Mamadou Sadio Diallo

  Rendre un programme interactif en recuperant l'input de l'utilisateur
"""

def main():
  """Fonction principale"""
  Module = input("Nom du module: ")
  Volume_Horaire = input("Volume Horaire: ")
  Prof = input("Nom du prof: ")
  date_cours = input("Date du cours: ")
  Debut = input("Heure de debut: ")
  Fin = input("Heure fin: ")
  Salle = input("Salle de cours")
  Solde_Heure = input("Nombre d'heure restant")

print(f"Module: {Module}")
print(f"Volume horaire: {Volume_Horaire}")
print(f"Nom du professeur: {Prof}")
print(f"Date cours: {date_cours}")
print(f"Heure de debut: {Debut}")
print(f"Heure de fin: {Fin}")
print(f"Salle de cours: {Salle}")
print(f"solde heure: {Solde_Heure}")

if __name__ == "__main__":
  main()


"""SECTION4: LES NOMBRES ALEATOIRES
  __auteur__: Mamadou Sadio Diallo
"""

import random
def main():
  """Fonction Principale"""
  nombre = random.randint(1,10) #Permet de generer des nombres aleatoire de 1 a 10
  print(nombre)

if __name__ == "__main__":
  main()

"""SECTION4: LES NOMBRES ALEATOIRES
  __auteur__: Mamadou Sadio Diallo
"""
Ma_List = [12,15,8,9,45]
les_String = ["les chaussures", "les arachides","Les boulangers", "Les sangliers"]
print(Ma_List)
les_String.append("les amendes")
print(les_String)

# Pour des données plus complexes, vous pouvez utiliser la fonction deepcopy du module copy
import copy

x = [[1,2],3]
y = copy.deepcopy(x)
y[1] = [1,2,3]
print(y)
print(x)

# Transformer une string en liste
ma_chaine = "Olivier:Momar:Magui"
ma_chaine.split(":")

ma_list = ["Leo", "Oscar"]
":".join(ma_list)

# Trouver un item dans une liste
num = [12,15,5,6,9]
12 in num

# Agrandir une liste par une liste
op = [1,2,3,4,5]
og = [6,7,8,9,10]
op.extend(og)
print(op)

from itertools import permutations
list(permutations(["a", "b", "c"]))

# Les tuples python
# Un tuple est une liste qui ne peut plus être modifiée.
ma_tuple = ()
ma_tuple2 = (1, "Ok", "bravo")
print(ma_tuple2)
type(ma_tuple2)

def donne_ton_nom():
  return "olivier","angel"

donne_ton_nom()

# Les dictionnaires python
a = {}

a = dict()
a["nom"] = "wayne"
a["prenom"] = "Jiip"
a


# Comment récupérer une valeur dans un dictionnaire python?
data = {"name":"Mamadou", "Age":45}
data.get("Age")
data.get("name")
# Comment supprimer une entrée dans un dictionnaire python?
del data["name"]

data

# Comment récupérer les clés d'un dictionnaire python par une boucle?
fiche = {"nom": "Mamadou", "Prenom":"Sadio"}
for cle in fiche.keys():
  print(cle)

# Comment récupérer les valeurs d'un dictionnaire python par une boucle?
fiche2 = {"Age":22, "adress": "Dakar, Senegal"}
for cle, values in fiche2.items():
  print(cle,values)



# Les fonctions python
def mon_age():
  return 28
mon_age()

def augmentation(a):
  return a + 2
augmentation(1)

def augmentation2(a, b):
  return 30 + a + b
augmentation2(2,3)
def ton_nom(a):
    return input("donnez votre nom ici")
ton_nom("Mamadou")

def param(prenom,nom,age):
  return prenom + " " + nom + " " + str(age)
print("Votre nom est " + param("mamadou", "diallo", 28))

# Portée des variables (variable globale et variable locale)
x = "Hello"
def myvar():
  return x
myvar()


from posixpath import join
# Les fonctions natives de python
# les fonction native sont ceux qui viennent avec python apres l'installation de celui ci dans la machine.
#le plus connu est la fonction print qui permet d'afficher les resultats d'un code a l'ecran

abs(24) # cette fonction retourne la valeur absolue d'un nombre donnee

#all(iterable) : retourne True si tous les elements d'un iterable sont True
liste = [True, True, True,1]
all(liste)

# any(iterable): Retourne True si au moins un element d'un element iterable est True
liste2 = [True, True, False]
any(liste2)

#bin(): Converti un entier en chaine de caractere
bin(123)

#callable(): Determine si un objet est callable
callable("A")

# La méthode capitalize permet de mettre une chaine de caractères au format Xxxxx
nom = "oLivIer"
nom.capitalize()

#choice([]): retourne les valeurs d'une liste aleatoire
import random
random.choice([20,36,58,96])

#count() permet de compter le nombre d'occurence dans une recherche
le_nom = "Metalou alaou aparou"
le_nom.count('a')

#dir(objet): indique les noms de la structure de l'objet
dir(int)

#hex(): convertie une valeur en hexadecimal
hex(10)

#isalnum(): retourne True si tout les caracteres sont alphanumerique
"25".isalnum()

#str.isalpha(): retourne True si tous les caractere sont des lettres et qu'il ya ay moins un caractere
"diallo".isalpha()

#str.isdigit(): retourne True si tous les caractere numerique et qu'il ya au moins un caractere
"1".isdigit()
"a".isdigit()
"12.3".isdigit()

#str.islower(): retourne True si tous les caracteres sont en miniscule
"Mamadou".islower()

#str.isspace(): retourne true si il y a un espace
" ".isspace()
"mamadou sadio".isspace()

#str.isupper(): retourne True si tous les caracteres sont en majuscule
"Mamadou".isupper()
"MAMADOU".isupper()

#str.join(list): La methode join transforme une liste en chaine de caractere
":".join(["Mamadou", "Sadio"])

#len(s): retourne le nombre d'items d'un objet
len([1,36,25,58])
len("Mamadou sadio diallo")

#locals(): retourne un dictionnaire avec les valeurs des variable en cours
locals()

#str.lower(): la methode lower permet de mettre une chaine de caractere en miniscule
"DIOSE".lower()

#map(function,[]): execute une fonction sur chaque item d'un element iterable
def add_no(x):
  return x + 12
map(add_no, [12,25])

#max()/min(): retourne la valeur la plus eleve pour max et la moin eleve pour min
mes_nombre = [22,56,3698,32,15]
max(mes_nombre)
min(mes_nombre)

#radint(): retourne un int aleatoire
import random
random.randint(12,50)

#random(): permet de generer des nombre aleatoire
import random
random.random()

#str.replace(string, string): permet de remplacer un segment d'une chaine de caractere par un autre
"Mamadou".replace("a", "o")

#reverse(): la methode reverse inverse l'ordre d'une liste
x = [4,58,12,69]
x.reverse()
x
