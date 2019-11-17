'''
#10. Write a Python program that 
requests five integer values from 
the user. It then prints one of two 
things: if any of the values entered 
are duplicates, it prints 
"DUPLICATES"; otherwise, it prints 
"ALL UNIQUE".
'''

#Solution0:
n1 = int(input("enter 1st number: "))
n2 = int(input("enter 2nd number: "))
n3 = int(input("enter 3rd number: "))
n4 = int(input("enter 4th number: "))
n5 = int(input("enter 5th number: "))

if n1 == n2 or n1 == n3 or n1 == n4 \
or n1 == n5 or n2 == n3 or n2 == n4\
or n2 == n5 or n3 == n4 or n3 == n5 \
or n4 == n5:
	print("DUPLICATES")
else:
	print("ALL UNIQUE")


#Solution1:
nums = [int(input(f"enter n{i+1}: ")) for i in range(5)]
duplicates = False
for i in range(5):
	if nums[i] in nums[:i] or nums[i] in nums[i+1:]:
		duplicates = True
		break
if duplicates:
	print("DUPLICATES")
else:
	print("ALL UNIQUE.")

 
Ppp
#Solution2:
nums = [int(input(f"enter n{i+1}: ")) for i in range(5)]

if len(nums) == len(set(nums)):
	print("ALL UNIQUE.")
else:
	print("duplicates")
