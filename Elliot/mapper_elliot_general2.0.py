#!/usr/bin/python

# The aim here is to split the large matrices into 4 blocks so as to obtain a 2x2 'matrix of matrices'


import sys
import time

start_time = time.time()

# A (n x p)
# B (p x m)

n = int(3)
p = int(3)
m = int(3)

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
                for l in range(0,m):
                    key = 'C0' + str(l)
                    provenance_of_block = 'A' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)
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
                for l in range(0,n):
                    key = 'C' + str(l) + '0'
                    provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)
            else:
                block = 'B01'
                for l in range(0,n):
                    key = 'C' + str(l) + '1'
                    provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)

        else:
            if int(j) <= len(j)/2:
                block = 'B10'
                for l in range(0,n):
                    key = 'C' + str(l) + '0'
                    provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)
            else:
                block = 'B11'
                for l in range(0,n):
                    key = 'C' + str(l) + '1'
                    provenance_of_block = 'B' + ',' + str(i) + ',' + str(j)
                    print '%s\t%s\t%s\t%s' % (key, block, provenance_of_block, value)

end_time = time.time()
