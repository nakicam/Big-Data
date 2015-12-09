#!/usr/bin/env python
import sys
for line in sys.stdin:
	key, value = line.strip().split(',')
	if value.isdigit():
		print('%s\t%s' % (key, value))
	else:
		print('%s\t%s' % (value, key))
	
	
	
	


