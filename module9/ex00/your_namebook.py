#!/usr/bin/env python3
import sys
import numpy as np

class Helper:
	def array_of_names(self, persons):
		result = []
		for key, value in persons.items():
			name = key.capitalize()
			last_name = value.capitalize()
			result.append(name + " " + last_name)
		return result

c = Helper()
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(c.array_of_names(persons))