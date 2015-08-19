def get_bullcow(guess, rand_num):
	"""This function evaluates and returns the number of bulls and cows."""
	guessed_list = list(guess)	#converting the strings to lists to check for bulls
	magic_list = list(rand_num)  #assuming rand_num is string
	list_bulls = []
	cows = 0
	bulls = 0

# iterating the two lists to find matches and get a count of bulls	
	for i in range(num_of_digits):
		if guessed_list[i] == magic_list[i]:
			bulls += 1
			list_bulls.append(guessed_list[i])
			
#eliminating the bulls to find cows
	for item in list_bulls:
		guessed_list.remove(item)
		magic_list.remove(item)

#iterating the remaining lists to get a count for cows
	for item in guessed_list:
		if item in magic_list:
			cows += 1
							
	print bulls,"bull(s)",cows,"cow(s).",
	return bulls, cows
	
