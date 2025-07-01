#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
	print("none")
else:
	param = input("What was the parameter? ")
	if sys.argv[1] == param:
		print("Good job!")
	else:
		print("Nope, sorry...")