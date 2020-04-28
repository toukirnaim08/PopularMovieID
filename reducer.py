#!/usr/bin/env python
import sys
 
counts = {}	#dictionary for all age groups

counts1 = {}	#dictionary for age group 1(under 18)
counts18 = {}	#dictionary for age group 18(18-24)
counts25 = {}	#dictionary for age group 25(25-34)
counts35 = {}	#dictionary for age group 35(35-44)
counts45 = {}	#dictionary for age group 45(45-49)
counts50 = {}	#dictionary for age group 50(50-55)
counts56 = {}	#dictionary for age group 56(56+)

index = ""
 
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
 
	# parse the input we got from mapper.py
	user, movie, age = line.split()
	if movie == "0":
		index = age
	else:
		if index == "56":
			#setting movieIDs as keys of counts56 dictionary 
			#counting number of movies for age group 56
			try:
				counts56[movie] = counts56[movie] + 1
			except:
				counts56[movie] = 1
			
			#setting age group as a key of counts dictionary 			
			#setting counts56 dictionary as a value
			counts[index] = counts56

		elif index == "50":
			#setting movieIDs as keys of counts50 dictionary 
			#counting number of movies for age group 50
			try:
				counts50[movie] = counts50[movie] + 1
			except:
				counts50[movie] = 1

			#setting age group as a key of counts dictionary 			
			#setting counts50 dictionary as a value
			counts[index] = counts50

		elif index == "45":
			#setting movieIDs as keys of counts45 dictionary 
			#counting number of movies for age group 45
			try:
				counts45[movie] = counts45[movie] + 1
			except:
				counts45[movie] = 1
			
			#setting age group as a key of counts dictionary 			
			#setting counts45 dictionary as a value
			counts[index] = counts45

		elif index == "35":
			#setting movieIDs as keys of counts35 dictionary 
			#counting number of movies for age group 35
			try:
				counts35[movie] = counts35[movie] + 1
			except:
				counts35[movie] = 1

			#setting age group as a key of counts dictionary 			
			#setting counts35 dictionary as a value
			counts[index] = counts35

		elif index == "25":
			#setting movieIDs as keys of counts25 dictionary 
			#counting number of movies for age group 25
			try:
				counts25[movie] = counts25[movie] + 1
			except:
				counts25[movie] = 1

			#setting age group as a key of counts dictionary 			
			#setting counts25 dictionary as a value
			counts[index] = counts25
		
		elif index == "18":
			#setting movieIDs as keys of counts18 dictionary 
			#counting number of movies for age group 18
			try:
				counts18[movie] = counts18[movie] + 1
			except:
				counts18[movie] = 1

			#setting age group as a key of counts dictionary 			
			#setting counts18 dictionary as a value
			counts[index] = counts18

		elif index == "1":
			#setting movieIDs as keys of counts1 dictionary 
			#counting number of movies for age group 1
			try:
				counts1[movie] = counts1[movie] + 1
			except:
				counts1[movie] = 1

			#setting age group as a key of counts dictionary 			
			#setting counts1 dictionary as a value
			counts[index] = counts1

#for index in counts.keys():
#    print ("%s\t%s" % (index, counts[index]))

for index in counts.keys():
	if index == "56":
		#key of maximum value 
		movieWithMaxCount = (list(counts56.keys())[list(counts56.values()).index(max(counts56.values()))])
		print ("%s\t%s" % (index, movieWithMaxCount))

	elif index == "50":
		#key of maximum value 
		movieWithMaxCount = (list(counts50.keys())[list(counts50.values()).index(max(counts50.values()))])
		print ("%s\t%s" % (index, movieWithMaxCount))

	elif index == "45":
		#key of maximum value 
		movieWithMaxCount = (list(counts45.keys())[list(counts45.values()).index(max(counts45.values()))])
		print ("%s\t%s" % (index, movieWithMaxCount))

	elif index == "35":
		#key of maximum value 
		movieWithMaxCount = (list(counts35.keys())[list(counts35.values()).index(max(counts35.values()))])
		print ("%s\t%s" % (index, movieWithMaxCount))

	elif index == "25":
		#key of maximum value 
		movieWithMaxCount = (list(counts25.keys())[list(counts25.values()).index(max(counts25.values()))])
		print ("%s\t%s" % (index, movieWithMaxCount))

	elif index == "18":
		#key of maximum value 
		movieWithMaxCount = (list(counts18.keys())[list(counts18.values()).index(max(counts18.values()))])
		print ("%s\t%s" % (index, movieWithMaxCount))

	elif index == "1":
		#key of maximum value 
		movieWithMaxCount = (list(counts1.keys())[list(counts1.values()).index(max(counts1.values()))])
		print ("%s\t%s" % (index, movieWithMaxCount))
