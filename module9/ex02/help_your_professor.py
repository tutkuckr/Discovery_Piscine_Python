#!/usr/bin/env python3
import sys
import numpy as np

class Helper:
	def average(self, class_list):
		avg = 0
		for name, score in class_list.items():
			avg += score
		return avg / len(class_list)
	
class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}

class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

c = Helper()
print(f"Average for class 3B: {c.average(class_3B)}.")
print((f"Average for class 3B: {c.average(class_3C)}."))