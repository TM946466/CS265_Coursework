#!/usr/bin/env python3
import sys

F = sys.stdin
F = open("students", "r") #opens file names "students" in read only
line = F.readline() #read lines of the file
while line:
	line = line.strip( '\t\n' ) #strip lines of tabs and new lines
	cont = 0 #counter 
	tot = 0 #Total variable
	for x in line.split() : 
		if cont > 0:
			tot += int(x) #checks to see if view is past position 0 and adds the subsequent scores together
		else:
			name = x #Assigns first position to name variable 
		cont += 1
	avge = tot / (cont - 1) #Calculate average
	print(name, " " , avge)
	line = F.readline() #Reads next line

F.close() #Closes file
		

