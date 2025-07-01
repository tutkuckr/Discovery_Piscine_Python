#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
	print("none")
else:
	if len(re.findall(sys.argv[1], sys.argv[2])) == 0:
		print("none")
	else:
		print(len(re.findall(sys.argv[1], sys.argv[2])))

#• The first parameter is a keyword to search for in a string.
#• The second parameter is the string to be searched.
#• When executed, the program should display 
# the number of times the keyword appears in the string.
#• If the number of parameters is different from 2 or 
# if the first string does not appear
#in the second, it should display none followed by a newline