#-*- coding: cp1252 -*-
#!/usr/local/bin/python3


""" L'encodage est :   #-*- coding: cp1252 -*-
    sur Linux ou Mac"""



# AFFICHAGE DE MESSAGE
print ("Premier test de Python")
input()


# AFFECTATION DE VARIABLES
a = 5
b = 6.3
c = a*b
# AFFICHAGE DE VARIABLES
print (a)
print (b)
print (c)
input()


# AFFICHAGE SIMULTANE DE VARIABLES ET DE MESSAGE
print ("Le produit de",a,"par",b,"est :",c)
input()


# SAISIE DE VARIABLES
nom = input("Quel est votre pr�nom : ")             # pour cr�er une chaine de caract�res
age = int(input("Entrez votre age : "))             # pour cr�er un entier
taille = float(input("Entrez votre taille : "))     # pour cr�er un r�el
input()
print(type(nom))
print(type(age))



# INSTRUCTION CONDITIONNELLE
if (age>=18) :
    print ("Vous �tes majeur.\nVous pouvez entrer")
else :
    print ("Vous �tes encore trop jeune pour entrer.")
    print ("Il faut encore attendre",18-age,"ans.")
input()


# BOUCLE ITERATIVE POUR
for i in range(1,11):                          # Attention boucle de 1 � 10, le dernier entier n'est pas atteint
    print (i,"multipli� par 9 donne",9*i)
input()


# BOUCLE ITERATIVE TANT QUE
a = 0
while (a<5):
    print ("Dans la boucle, a =",a)
    a = a+1
print ("Une fois sorti de la boucle, a =",a)
input()
