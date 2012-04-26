#!/usr/bin/env python
# tableFormat.py
"""
This script will format the data from an input file and mess around with it;
"""
import sys
from itertools import * #this is for the "islice" function

if __name__ == '__main__':
	if (len(sys.argv) > 1): #check if there are arguments present
		infilename = sys.argv[1]
		infile = open(infilename, 'r') # open file for reading

		matrix = [] #list of lists - a variable which contains all the lists
		maxList = 0 #variable to hold which list is the largets
		
		lines = infile.readlines() # read the file into a list of lines:

		for line in lines:			
			line = line.strip() #This removes the end-of-the-line symbol > \n
			currentList = list(line[::2])
			#matrix.append(list(islice(line, 0, None, 2))) #another way to slice the list space by space
			matrix.append(currentList)	#adding list to list of lists
			#print '|{0} |'.format(' | '.join(currentList)) #one of the alternative ways
			print '+---'*len(currentList) + '+'
			print '| ' + ' | '.join(currentList) + ' |'
		print '+---'*len(currentList) + '+' #currentList scope can be seen outside for - bad practice in general
		infile.close()
		#maxList = max(matrix, key=len) #fnd ouut which list of chracters was the longest		
		#print maxList
			
	else:
		print "You did not specify the file correctly."


