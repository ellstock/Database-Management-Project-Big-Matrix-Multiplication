#!/usr/bin/python

import sys
import time

# We assume we know the dimensions of the final matrix output (m row, n columns)
# Here we will set m and n for our matrix example where A is (2 x 3) and B is (3 x 2) so C is (2 x 2)
# Since python indexing starts at 0 it has column indexes 0 and 1 (same for rows)

# IMPORTANT : - If you are using our matrix generator please input the same m and n you used in that script!
#             - If you aren't don't mind that, just change the split to "," instead of "\t"!

s_time = time.time() # Beginning time

m = 1
n = 1

for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    
    # split the line corresponding to one element of either matrix
    element = line.split(",")
    
    # Retrieve the 4 attributes of each line respectively
    provenance = element[0]
    row = str(element[1])
    col = str(element[2])
    value = float(element[3])


    # Matrix A
    ## If line corresponds to an element of matrix A, we will need to replicate each element of this matrix n times

    if provenance == "A":

        for k in range(0, n + 1): # We add 1 so Python will replicate n times
            
            key = row + "," + str(k)
            print '%s\t%s\t%s' % (key, col, value)

    # Matrix B
    # If line corresponds to an element of matrix B, we will need to replicate each element of this matrix m times

    else:
    
        for i in range(0, m + 1): # We add 1 so Python will replicate m times
        
            key = str(i) + "," + col
            print '%s\t%s\t%s' % (key, row, value)

e_time = time.time() # End time

# Printing last object!

#print '%s\t%s' % ((i, col),(provenance, row, value))

# Each element then goes through a sort&shuffle phase where key-value pairs are grouped by composite key (k1, k2)

#### NOTES : We could try two implementations :
####    - this one
####    - using a dictionnary where we append every element which should have the same composite key
####
#### Main difference is that dictionnaries may be faster but are memory bound, which implies it may crash if the
#### matrix is too big

#### Approx 1min to map&sort 99x99 * 99x99 matrix product


