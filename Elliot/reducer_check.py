#!/usr/bin/python

import sys
import time
import numpy as np

# first three elements of list name are the past block and last two digits represent i and j of future block.

# Block C00:
B0000 = []
A0100 = []
B1000 = []
A0000 = []

# Block C01
A0001 = []
B0101 = []
A0101 = []
B1101 = []

# Block C10
A1010 = []
B0010 = []
A1110 = []
B1010 = []

# Block C11
A1011 = []
B0111 = []
A1111 = []
B1111 = []

for line in sys.stdin :
    ls = line.rstrip().split('\t')
    future_block = str(ls[0])
    past_block = str(ls[1])
    provenance = str(ls[2])
    value = float(ls[3])
    provenance_details = provenance.split(',')
    provenance_matrix = provenance_details[0]
    i = str(provenance_details[1])
    j = str(provenance_details[2])
    
    
    
    

    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (future_block,past_block,provenance,provenance_details,provenance_matrix, i, j, value)
