#! /usr/bin/env python
import sys

# This mapper code will input a line of text and output <word, 1>

for line in sys.stdin:
	line = line.strip()
	keys = line.split()
	for key in keys:
		value = 1
		print('{0}\t{1}'.format(key, value))

