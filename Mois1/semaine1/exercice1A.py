import math
import random

#1A.1: demande un prénom et un âge, puis affiche "Bonjour Awa, tu auras 26ans l'an prochain"
#prenom = input("Votre prénom: ")
#age = input("Votre âge: ")
#print(f"Bonjour {prenom}, tu auras {int(age)+1} ans l'année prochaine")

#1A.2: dire si un nombre est pair ou pas
#nombre = input("Donnez un nombre: ")
#parite = "est pair" if (int(nombre)%2 == 0) else "est impair"
#print(f"{nombre} est {parite}")

#1A.3: affiche la table de multiplication d'un nombre saisi (de 1 à 10), au format 7 x 3 = 21
#nombre = input("Donner un nombre: ")
#print(f"La table de multiplication par {nombre} est:")
#for i in range(1,11):
#    print(f"{int(nombre)} x {i} = {int(nombre)*i}")

#1A.4: convertir_celsius(c) qui retourne la température en Fahrenheit (F = C x 9/5 + 32)
#def convertir_celsius(c):
#    return c*(9/5)+32
#temperature_en_celsius = input("Donnez la température en celsius: ")
#print(f"{temperature_en_celsius}°c correspond à {convertir_celsius(int(temperature_en_celsius))} Farenheit!!!")

#1A.5: Écris un programme qui affiche les nombres de 1 à 100. Pour les multiples de 3 affiche « Fizz »,
#pour les multiples de 5 « Buzz », pour les multiples des deux « FizzBuzz » (exercice classique d'entretien).
#for i in range(1,101):
#    if i%3 == 0:
#        print(f"{i}Fizz ")
#    elif i%5 == 0:
#        print(f"{i}Buzz ")
#    elif i%2 == 0:
#        print(f"{i}FizzBuzz ")
#    else:
#        print(i)

#1A.6: (moyen) Écris moyenne(liste) qui retourne la moyenne d'une liste de nombres. Teste-la avec [12,15, 9, 18].
#def moyenne(liste):
#    somme_des_elements_de_la_liste = 0
#    for i in range(0,len(liste)):
#        somme_des_elements_de_la_liste += liste[i]
#    return somme_des_elements_de_la_liste/len(liste)

#ma_liste = [12,15,9,18]
#print(f"{moyenne(ma_liste)}")


#1A.7: (moyen) Écris compter_voyelles(texte) qui retourne le nombre de voyelles (a, e, i, o, u, y) dans un texte, sans tenir compte de la casse.
#def compter_voyelles(texte):
#    nombre_de_a = f" {texte.count("a")} voyelles a" if texte.count("a") != 0 else "n'a pas de voyelles a"
#    nombre_de_o = f" {texte.count("o")} voyelles o" if texte.count("o") != 0 else "n'a pas de voyelles o"
#    nombre_de_i = f" {texte.count("i")} voyelles i" if texte.count("i") != 0 else "n'a pas de voyelles i"
#    nombre_de_e = f" {texte.count("e")} voyelles e" if texte.count("e") != 0 else "n'a pas de voyelles e"
#    nombre_de_u = f" {texte.count("u")} voyelles u" if texte.count("u") != 0 else "n'a pas de voyelles u"
#    nombre_de_y = f" {texte.count("y")} voyelles y" if texte.count("y") != 0 else "n'a pas de voyelles y"
#    print(f"Votre texte a {nombre_de_a}, {nombre_de_o}, {nombre_de_i}, {nombre_de_e}, {nombre_de_u}, {nombre_de_y}")

#votre_texte = "Bonjour, je m'appelle Simon Gildas"
#compter_voyelles(votre_texte)

#1A.8 Écris est_premier(n) qui retourne True si n est un nombre premier, puis affiche tous les nombres premiers inférieurs à 100.
"""def est_premier(n):
    if n !=0:
        if n < 0:
            n = n * (-1)
        trouve = True
        i = 2
        if n>2:
            while (trouve) and (i <= n**0.5):
                if n%i == 0:
                    trouve = False
                i += 1
            return trouve
        else:
            return trouve
    else:
        return False

nombre = input("Donner un nombre: ")
resultat = f"{nombre} est un nombre premier" if est_premier(int(nombre)) else f"{nombre} n'est pas un nombre premier"
print(resultat)
print("Voici la liste des nombres premiers compris entre 1 et 100")
for i in range(1,101):
    if est_premier(i):
        print(f"{i} ",end="")"""

#1A.9 Jeu « devine le nombre » : l'ordinateur choisit un nombre entre 1 et 100 (random.randint),l'utilisateur propose des valeurs, le programme répond « trop petit » ou « trop grand » et compte les essais.
nombre_a_deviner = random.randint(1,100)
#print(f"{nombre_a_deviner} est le nombre généré!!!")
trouve = False
nombre_de_tentatives = 0
while (not trouve):
    votre_proposition = input("Quel est le nombre à déviner: ")
    nombre_de_tentatives += 1
    if nombre_a_deviner == int(votre_proposition):
        trouve = True
    elif int(votre_proposition) > nombre_a_deviner:
        print("Trop grand")
    else:
        print("Trop petit")

print(f"Félicitations, il vous a fallu {nombre_de_tentatives} tentatives pour déviner le nombre")
