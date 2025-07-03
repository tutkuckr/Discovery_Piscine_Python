#!/usr/bin/env python3
import sys
import numpy as np

def sort_dic(item):
	return item[1]

class Helper:
	def famous_births(self, women_scientists):
		sorted_people = sorted(women_scientists.values(), key=lambda item:int(item['date_of_birth']))
		for people in sorted_people:
			print(f"{people['name']} is a great scientist born in {people['date_of_birth']}")
	
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

c = Helper()
c.famous_births(women_scientists)
