#! /usr/bin/env python
import sys

# This reducer code will input a line of text and output <word, total-count>

last_key = None
running_total = 0

for line in sys.stdin:
	line = line.strip()
	this_key, value = line.split('\t', 1)
	value = int(value)

	if this_key == last_key:
		running_total += value
	else:
		if last_key:
			print('{0}\t{1}'.format(last_key, running_total))
		running_total = value
		last_key = this_key

if last_key == this_key:
	print('{0}\t{1}'.format(last_key, running_total))
