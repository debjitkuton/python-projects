x = input("Choose rock, paper or scissor- ")
import random
words = ["rock", "paper", "scissor"]
word = random.choice(words)
while word == "rock":
	if x == "rock":
		print("I chose rock aswell.")
		print("Try again")
		break
	elif x == "paper":
		print("I chose rock.")
		print("You won")
		break
	elif x == "scissor":
		print("I chose rock.")
		print("You lost")
		break
while word == "paper":
	if x == "paper":
		print("I chose paper aswell.")
		print("Try again")
		break
	elif x == "scissor":
		print("I chose paper.")
		print("You won")
		break
	elif x == "rock":
		print("I chose paper.")
		print("You lost")
		break
while word == "scissor":
	if x == "scissor":
		print("I chose scissor aswell.")
		print("Try again")
		break
	elif x == "rock":
		print("I chose scissor.")
		print("You won")
		break
	elif x == "paper":
		print("I chose scissor.")
		print("You lost")
		break
