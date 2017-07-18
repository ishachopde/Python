import random
magic_numbers= [random.randint(0,9), random.randint(0,9)]
chances = 3
for attempts in range(chances):
	user_number = int(input("Enter a number between 0 and 9: "))
	if user_number in magic_numbers:
		print("You got it right !")
	if user_number not in magic_numbers:
		print("Try again!")