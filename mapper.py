#!/usr/bin/env python  
import sys

for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse files
	line = line.split("::")
	if len(line) == 4:
		# parse ratings.dat file
		movie = line[1]
		user = line[0]
		print '%s %s %s' % (user,movie,0)
	else:
		# parse users.dat file
		user = line[0]
		age = line[2]
		print '%s %s %s' % (user,0,age)
