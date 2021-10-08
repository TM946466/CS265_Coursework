#!/usr/bin/env python3
import sys

F = sys.stdin
F = open("students.csv", "r") #open file
line = F.readline()
while line:
	line = line.strip( '\t\n' )#remove tabs and new lines
	cont = 0
	tot = 0
	for x in line.split(",") :#Split by comma
		if cont > 0:
			tot += int(x) #Add to total if after name place
		else:
			name = x #Holds onto name
		cont += 1
	avge = tot / (cont - 1)#Calculates average
	print(name, " " , avge)
	line = F.readline() #Reads next line

F.close() #closes file		
