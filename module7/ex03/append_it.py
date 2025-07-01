#!/usr/bin/env python3
import sys

counter = 0
if len(sys.argv) == 1:
	print("none")
else:
	for val in sys.argv[1:]:
		if val[-3:] != "ism":
			print(f"{val}ism")
		
