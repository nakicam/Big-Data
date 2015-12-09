#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# This mapper code will input a <date word, value>  or <word, value> input file,
# and move date into the value field for output
# --------------------------------------------------------------------------

for line in sys.stdin:
	key, value = line.strip().split(',')
	tokens = key.split()
	if len(tokens) >= 2:
		date = tokens[0]
		key = tokens[1]
		value = date + " " + value
		print("%s\t%s" % (key, value))
	else:
		print("%s\t%s" % (key, value))

