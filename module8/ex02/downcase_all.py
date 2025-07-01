#!/usr/bin/env python3
import sys

class Helper:
	def downcase_it(self, str):
		return str.lower()

if len(sys.argv) == 1:
	print("none")
else:
	c = Helper()
	#for i in range(1, len(sys.argv)):
	#	print(c.downcase_it(sys.argv[i]))
	for i in sys.argv[1:]:
		print(c.downcase_it(i))
