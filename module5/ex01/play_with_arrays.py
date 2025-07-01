#!/usr/bin/env python3

org_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
for index, val in enumerate(org_arr):
	new_arr.append(val + 2)
print(f"Original array: {org_arr}\nNew array: {new_arr}")