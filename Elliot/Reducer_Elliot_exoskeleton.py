#!/usr/bin/python

import sys
import time
import numpy as np

# The First three elements of a list name represent the past block and last two digits represent i and j of future block. (eg: A0100 means that the cells in this list come from A01 - the upper right block of A - and we will use this list in the computation of C00). 

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
	
	# Eliminate leading and trailing white spaces

	ls = line.rstrip().split('\t')

	# We now split the information into the various chunks that were described earlier in the mapper

	future_block = str(ls[0])
	past_block = str(ls[1])
	provenance = str(ls[2])
	value = float(ls[3])
	provenance_details = provenance.split(',')
	provenance_matrix = provenance_details[0]
	i = str(provenance_details[1])
	j = str(provenance_details[2])


# We now split the information to create the lists that will be used to compute the blocks of C. In the chunk below, we are determining how we will compute C00, which depends on 4 blocks from the original matrices : A00, B00, A01 and B10. We repeat this process for each of the four blocks of C

	if future_block == "C00" :
		if past_block == "A00" : 
			A0000.append(value)
		elif past_block == "B00" :
			B0000.append(value)
		elif past_block == "A01" :
			A0100.append(value)
		else :
			B1000.append(value)





	elif future_block == "C01" :
		if past_block == "A00" : 
			A0001.append(value)
		elif past_block == "B01" :
			B0101.append(value)
		elif past_block == "A01" :
			A0101.append(value)
		else :
			B1101.append(value)




	elif future_block == "C10" :
		if past_block == "A10" : 
			A1010.append(value)
		elif past_block == "B00" :
			B0010.append(value)
		elif past_block == "A11" :
			A1110.append(value)
		else :
			B1010.append(value)




	else :
		if past_block == "A10" : 
			A1011.append(value)
		elif past_block == "B01" :
			B0111.append(value)
		elif past_block == "A11" :
			A1111.append(value)
		else :
			B1111.append(value)

print(len(A0000))
print(len(B0000))
print(len(A0100))
print(len(B1000))
print(len(A0001))
print(len(B0101))
print(len(A0101))
print(len(B1101))
print(len(A1010))
print(len(B0010))
print(len(A1110))
print(len(B1010))
print(len(A1011))
print(len(B0111))
print(len(A1111))
print(len(B1111))

# We now multiply the lists to obtain our 4 lists of values for the four blocks of C

#C00 = np.array(A0000)*np.array(B0000) + np.array(A0100)*np.array(B1000)
#C00 = np.dot(A0000,B0000) + np.dot(A0100,B1000)
#print(np.dot(A0000,B0000))
#print(np.dot(A0100,B1000))
#C01 = np.array(A0001)*np.array(B0101) + np.array(A0101)*np.array(B1101)
#C01 = np.dot(A0001,B0101) + np.dot(A0101,B1101)
#print(np.dot(A0001,B0101))
#print(np.dot(A0101,B1101))
#C10 = np.array(A1010)*np.array(B0010) + np.array(A1110)*np.array(B1010)
#C10 = np.dot(A1010,B0010) + np.dot(A1110,B1010)
#print(np.dot(A1010,B0010))
#print(np.dot(A1110,B1010))
#C11 = np.array(A1011)*np.array(B0111) + np.array(A1111)*np.array(B1111)
#C11 = np.dot(A1011,B0111) + np.dot(A1111,B1111)
#print(np.dot(A1011,B0111))
#print(np.dot(A1111,B1111))
#print(C00)
#print(C01)
#print(C10)
#print(C11)
