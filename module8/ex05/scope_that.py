#!/usr/bin/env python3
import sys

class Helper:
	def add_one(self, par):
		par += 1

c = Helper()
par = 42
print(par)
c.add_one(par)
print(par)