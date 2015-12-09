#!/usr/bin/env python
import sys

previous_channel = None
previous_show = None
CHANNELS = {}
SHOWS = {}

for line in sys.stdin:
	key, value = line.strip().split('\t')
	if value.isdigit():
		current_show = key
		current_count = int(value)
		if current_show == previous_show:
			SHOWS[current_show] += current_count
		else:
			SHOWS[current_show] = current_count
			previous_show = current_show
	else:
		current_channel = key
		current_show = value
		if current_channel == previous_channel:
			CHANNELS[current_channel].append(current_show)		
		else:
			CHANNELS[current_channel] = [current_show]
			previous_channel = current_channel

query = "ABC"
for show in CHANNELS[query]:
	count = SHOWS[show]
	print('{0}\t{1}'.format(show, count))

