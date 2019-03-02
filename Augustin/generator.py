#!/usr/bin/python

# This file allows you to automatically generate two matrices A of size (m x p) and B of size (p x n) which will yield a final matrix C of size (m x n)
# Remeber that due to python's indexing (starting at 0) if you want a 3x3 matrix you'll need to input m = n = 2

import random
import sys

m = 36
p = 36
n = 36

for i in range(0, m):
    for j in range(0, p):
        
        val_A = random.randint(-10,10)
        
        if val_A != 0:
            line = "A" + "," + str(i) + "," + str(j) + "," + str(val_A)
            print '%s' % (line)

for j in range(0, p):
    for l in range(0, n):
        
        val_B = random.randint(-10,10)
        
        if val_B != 0:
            line = "B" + "," + str(j) + "," + str(l) + "," + str(val_B)
            print '%s' % (line)
