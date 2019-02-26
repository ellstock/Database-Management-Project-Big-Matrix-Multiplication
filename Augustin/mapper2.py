#!/usr/bin/env python

import sys   

# We assume that we know the size of the matrices we want to multiply

length = int(2)
width = int(2)

for line in sys.stdin:
	# Get rid of trailing white spaces and split the elements in the line into the origin matrix (A or B), i (the row), j (the column) and the value of the cell. 
	
	matrix, row, col, val = line.rstrip().split(",")

# For matrix A we want to output a key that contains the origin matrix and the row number and for matrix B we want to obtain a key that contains the origin matrix and the column number 

	if matrix == "A":

		for i in range(0,length):

			key = "A" + str(i)
			if row == str(i):

				print '%s\t%s\t%s' % (key,col,val)


	else :
		for i in range(0,width):

			key = "B" + str(i)
			if col == str(i):

				print '%s\t%s\t%s' % (key,row,val)
