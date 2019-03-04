#!/usr/bin/python

import sys

# We know the dimensions of A and B! We also assume that matrix is sorted by line then by column:
length = int(35) + 1
width = int(35) + 1

for line in sys.stdin:
    
    # Retrieving the element from our txt file:
    element = line.rstrip().split(",")
    
    # The provenance of the element
    matrix = element[0]
    
    # Retrieving row and column of the element
    row = element[1]
    col = element[2]
    
    # Transforming value into integer:
    val = int(element[3])
    
    
    if matrix == "A":
        for i in range(0,length):
            
            # Attributing key as provenance and line in which it was originally
            key = "A" + str(i)
            
            if row == str(i):
                print '%s\t%s\t%s' % (key,col,val)

    if matrix == "B":
        for i in range(0,width):
            
            # Attributing key as provenance and column in which it was originally
            key = "B" + str(i)
            
            if col == str(i):
                print '%s\t%s\t%s' % (key,row,val)
