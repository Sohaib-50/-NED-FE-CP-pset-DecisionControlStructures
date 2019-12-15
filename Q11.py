#Q11. Write a Python program to check whether the triangle is equilateral, isosceles or scalene triangle. In equilateral triangle all three sides are equal, in isosceles triangle any two sides are equal, and in scalene triangle none of the three are equal.
s1 = int(input("enter 1st side: "))
s2 = int(input("enter 2nd side: "))
s3 = int(input("enter 3rd side: "))

if s1 == s2 == s3:
	print("EQUILATERAL")
elif s1 != s2 != s3:
	print("SCALENE")
else:
	print("ISOSCELES")
