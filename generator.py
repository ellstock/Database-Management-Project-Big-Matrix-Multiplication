#!/usr/bin/python

# This file allows you to automatically generate two matrices A of size (m x p) and B of size (p x n) which will yield a final matrix C of size (m x n)
# Remeber that due to python's indexing (starting at 0) if you want a 3x3 matrix you'll need to input m = n = 2

import random
import sys

m = 2
p = 2
n = 2

for j in range(0, p + 1): 
    for i in range(0, m + 1):
        
        val_A = random.randint(-100,100)
        print '%s\t%s\t%s\t%s' % ("A",i,j,val_A)
              
    for l in range(0, n + 1):
        
        val_B = random.randint(-100,100)
        print '%s\t%s\t%s\t%s' % ("B",j,l,val_B)
