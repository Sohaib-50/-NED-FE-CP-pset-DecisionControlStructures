#Q1. Write a Python program that requests an integer value from the user. If the value is between 1 and 100 inclusive, print "OK"; otherwise, do not print anything.

#solutuon:
if int(input("Enter integer value: ")) in range(1, 101):
    print("OK")
