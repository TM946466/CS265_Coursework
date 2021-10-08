#!/usr/bin/env python3
import sys
try:				#Tries to get command line argument
	F = sys.argv[1]
	F = open(F, "r")
except IndexError: 		#If no argument given defaults to default file
	F = sys.stdin
	F = open("ids", "r")
line = F.readline()
idDict = {} #Initialize dictionary
while line :
	line = line.strip( '\t\n' ) #Remove tabs and new lines
	count = 0
	idName = ""
	for x in line.split() :
		if count > 0:
			idName = idName + x
		else:
			idNum = int(x)
		count += 1

	idDict[idNum] = idName #Assign names to corosponding Id Number
	line = F.readline()

for i in sorted(idDict):
	print(i," ",idDict[i]) #Prints sorted dictionary
F.close() #Close file
	

