#!/usr/bin/env python3
import sys

args = sys.argv
length = len(args)
if length < 3:
	print("none")
else:
	while length > 1:
		print(args[length - 1])
		length -= 1 
		
