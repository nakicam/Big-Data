#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# This reducer code will input a <word, "total count"> or
# <word, date "daily count"> input file and join words together.
#
# Note, the input will come as grouped by words and as it is read in
# --------------------------------------------------------------------------

previous_word = None
dates = []			# list to hold dates for a given word
daily_counts = []	# list of day counts for a given word

for line in sys.stdin:
	key, value = line.strip().split('\t')
	if key != previous_word:
		for i in range(len(dates)):
			print('%s %s %s %s' % (dates[i], previous_word, daily_counts[i], total_count))
		# Reset the following on a new word
		dates = []
		daily_counts = []
		previous_word = key
	if (value[0:3] in ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec']):
		day, count = value.split()
		dates.append(day)
		daily_counts.append(count)
	else:
		total_count = value
for i in range(len(dates)):
	print('%s %s %s %s' % (dates[i], previous_word, daily_counts[i], total_count))

