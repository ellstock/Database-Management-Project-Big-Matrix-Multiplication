#!/usr/bin/python

import sys
import time
import numpy as np

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
