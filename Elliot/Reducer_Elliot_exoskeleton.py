#!/usr/bin/python

import sys
import time
import numpy as np

# first three elements of list name are the past block and last two digits represent i and j of future block.

# Block C00:
B0000 = []
A0100 = []
B1000 = []
A0000 = []

# Block C01
A0001 = []
B0101 = []
A0101 = []
B1101 = []

# Block C10
A1010 = []
B0010 = []
A1110 = []
B1010 = []

# Block C11
A1011 = []
B0111 = []
A1111 = []
B1111 = []

for line in sys.stdin :
	ls = line.rstrip().split('\t')
	future_block = str(ls[0])
	past_block = str(ls[1])
	provenance = str(ls[2])
	value = float(ls[3])
	provenance_details = provenance.split(',')
	provenance_matrix = provenance_details[0]
	i = str(provenance_details[1])
	j = str(provenance_details[2])


	if future_block == "C00" :
		if past_block == "A00" : 
			A0000.append(value)
		elif past_block == "B00" :
			B0000.append(value)
		elif past_block == "A01" :
			A0100.append(value)
		else :
			B1000.append(value)




	if future_block == "C01" :
		if past_block == "A00" : 
			A0001.append(value)
		elif past_block == "B01" :
			B0101.append(value)
		elif past_block == "A01" :
			A0101.append(value)
		else :
			B1101.append(value)




	if future_block == "C10" :
		if past_block == "A10" : 
			A1010.append(value)
		elif past_block == "B00" :
			B0010.append(value)
		elif past_block == "A11" :
			A1110.append(value)
		else :
			B1010.append(value)




	if future_block == "C11" :
		if past_block == "A10" : 
			A1011.append(value)
		elif past_block == "B01" :
			B0111.append(value)
		elif past_block == "A11" :
			A1111.append(value)
		else :
			B1111.append(value)
print(A0000)
print(B0000)
print(A0100)
print(B1000)
print(A0001)
print(B0101)
print(A0101)
print(B1101)
print(A1010)
print(B0010)
print(A1110)
print(B1010)
print(A1011)
print(B0111)
print(A1111)
print(B1111)

#C00 = np.array(A0000)*np.array(B0000) + np.array(A0100)*np.array(B1000)
#C00 = np.dot(A0000,B0000) + np.dot(A0100,B1000)
print(np.dot(A0000,B0000))
print(np.dot(A0100,B1000))
#C01 = np.array(A0001)*np.array(B0101) + np.array(A0101)*np.array(B1101)
#C01 = np.dot(A0001,B0101) + np.dot(A0101,B1101)
print(np.dot(A0001,B0101))
print(np.dot(A0101,B1101))
#C10 = np.array(A1010)*np.array(B0010) + np.array(A1110)*np.array(B1010)
#C10 = np.dot(A1010,B0010) + np.dot(A1110,B1010)
print(np.dot(A1010,B0010))
print(np.dot(A1110,B1010))
#C11 = np.array(A1011)*np.array(B0111) + np.array(A1111)*np.array(B1111)
#C11 = np.dot(A1011,B0111) + np.dot(A1111,B1111)
print(np.dot(A1011,B0111))
print(np.dot(A1111,B1111))
#print(C00)
#print(C01)
#print(C10)
#print(C11)
