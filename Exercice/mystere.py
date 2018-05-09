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