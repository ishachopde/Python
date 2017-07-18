import random

def menu():
	# ask for user numbers
	# calculate lottery numbers
	# print the winnings
	user_number_method = get_user_numbers()
	lottery_numbers_method = create_lottery_numbers()
	
	matched = user_number_method.intersection(lottery_numbers_method)
	print( "You matched {}. You won ${}".format(matched, 100 ** len(matched)))


# User picks 6 numbers
def get_user_numbers():
	number_csv = input("Enter 6 numbers (separate with commas): ")
	number_list = number_csv.split(",")
	integer_set = {int(numbers) for numbers in number_list}
	return integer_set

# Lottery calculates 6 random numbers (b/w 1-20)
def create_lottery_numbers():
	values = set()
	loops = 6
	while len(values) < loops:
		values.add(random.randint(1,20))
	return values



menu()
# we match the user numbers to the lottery numbers

# calculate the winnings based on how many numbers the user matched






