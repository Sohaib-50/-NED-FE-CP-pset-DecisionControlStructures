'''
#Q13. Write a Python program to input basic salary of an employee. It calculates and prints the gross and net salary 

according to following rules.

Gross Salary = Basic Salary (BS) + House Rent Allowance (HRA) + Dearness Allowance (DA) 

Net Salary = Gross Salary (GS) – Deductions (DD) 

BS <= 10000 : HRA = 20%, DA = 80%

BS <= 20000 : HRA = 25%, DA = 90%

BS > 20000 : HRA = 30%, DA = 95%

DD = 10% of BS
'''

#Solution:
bs = float(input("enter basic salary: "))
if bs <= 10000:
	gs = bs + (0.2*bs) + (0.8*bs)
elif bs <= 20000:
	gs = bs + (0.25*bs) + (0.9*bs)
else:
	gs = bs + (0.3*bs) +(0.95*bs)
print(f"Gross salary = {gs}\nNet Salary = {gs - (0.1*bs)}")
