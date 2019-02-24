#!/usr/bin/python

# The aim here is to split the large matrices into 4 blocks so as to obtain a 2x2 'matrix of matrices'


import sys
import time

start_time = time.time()

for line in sys.stdin :
    element = line.rstrip().split(",")
    
    provenance = element[0]
    i = str(element[1])
    j = str(element[2])
    value = float(element[3])
        
    if provenance == 'A':
        if i <= len(i)/2:
            if j <= len(j)/2:
                key = 'A00'
                provenance_of_block = 'A' + str(i) + str(j)
                print '%s\t%s\t%s' % (key, provenance_of_block, value)
            else:
                key = 'A01'
                provenance_of_block = 'A' + str(i) + str(j)
                print '%s\t%s\t%s' % (key, provenance_of_block, value)
    
        else:
            if j <= len(j)/2:
                key = 'A10'
                provenance_of_block = 'A' + str(i) + str(j)
                print '%s\t%s\t%s' % (key, provenance_of_block, value)
            else:
                key = 'A11'
                provenance_of_block = 'A' + str(i) + str(j)
                print '%s\t%s\t%s' % (key, provenance_of_block, value)

    else:
        if i <= len(i)/2:
            if j <= len(j)/2:
                key = 'B00'
                provenance_of_block = 'B' + str(i) + str(j)
                print '%s\t%s\t%s' % (key, provenance_of_block, value)
            else:
                key = 'B01'
                provenance_of_block = 'B' + str(i) + str(j)
                print '%s\t%s\t%s' % (key, provenance_of_block, value)

        else:
            if j <= len(j)/2:
                key = 'B10'
                provenance_of_block = 'B' + str(i) + str(j)
                print '%s\t%s\t%s' % (key, provenance_of_block, value)
            else:
                key = 'B11'
                provenance_of_block = 'B' + str(i) + str(j)
                print '%s\t%s\t%s' % (key, provenance_of_block, value)

end_time = time.time()
