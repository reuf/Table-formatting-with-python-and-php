<<<<<<< HEAD
#!/usr/bin/python
=======
#!/usr/bin/env python
>>>>>>> eaa8bd3b61ddc5b7bc88458e5d45fbc388ff7100
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

<<<<<<< HEAD
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
=======
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
			
>>>>>>> eaa8bd3b61ddc5b7bc88458e5d45fbc388ff7100
	else:
		print "You did not specify the file correctly."


