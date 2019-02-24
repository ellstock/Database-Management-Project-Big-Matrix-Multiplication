#!/usr/bin/env python

import sys
import numpy as np

length = int(200) + 1
width = int(200) + 1

A_list = [0]*(length*width)
B_list = [0]*(length*width)
for line in sys.stdin:
	temp = max(length,width)
	for i in range(0,temp):
		matrc, cr, val = line.rstrip().split("\t")
		cr, val = map(int,[cr,val])
		if matrc == "A" + str(i):
			A_list[length*i + cr] = val 

		if matrc == "B" + str(i):
			B_list[width*i + cr] = val
print(A_list)
print(B_list)



for i in range(0,length):
	for j in range(0,width):
		my_row = A_list[length*i : length*(i+1)]
		my_col = B_list[width*j : width*(j+1)]
		dotpro = np.dot(my_row, my_col)
		print("%s\t%s\t%s"%(i,j,dotpro))



