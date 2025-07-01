#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
	print("none")
else:
	esc_substr = re.escape(sys.argv[1])
	all_finds = re.findall(esc_substr, sys.argv[2])
	if len(all_finds) == 0:
		print("none")
	else:
		print(len(all_finds))

#• The first parameter is a keyword to search for in a string.
#• The second parameter is the string to be searched.
#• When executed, the program should display 
# the number of times the keyword appears in the string.
#• If the number of parameters is different from 2 or 
# if the first string does not appear
#in the second, it should display none followed by a newline