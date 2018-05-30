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
	word = input("Merci de saisir un mot : ")
	print(len(word))

def exo05():
	number = int(input("Merci de saisir un nombre entier : "))
	if number % 2 != 0:
		print("Votre nombre est impair.")
	else:
		print("Votre nombre est pair.")

def exo06():
	number = int(input("Entrez un nombre entre 10 et 20 :"))
	if number < 10:
		print("Plus grand!!")
		exo06()
	if number > 20:
		print("Plus petit!!")
		exo06()
	print("ok")

def exo07():
	user_input = int(input("Entrez un nombre entier: "))
	print(range(int(user_input)+1, int(user_input)+11))

def exo08():
	nb = int(input("Entrez un nombre entier :"))
	for i in range(1,11):
		print(i , "*", nb , "=", i*nb)

def exo09():
	nombre=int(input("entrer votre nombre"))
	liste=[]
	for i in range(0,nombre+1,1):
		liste.append(i)
	print(sum(liste))

def exo10():
	nombre=int(input("entrer votre nombre : "))
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
	nbrArticle = int(input("Combien avez-vous d'articles ? "))
	listPriceHt = []
	while i != nbrArticle:
		i += 1
		prixHT=float(input("Combien coûte l'article ? "))
		listPriceHt.append(prixHT)

	ttc = 1.20
	total= sum(listPriceHt)

	print("Nombre d'articles : ", nbrArticle)
	print(listPriceHt)
	print("Prix HT : ", total)
	print("Prix TTC : ", ttc*total)

def exo12():
	number = int(input("entrer votre nombre : "))
	count = number
	while number > 1:
		number = number - 1
		count = count * number
	print(count)

def exo13():
	number = int(input("entrer votre nombre : "))
	binaire = []
	while number >= 1:
		modulo = int(number % 2)
		binaire.append(str(modulo))
		number = int(number / 2)
	binaire.reverse()
	print(''.join(binaire))

def exo14():
	a = 3
	somme_a = 0
	b = 5
	somme_b = 0
	while a < 1000:
		a = a + 3
		somme_a = a + somme_a
	while b < 1000:
		b = b + 5
		somme_b = b + somme_b
	print(somme_a)
	print(somme_b)

def exo15():
	a = 0
	fib = 1
	start = 0
	while a < 1500:
		a = a + 1
		n = fib + start
		start = fib
		fib = n
	print(fib)

def exo16(a = 1):
	i = 1
	while i < 5:
		if not (a/i).is_integer():
			exo16(a + 1)
		i = i + 1
	print(a)

def bubule():
	list = [4, 8, 415, 1, 25, 75, 6]
	last = True
	limit = len(list)
	while last:
		for i in range(0, limit-1):
			last = False
			if (list[i] > list[i+1]):
				list[i+1], list[i] = list[i], list[i+1]
				last = True
		limit = limit - 1
	print(list)

def insertion():
	list = [4, 8, 415, 1, 25, 75, 6]
	for i in range(1, len(list)):
		current = list[i]
		j = i
		while j > 0 and list[j - 1] > current:
			list[j] = list[j - 1]
			j = j - 1
		list[j] = current
	print(list)
