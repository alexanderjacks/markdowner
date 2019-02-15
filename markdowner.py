#!/usr/bin/env python

# ready to open CSV
filename = "heroes.csv"

# opens CSV data as list of lists
with open(filename) as fn:
	raw_content = fn.readlines()
	# learns number of records in CSV data
	record_total = len(raw_content)
	# removes carriagereturn chars leaves only newlines to mark lines
	cleaner_content = [x.split('\r') for x in raw_content]

# readies to print list items from front to back (negative index asending)
z = (record_total*-1)
while z < 0:
	# lists each line in data
	line_of_content = cleaner_content[z]
	# juggling data types: needs refactoring
	ara = []
	ara.append(line_of_content[0].split(','))
	# back down to 1-level array with all members strings
	print(ara[0])
	# this loop iterates negative index asending; climbs to 0 from -len()
	z += 1
	# goal now is to print each list member in sequence, with needed markdown


