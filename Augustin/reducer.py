#!/usr/bin/python

import sys
import numpy as np

# We know the dimensions of A and B!
length = int(35) + 1
width = int(35) + 1

# Initializing A_list and B_list to deal with sparsity
A_list = [0]*(length*width)
B_list = [0]*(length*width)

for line in sys.stdin:
    
    # Retrieving elements of (key,value) pair of our map output
    element = line.rstrip().split('\t')
    
    # The provenance of the element and its row/column
    matrc = element[0]
    
    # The intermediate index to keep the order within the original matrix
    index = int(element[1])
    
    # The value associated to that element:
    val = int(element[2])
    
    for i in range(0,601):
		if matrc == "A" + str(i):
			A_list[length*i + index] = val

		if matrc == "B" + str(i):
			B_list[width*i + index] = val

#For more transparancy have a look at the output of the two lists! (uncomment)
#print(A_list)
#print(B_list)


# We go through all elements of both lists:
for i in range(0,length):
	for j in range(0,width):
        
        # Retrieving line i of A and column j of B
		C_A = np.array(A_list[length*i : length*(i+1)])
		C_B = np.array(B_list[width*j : width*(j+1)])

        #Computing element-wise product of elments of line i of A and column j of B
        C_temp = C_A * C_B

        # Summing the product to yield element i,j of C!
        C = np.sum(C_temp)
        print '%s\t%s' % ((i,j),C)

        #Again for more transparancy have a look a this output rather than the above! (uncomment)
        # print '%s\t%s\t%s\t%s\t%s' % (i,j,C,my_row,my_col)



