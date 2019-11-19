'''
#Q14. Write a Python program to input electricity units consumed. The program calculates and prints total electricity bill 

according to the following condition. 

For first 50 units Rs. 0.50/unit.

For next 100 units Rs. 0.75/unit.

For next 100 units Rs. 1.20/unit.

For unit above 250 Rs. 1.50/unit.
'''

#Solution0:
units = int(input("enter units consumed: "))
bill = 0

while units > 250:
	bill += 1.50
	units -=1
while units > 150:
	bill += 1.20
	units -= 1
while units > 50:
	bill += 0.75
	units -= 1
while units:
	bill += 0.5
	units -= 1
print(bill)

#Solution1:
units = int(input("enter units consumed: "))
units_rem = units
bill = 0

if units_rem >=50:
	bill += 50 * 0.5
	units_rem -= 50
	if units_rem >= 100:
		bill += 100 * 0.75
		units_rem -= 100
		if units_rem >= 100:
			bill += 100 * 1.20
			units_rem -= 100
			if units_rem:
				bill += units_rem * 1.50
				units -= units
		else:
			bill += units_rem * 1.20
	else:
		bill += units_rem * 0.75
		
else:
	bill += units * 0.5
	
		
print(bill)
