#!/usr/bin/env python3
import sys

counter = 0
if len(sys.argv) != 3:
	print("none")
else:
	if sys.argv[1] >= sys.argv[2]:
		print("none")
	l = list(range(int(sys.argv[1]), int(sys.argv[2]) + 1))
	print(f"{l}")
