#!/usr/bin/env python3
import sys
import numpy as np

def collect_names(dict):
	if dict[1] == "red":
		return True
	else:
		return False

class Helper:
	def find_the_redheads(self, dupont_family):
		result = filter(collect_names, dupont_family.items())
		reds = [name for name, color in result]
		return reds

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
c = Helper()
print(c.find_the_redheads(dupont_family))