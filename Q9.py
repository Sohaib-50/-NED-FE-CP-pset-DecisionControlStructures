'''
#Q9. Write a Python program that 
requests five integer values from
the user. It then prints the 
maximum and minimum values entered.
If the user enters the values 3, 2,
5, 0, and 1, the program would
indicate that 5 is the maximum and 
0 is the minimum. Your program should 
handle ties properly; for example, 
if the user enters 2, 4, 2, 3, and 3,
the program should report 2 as the 
minimum and 4 as maximum.
'''


#Solution0:
n1 = int(input("enter 1st number: "))
n2 = int(input("enter 2nd number: "))
n3 = int(input("enter 3rd number: "))
n4 = int(input("enter 4th number: "))
n5 = int(input("enter 5th number: "))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
	max = n1
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
	max = n2
elif n3 > n1 and n3 > n2 and n3 > 4 and n3 > n5:
	max = n3
elif n4 > n1 and n4 > n2 and n4 >  n3 and n4 > n5:
	max = n4
else:
	max = n5
	
if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
	min = n1
elif  n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
	min = n2
elif n3 <= n1 and n3 <= n2 and n3 <= 4 and n3 <= n5:
	min = n3
elif n4 <= n1 and n4 <= n2 and n4 <=  n3 and n4 <= n5:
	min = n4
else:
	min = n5
print()	
print(f"max = {max}")
print(f"min = {min}")


#Solution1:

nums = [int(input(f"Enter n{i+1}: ")) for i  in range(5)]
max, min = nums[0], nums[0]
for i in range(5):
	if nums[i] > max:
		max = nums[i]
	if  nums[i] < min:
		min = nums[i]
print()	
print(f"max = {max}")
print(f"min = {min}")

