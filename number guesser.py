attempts = int(0)
import random
num = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20, let's see if you can guess it.")
x = 0
while x != num:
	x = int(input("Your guess? "))
	if x > num:
		 print("Too high!!") 
	elif x < num:
 		print("Too low!!")
	else:
 		print("Correct!!")
