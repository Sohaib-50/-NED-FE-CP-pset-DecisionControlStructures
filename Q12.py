	
'''
#Q12. Write a Python program to input marks (obtained marks as well as maximum marks) for five subjects Physics, 

Chemistry, Biology, Mathematics and Computer. It calculates and prints percentage and grade according to following: None

Percentage >= 90% : Grade A

Percentage >= 80% :  Grade B

Percentage >= 70% : Grade C

Percentage >= 60% : Grade D

Percentage >= 40% : Grade E

Percentage < 40% : Grade F
'''

#Solut
sub_marks = {
"Physics": None,
"Chemistry": None, 
"Biology": None, 
"Mathematics": None, 
"Computer": None
}

for subject in sub_marks.keys():
	print(subject + ":")
	sub_marks[subject] = float(input("enter marks obtained: ")), float(input("enter total obtainable marks: "))
	print()

total_obtained, total_obtainable = 0, 0
for obtained, obtainable in sub_marks.values():
	total_obtained += obtained
	total_obtainable += obtainable

percentage = (total_obtained/total_obtainable) * 100
	
print(f"\nPercentage: {round(percentage, 2)}%")
print(f"Grade: ", end = "")
if  0< percentage > 100:
	print("Invalid input.")
else:
	if percentage >= 90:
		print("A")
	elif percentage >= 80:
		print("B")
	elif percentage >= 70:
		print("C")
	elif percentage >= 60:
		print("D")
	elif percentage >= 40:
		print("E")
	else:
		print("F")
