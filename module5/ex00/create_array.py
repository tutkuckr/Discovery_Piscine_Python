#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]

print("[", end="")
for index, val in enumerate(array):
	if index == len(array) - 1:
		print(val, end="")
	else:
		print(f"{val}, ", end="")
print("]", end="")