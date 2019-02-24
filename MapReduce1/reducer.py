#!/usr/bin/python

# All elements of our two matrices were replicated the number of times they were necessary for each element of our final output matrix C.
# They were grouped according to the composite key (row and column of final matrix)
# We know that first key read by stdin will be (0,0) given passage through S&S (this will be usefull for keeping track of necessary computations

import sys
import numpy as np
import time

s_time = time.time() # Beginning time

list_A = []
list_B = []
current_key = str((0, 0))

for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    
    #Split line into array of entry data
    element = line.split("\t")
    
    key = element[0]
    provenance = str(element[1][2])
    tracker1 = element[1][7]
    tracker2 = element[1][9]
    tracker3 = element[1][10]
    
    if tracker1 == ",":
        
        if tracker2 == "-":
            
            value = -int(element[1][10])
    
        else:
            
            value = int(element[1][9])

    else:
    
        if tracker3 == "-":
        
            value = -int(element[1][11])
        
        else:
            
            value = int(element[1][10])

    # As long as we are dealing with the same key we keep on appending value either from A or B to a list in order to apply elemebt-wise multiplication
    
    if current_key == key:

        if provenance == "A":
    
            list_A.append(value)
            current_key = key

        else:
            
            list_B.append(value)
            current_key = key

    else:

        A = np.array(list_A)
        B = np.array(list_B)

        list_C = A * B
        C = np.sum(list_C)

        print '%s\t%s' % (current_key,C)
#        print '%s\t%s\t%s\t%s\t%s' % ((current_key),(C),list_A,list_B,list_C)

        current_key = key
        list_A = []
        list_B = []

        if provenance == "A":

            list_A.append(value)

        else:
            
            list_B.append(value)

# Printing last object!

if current_key == key:
    
    A = np.array(list_A)
    B = np.array(list_B)
    list_C = A * B
    C = np.sum(list_C)
    
    print '%s\t%s' % (current_key,C)
#    print '%s\t%s\t%s\t%s\t%s' % ((current_key),(C),list_A,list_B,list_C)

e_time = time.time() # End time

print('Reduce phase : ' + str(e_time-s_time))


#### NOTES : Not sure which format we should print out elements of our final matrix... We also need to create a
####        a matrix generator!!
####
#### Result of matrix multiplication for matrix1.txt is array([[22., 28.],
####                                                           [49., 64.]])
#### Found a way to print last element but it seems like it prints out the same as the beofre last
#### value...
####
#### Also the tracker method I designed isn't perfect, and this program works only for matrix values
#### below 10... and if size matrix is below 100.
####
#### It's pretty fast though, the most time is took by S&S which is out of our reach.
