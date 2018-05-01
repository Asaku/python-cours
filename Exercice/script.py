#!/usr/bin/env python
# coding: utf-8

def exo01():
	i=0
	while i <= 500:
		print("Je dois faire des sauvegardes régulières de mes fichiers.")
		i = i + 1

def exo02():
	for i in range(0,1000):
		if i % 2 != 0:
			print(i)

def exo03():
	i=0
	while i <= 10:
		print(i*13)
		i=i+1

def exo04():
	word = raw_input("Merci de saisir un mot : ")
	print(len(word))

def exo05():
	number = int(raw_input("Merci de saisir un nombre entier : "))
	if number % 2 != 0:
		print("Votre nombre est impair.")
	else:
		print("Votre nombre est pair.")

def exo06():
	number = int(raw_input("Entrez un nombre entre 10 et 20 :"))
	if number < 10:
		print("Plus grand!!")
		exo06()
	if number > 20:
		print("Plus petit!!")
		exo06()
	print("ok")

def exo07():
	user_input = int(raw_input("Entrez un nombre entier: "))
	print(range(int(user_input)+1, int(user_input)+11))

def exo08():
	nb = int(raw_input("Entrez un nombre entier :"))
	for i in range(1,11):
		print(i , "*", nb , "=", i*nb)

def exo09():
	nombre=int(raw_input("entrer votre nombre"))
	liste=[]
	for i in range(0,nombre+1,1):
		liste.append(i)
	print(sum(liste))

def exo10():
	nombre=int(raw_input("entrer votre nombre : "))
	if nombre >= 6 and nombre <= 7:
		print("Vous etes poussin !")
	elif nombre >= 8 and nombre <= 9:
		print("Vous etes pupille !")
	elif nombre >= 10 and nombre <= 11:
		print("Vous etes minime !")
	elif nombre > 12:
		print("Vous etes Cadet !")

def exo11():
	i=0
	nbrArticle = int(raw_input("Combien avez-vous d'articles ? "))
	listPriceHt = []
	while i != nbrArticle:
		i += 1
		prixHT=float(raw_input("Combien coûte l'article ? "))
		listPriceHt.append(prixHT)

	ttc = 1.20
	total= sum(listPriceHt)

	print("Nombre d'articles : ", nbrArticle)
	print(listPriceHt)
	print("Prix HT : ", total)
	print("Prix TTC : ", ttc*total)

def exo12():
	number = int(raw_input("entrer votre nombre : "))
	count = number
	while number > 1:
		number = number - 1
		count = count * number
	print(count)

import random, emoji

def nb_mystere():
	i = 9
	rand = random.randint(1, 100)
	while i > 1:
		enter = int(input("Veuillez saisir un nombre : "))
		if enter < rand:
			print("Le chiffre est superieur")
		elif enter > rand:
			print("Le chiffre est inferieur")
		elif enter == rand:
			print("Gagné")
			break
		i = i - 1
		print(emoji.emojize(":heart:"*i))
nb_mystere()
