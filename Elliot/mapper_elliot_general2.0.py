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
        if int(i) <= len(i)/2:
            if int(j) <= len(j)/2:
                block = 'A00'
                key1 = 'C00'
                key2 = 'C01'
                provenance_of_block = 'A' + ',' + str(i) + ',' + str(j)
                print '%s\t%s\t%s\t%s' % (key1, block, provenance_of_block, value)
                print '%s\t%s\t%s\t%s' % (key2, block, provenance_of_block, value)
            else:
                block = 'A01'
                key1 = 'C00'
                Key2 = 'C01'
                provenance_of_block = 'A' + ',' + str(i) + ',' + str(j)
                print '%s\t%s\t%s\t%s' % (key1, block, provenance_of_block, value)
                print '%s\t%s\t%s\t%s' % (key2, block, provenance_of_block, value)
        else:
            if int(j) <= len(j)/2:
                block = 'A10'
                key1 = 'C10'
                key2 = 'C11'
                provenance_of_block = 'A' + ',' + str(i) + ',' + str(j)
                print '%s\t%s\t%s\t%s' % (key1, block, provenance_of_block, value)
                print '%s\t%s\t%s\t%s' % (key2, block, provenance_of_block, value)
            else:
                block = 'A11'
                key1 = 'C10'
                key2 = 'C11'
                provenance_of_block = 'A' + ',' + str(i) + ',' + str(j)
                print '%s\t%s\t%s\t%s' % (key1, block, provenance_of_block, value)
                print '%s\t%s\t%s\t%s' % (key2, block, provenance_of_block, value)

    else:
        if int(i) <= len(i)/2:
            if int(j) <= len(j)/2:
                block = 'B00'
                key1 = 'C00'
                key2 = 'C10'
                provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                print '%s\t%s\t%s\t%s' % (key1, block, provenance_of_block, value)
                print '%s\t%s\t%s\t%s' % (key2, block, provenance_of_block, value)
            else:
                block = 'B01'
                key1 = 'C01'
                key2 = 'C11'
                provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                print '%s\t%s\t%s\t%s' % (key1, block, provenance_of_block, value)
                print '%s\t%s\t%s\t%s' % (key2, block, provenance_of_block, value)

        else:
            if int(j) <= len(j)/2:
                block = 'B10'
                key1 = 'C00'
                key2 = 'C10'
                provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                print '%s\t%s\t%s\t%s' % (key1, block, provenance_of_block, value)
                print '%s\t%s\t%s\t%s' % (key2, block, provenance_of_block, value)
            else:
                block = 'B11'
                key1 = 'C01'
                key2 = 'C11'
                provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                print '%s\t%s\t%s\t%s' % (key1, block, provenance_of_block, value)
                print '%s\t%s\t%s\t%s' % (key2, block, provenance_of_block, value)

end_time = time.time()
