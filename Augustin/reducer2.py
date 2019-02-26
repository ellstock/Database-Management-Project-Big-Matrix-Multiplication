#!/usr/bin/env python

import sys
import numpy as np

# We assume we know the size of the two matrices to be multiplied

length = int(2)
width = int(2)

# Generate lists to store the values of the original Matrices to multiply

A_list = [0]*(length*width) 
B_list = [0]*(length*width)


for line in sys.stdin:

	temp = max(length,width) # what's the point of this? Couldn't we just include this in the next line? 

	for i in range(0,temp):

		# Get rid of trailing white spaces and split the elements in the line into the key (matrix origin + row or column number depending on origin), column or row number (opposite of that in the 			# key - col_or_row) and the cell value

		key, col_or_row, value = line.rstrip().split("\t")

		# Transform into integers

		col_or_row, value = map(int,[col_or_row,value])

		# Create two lists of values for the two original Matrices. For A it is ordered by row and for B it is ordered by column so that we can do element-wise multiplication

		if key == "A" + str(i):
			A_list[length*i + col_or_row] = value 

		if key == "B" + str(i):
			B_list[width*i + col_or_row] = value

# Not sure if we need to print these...
print(A_list) 
print(B_list)


# Compute the final matrix C from the lists of values for A and B

for i in range(0,length):

	for j in range(0,width):

		my_row = A_list[length*i : length*(i+1)]
		my_col = B_list[width*j : width*(j+1)]
		dotpro = np.array(my_row)*np.array(my_col) 
		print "%s\t%s\t%s" % (i,j,dotpro)



