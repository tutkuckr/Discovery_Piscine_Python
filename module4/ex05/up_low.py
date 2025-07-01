#!/usr/bin/env python3

val = input()
result = ""

def convert(char):
	if char.isupper():
		return char.lower()
	else:
		return char.upper()

for char in val:
	result += convert(char)
#print(val.swapcase())
print(result)
