import random

guesses = 0
print("Welcome to Jake's Number Guessing Game!")
print("What is your name?")

yourName = input()
num = random.randint(1,51)

print("Nice to meet you, " + str(yourName) + "! I am thinking of a random number between 1 and 50. You only get 5 tries!")

while guesses < 6:
	print("Take a wild guess!")
	guess = input()
	guess = int(guess)
	guesses += 1

	if guess < num:
		print("Too low! You suck at this...")
	elif guess > num:
		print("Way too high there, buddy. Get it together!")
	elif guess == num:
		break

if guess == num:
	guess = str(guess)
	print("Wow, you finally got it right, " + yourName + ". It took you a whole " + str(guesses) + " tries...")
elif guess != num:
	num = str(num)
	print("You lose! The number was " + num + ", jackass!")

input("Game over.")





