#!/usr/bin/env python3

num1 = input("Enter the first number:\n")
num2 = input("Enter the second number:\n")
result = (int(num1) * int(num2))

print(num1 + " x " + num2 + " = " + str(result))
if result < 0:
	print("The result is negative.")
elif result > 0:
	print("The result is positive.")
else:
	print("The result is positive and negative.")