#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
	print("none")
else:
	param = sys.argv[1:]
	print(f"parameters: {len(param)}")
	for i in param:
		print(f"{i}: {len(i)}")