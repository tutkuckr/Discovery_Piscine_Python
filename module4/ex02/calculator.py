#!/usr/bin/env python3

first_num = int(input("Give me the first number: "))
second_num = int(input("Give me the second number: "))

print("Thank you!")
print(f"{first_num} + {second_num} = {first_num + second_num}")
print(f"{first_num} - {second_num} = {first_num - second_num}")
if second_num != 0:
	print(f"{first_num} / {second_num} = {int(first_num / second_num)}")
else:
	print("Cannot divide a number to 0")
print(f"{first_num} * {second_num} = {first_num * second_num}")