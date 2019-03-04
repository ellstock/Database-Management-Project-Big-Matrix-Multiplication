#!/usr/bin/python

# The aim here is to split the large matrices into 4 blocks so as to obtain a 2x2 'matrix of matrices'


import sys
import time

#start_time = time.time()

# Here we are saying that we are splitting both A and B into a matrix of matrices with mxm blocks. We can obviously tune this parameter and add more if we want to have non-square matrices of blocks or if # we want different partitioning for A and B (so up to 4 parameters - number of blocks per row and column for A and B). Changing the number of parameters does require altering the line : "for l in #range(0,m)" in the code below as there will not be one universal m. 

m = int(2)

for line in sys.stdin :

    # Eliminate leading and trailing white spaces

    element = line.rstrip().split(",")
    
    # We want to split the line read from stdin into the provenance (original matrix A or B), i (the row number), j (the column number) and the value of the cell

    provenance = element[0]
    i = str(element[1])
    j = str(element[2])
    value = float(element[3])
        
	# What we want to do here is, for each block (4 in this case) of A and B, emit a line that will contain the the block name ("A00") for example, then the provenance of the value #(provenance_of_block - which contains specific row/column info about the value) and finally the value of the individual cell. We want to do this for every final block of C that this cell will be relevant #to in the multiplication. So for example, we need A00 to compute C00 and C01

    if provenance == 'A':
	# Here we split the length of the matrix into 2 for our 2 blocks length-wise

        if int(i) <= len(i)/2:

	# Here we split the width of the matrix into 2 for our 2 blocks width-wise

            if int(j) <= len(j)/2:

		# We start with the block in the upper left of A and call it A00

                block = 'A00'

		# This step creates the destination blocks that A00 will be relevant to and emits our (key,value) "pairs"

                for l in range(0,m):

                    key = 'C0' + str(l)
                    provenance_of_block = 'A' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)

		# We then repeat the exact same process for all blocks of A and of B (8 times in total - 4 blocks for A and 4 blocks for B)

            else:
                block = 'A01'
                for l in range(0,m):
                    key = 'C0' + str(l)
                    provenance_of_block = 'A' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)
        else:
            if int(j) <= len(j)/2:
                block = 'A10'
                for l in range(0,m):
                    key = 'C1' + str(l)
                    provenance_of_block = 'A' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)
            else:
                block = 'A11'
                for l in range(0,m):
                    key = 'C1' + str(l)
                    provenance_of_block = 'A' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)

    else:
        if int(i) <= len(i)/2:
            if int(j) <= len(j)/2:
                block = 'B00'
                for l in range(0,m):
                    key = 'C' + str(l) + '0'
                    provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)
            else:
                block = 'B01'
                for l in range(0,m):
                    key = 'C' + str(l) + '1'
                    provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)

        else:
            if int(j) <= len(j)/2:
                block = 'B10'
                for l in range(0,m):
                    key = 'C' + str(l) + '0'
                    provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)
            else:
                block = 'B11'
                for l in range(0,m):
                    key = 'C' + str(l) + '1'
                    provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)


#end_time = time.time()
#print ('The time taken for this job was ' + str(end_time - start_time) + ' seconds')

