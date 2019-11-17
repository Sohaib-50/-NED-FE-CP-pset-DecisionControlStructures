#Q7. Write a Python program to check if a character entered by the user is an alphabet or a digit or a special character. If the user enters more than one character as input, the program prints some appropriate error message and exit.

#solution1:
ch = input("Enter a single character: ")
if len(ch) == 1:
	if "A" <= ch <= "Z" or "a" <= ch <= "z":
		print("alphabet.")
	elif "0" <= ch <= "9":
		print("digit.")
	else:
		print("special character.")
else:
	print("you were supposed to enter one character only!")

#solution2:
ch = input("Enter a single character: ")
if len(ch) == 1:
	if ch.isalpha():
		print("alphabet.")
	elif ch.isdigit():
		print("digit.")
	else: #must be a special character if not a digit and not an alphabet.
		print("special character.")
else:
	print("you were supposed to enter one character only!")
