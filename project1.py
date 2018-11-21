
# Ai Quynh Nguyen
# TCSS 142
# Nov 14, 2018
# Project 1 Assignment
#
# This program is a calculator that ask the users to input two numbers using
# Napier's notation(letters in the alphabeter to represent succesive powers of 2),
# and an arithmetic operator including add or subtract or multiple or divide.
# The pogram convert the Napeier notation into Hindy-Arabic decimal numbers, display them
# Then doing arithmetic operator on two of the entered Napier notation and display them in
# Hindu-Arabic decimal numbers and Napier notation
# if the result Hindu-Arabic decimal numbers ia negative then the Napier notaion should be negative

def main():
	response = "Y"
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	while (response == "Y" or response == "y"):
		napierFirst = napierCal(alphabet)
		print("The first number is {}".format(napierFirst))

		napierSecond = napierCal(alphabet)
		print("The second number is {}".format(napierSecond))

		resultAfterOperator = operator(napierFirst, napierSecond)

		resultInNapier = napierResult(resultAfterOperator, alphabet)

		printResponse(resultAfterOperator, resultInNapier)

		response = input("Do you want to repeat the program? Enter y for yes, n for no: ")

# params: the Hindu-Arabic decimal numbers after the arithmetic operator and
# the converted result in Napier notation
# if the Hindu-Arabic decimal number after the arthmetic operator is 0, then print
# the result as 0 and ""
# Else, print the Hindu-Arabic decimal numbers after the arithmetic operator and
# the converted result in Napier notation
def printResponse(resultAfterOperator, resultInNapier):
	if(resultInNapier == ""):
		print("The result is {} or \"\" ".format(resultAfterOperator))
	else:
		print("The result is {} or {}".format(resultAfterOperator, resultInNapier))

# @param: the alphabet string
# Ask the user to input a Napier notation
# checking if the input napier contains only letters in the alphabet
# if not, then ask the user to input napier notation again
# Find the Hindu-Arabic decimal numbers from the Napier's notation
# return the Hindu-Arabic decimal numbers
def napierCal(alphabet):
	napierTotal = 0 # the total for each inputted napier
	napier = input("Enter Napier's number: ").lower()

	# checking if the input napier contains only letters in the alphabet
	# if not, then ask the user to input napier again
	while (not napier.isalpha()):
		print("Something is wrong. Try again")
		napier = input("Enter Napier's number: ")

	# Going through each character of the input napier
	for ch in napier:
		alphaCounter = 0

		# going to through each letter in the alphabet
		for alpha in alphabet:
			output = 2 ** alphaCounter # Calculating the napier value for that letter
			alphaCounter += 1
			# if the napier character inputted and the letter in the alphabet matched,
			# then add the output value to the napier input total
			if(ch == alpha):
				napierTotal += output
	return napierTotal

# @params: two of the Hindu-arabic numbers after converting from the Napier notation
# ask user to input an arithmetic operator include + - * /
# if user enter something else, ask them to re-enter
# if user typed +, then add the total of napier numbers
# if user typed -, then subtract the napier numbers
# if user typed *, then multiple the napier numbers
# if user typed /, then divide the napier numbers
# return the Hindu-Arabic decimal number result after operating the arthmetic
def operator(napierFirst, napierSecond):
	operator = input("Enter the desired arithmetic operator: ")

	while (not(operator == "+" or operator == "-" or operator == "*" or operator == "/")):
	 	print("Something is wrong. Try again")
	 	operator = input("Enter the desired arithmetic operator: ")

	result = 0
	if(operator == "+"):
		result = napierFirst + napierSecond
	elif(operator == "-"):
		result = napierFirst - napierSecond
	elif(operator == "*"):
		result = napierFirst * napierSecond
	else:
		result = napierFirst / napierSecond
	return result

# @params: the alphabet string, and the Hindu-Arabic result after the arithmetic operator
# If the Hindu-Arabic result is negative,
# then the result in napier notaion include the negative
# Find the Napier Notation of the Hindu-Arabic result
# If the result Napier Notation has many z characters.
# if the result need more than 10 z character, then result include
# a single z followed by an asterisk followed by integer represent the number z needed
# if result need less than 10 z character, then result include all the z needed
# return the Napier notation
def napierResult(result, alphabet):
	binaryString = ""

	# this result is negative, then the result in napier notaion include the negative
	if(result < 0):
		resultLettersNapier = "-"
	else:
		resultLettersNapier = ""

	result = abs(result)

	# Stop before z in the alphabet, getting the binary string, which are the remainder to
	# Hindu-Arabic number divide by 2
	for i in range(len(alphabet) - 1): # stop before the z
	 	binaryString = binaryString + str(result % 2)
	 	result = result // 2

	# if the character in the binaryString is 1, then it is the napier notation we need
	count = 0
	for ch in binaryString:
		if(ch == "1"):
			resultLettersNapier += alphabet[count]
		count += 1

	# If the result Napier Notation has many z characters.
	# if the result need more than 10 z character, then result include
	# a single z followed by an asterisk followed by integer represent the number z needed
	# if result need less than 10 z character, then result include all the z needed
	if result > 0 :
		if result <= 10:
			for i in range(result):
				resultLettersNapier  += "z"
		else:
			resultLettersNapier  = "(z*" + str(result) + ")"

	return resultLettersNapier

main()
