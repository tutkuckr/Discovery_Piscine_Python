#!/usr/bin/env python3
import sys

counter = 0
if len(sys.argv) != 2:
	print("none")
else:
	for i in sys.argv[1]:
		if i == "z":
			print("z",end="")
			counter += 1
	if counter == 0:
		print("none")
	else:
		print("")