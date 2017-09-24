#!/usr/bin/python3
# coding: utf-8
'''
import math as toto
a = 12
b = 6

print(toto.acosh(a + b))

if a < b:
	print(a + b)
else:
	print('hihou')

def maFunction(param1, param2='hihouuuu'):
	print(param1)
	print(param2)

maFunction(1)
'''

import os
#Fonction randrange nécessaire pour générer un nombre aléatoire.
from random import randrange
 
#On initie la variable nombrePropose à n'importe quelle valeur sauf entre 1 et 100 sinon il se pourrait que se soit précisement le nombre mystère !.
nombrePropose = 0
 
#Un titre pour faire joli.
print("\t\t\t\t=== LE JEU DU PLUS OU MOINS ===\n\n")
 
#On génère le nombre mystère.
nombreMystere = randrange(1, 100)
 
#Boucle qui continuera tant que l'utilisateur n'aura pas trouvé le nombre.
while nombrePropose != nombreMystere:
     
    print("Quel est le nombre ?")
 
    #L'utilisateur propose son nombre.
    nombrePropose = input()
    nombrePropose = int(nombrePropose)
 
    #Si le nombre est trop petit...
    if nombrePropose < nombreMystere:
        print("C'est trop petit !\n")
 
    #Sinon si le nombre est trop grand...
    elif nombrePropose > nombreMystere:
        print("C'est trop grand !\n")
 
    #Sinon (sous-entendu : si on a trouvé le nombre)...
    else:
        print("Félicitations, vous avez trouvé le nombre mystère !!!\n")
 
#On met le système en pause.
os.system("pause")
 
#Et voilà !!!