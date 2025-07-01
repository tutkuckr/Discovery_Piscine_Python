#!/usr/bin/env python3
import sys

class Helper:
	def shrink(self, string):
		print(string[:8])
	def enlarge(self, string):
		while len(string) < 8:
			string +='Z'
		print(string)

c = Helper()
if len(sys.argv) == 1:
	print("none")
else:
	for var in sys.argv[1:]:
		if len(var) > 8:
			c.shrink(var)
		elif len(var) < 8:
			c.enlarge(var)
		else:
			print(var)
