#!/usr/bin/env python3
import sys

class Helper:
	def greetings(self, name = "noble stranger"):
		#if type(name) != str:
		if not isinstance(name, str):
			print("Error! It was not a name.")
		else:
			print(f"Hello, {name}")

c = Helper()
c.greetings('Alexandra')
c.greetings('Wil')
c.greetings()
c.greetings(42)