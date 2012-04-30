#!/usr/bin/python
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

		#list of lists - a variable which contains all the lists
		listOfLists = [] 

		# read the file into a list of lines:
		lines = infile.readlines() 
		
		#initialize a var which will gold the longes line
		longestLine = 0

		for line in lines:			
			currentList = list(line[::2])

			if (len(currentList) > longestLine):
				longestLine = len(currentList)

			listOfLists.append(currentList) #adding list to list of lists
		infile.close()

		#count number of lines
		numberOfLines = len(listOfLists);

		# initalize an empty matrix of spaces
		matrix = [[' ' for i in range((longestLine*4)+1)] for j in range((2*numberOfLines)+1)]

		for i in range(numberOfLines):
			for j in range(len(listOfLists[i])):
				if (listOfLists[i][j] != ' '):
					matrix[2*i][4*j]='+'
					matrix[2*i][(4*j)+1]='-'
					matrix[2*i][(4*j)+2]='-'
					matrix[2*i][(4*j)+3]='-'
					matrix[2*i][(4*j)+4]='+'
					matrix[(2*i)+1][4*j]='|'
					matrix[(2*i)+1][(4*j)+2]=listOfLists[i][j]
					matrix[(2*i)+1][(4*j)+4]='|'
					matrix[(2*i)+2][4*j]='+'
					matrix[(2*i)+2][(4*j)+1]='-'
					matrix[(2*i)+2][(4*j)+2]='-'
					matrix[(2*i)+2][(4*j)+3]='-'
					matrix[(2*i)+2][(4*j)+4]='+'
		s = ''
		for i in range((2*numberOfLines)+1):
			for j in range((longestLine*4)+1):
				 s+=(matrix[i][j])				
			print s
			s=''			
	else:
		print "You did not specify the file correctly."


