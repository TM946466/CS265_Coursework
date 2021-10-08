#!/usr/bin/env python3
import sys

F = sys.argv[1] #Get command line agrument
F = open(F, "r") #open file
line = F.readline()
idDict = {} #Initialize dictionary
while line : #While there are lines
	line = line.strip( '\t\n' ) #Strip tabs and new lines
	count = 0
	idName = ""
	for x in line.split() :
		if count > 0:
			idName = idName + x 
		else:
			idNum = int(x)
		count += 1

	idDict[idNum] = idName #Assign names to id number
	line = F.readline()


for i in sorted(idDict):
	print(i," ",idDict[i]) #Print sorted dictionarty sorted by idNumber
F.close() #Close file
	

