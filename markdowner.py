#!/usr/bin/env python

# lib to allow print() to target an output file
import sys

# ready to open CSV
filename = "heroes.csv"

# opens CSV data as list of lists
with open(filename) as fn:
	raw_content = fn.readlines()
	# learns number of records in CSV data, offsets (why by 2? CSV header is 1 extra line)
	records_total = len(raw_content) - 2
	# removes carriagereturn chars leaves only newlines to mark lines
	cleaner_content = [x.split('\r') for x in raw_content]

# readies to print list items from first to last
z = 0
while z < records_total:
	# lists each line in data
	line_of_content = cleaner_content[z]
	# juggling data types: could use refactoring
	hero_content = []
	hero_content.append(line_of_content[0].split(','))
	
	# # # BEGIN PRINTING .md FILE # # #
	# map fields to vars
	title = hero_content[0][0]
	description = hero_content[0][1]
	tag1 = hero_content[0][2]
	tag2 = hero_content[0][3]
	tag3 = hero_content[0][4]
	tag4 = hero_content[0][5]
	ally1 = hero_content[0][6]
	ally2 = hero_content[0][7]
	ally3 = hero_content[0][8]

	# create markdown file for list
	sys.stdout = open(f'./mds/{title}.md','wt')

	# to print the static md
	print("---")
	print("templateKey: 'blog-post'")
	
	# to print the title field
	print(f"title: {title}")
	
	# to print the description field
	print(f"description: {description}")

	# to print the tags
	print("tags:")
	print(f"  -  {tag1}")
	print(f"  -  {tag2}")
	print(f"  -  {tag3}")
	# conditional ctrl for final value that's not always there;
	try:
		if tag4:
			print(f"  -  {tag4}")
	except:
		break

	# to print the allies
	print("allies:")
	print(f"  -  {ally1}")
	print(f"  -  {ally2}")
	print(f"  -  {ally3}")

	# to print the image location
	print("---")
	print(f"![{title}](/img/{title}.png)")

	# # # END PRINTING .md FILE # # #

	# goal now is to write~print each list member to a file w file name item[0]

	# this loop climbs to len()-2 from 0
	z += 1
	

# unbreak python! fix core cmd back to default
sys.stdout = sys.__stdout__

