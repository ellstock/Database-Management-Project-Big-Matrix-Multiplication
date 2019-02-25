#!/usr/bin/python

import sys

##get the size of the matrices from a size file:
#info = open("matrix_size.txt").readlines()
#for info_line in info:
#    info_line = info_line.strip()
#    matrix,i,j = info_line.split(",")
#    if matrix == "A":
#        #error prone type conversion
#        try:
#            A_i = int(i)
#            A_j = int(j)
#        except ValueError:
#            continue
#    else:
#        try:
#            B_i = int(i)
#            B_j = int(j)
#        except ValueError:
#            continue

#initialize row and column vector:
m = int(3)
p = int(3)
n = int(3)

# A (n x p) ; B (p x m)

ind_list=[]
val_list=[]
mat_list=[]

prev_key_index= None

for line in sys.stdin:
    #strip and get the values in each line (i.e. the key, the index and the value)
    line = line.strip()
    key_index, matrix, ind, v = line.split("\t")
    #error-prone type conversion to integer:
    try:
        key_index = int(key_index)
        ind = int(ind)
        v = int(v)
    except ValueError:
        continue
    
    if (key_index != prev_key_index) & (prev_key_index!=None):
        for l in range(len(mat_list)):
            if mat_list[l] == "A":
                for a in range(1,n+1):
                    key = str(ind_list[l]) + "," + str(a)
                    print "%s\t%s\t%s"%(str(prev_key_index),key,str(val_list[l]))
                    #we use tab to get rid of the problem of negative number
            else:
                for a in range(1,p+1):
                    key = str(a) + "," + str(ind_list[l])
                    print "%s\t%s\t%s"%(str(prev_key_index),key,str(val_list[l]))
        #initialize row and column vector:
        ind_list=[]
        val_list=[]
        mat_list=[]
    
    ind_list.append(ind)
    val_list.append(v)
    mat_list.append(matrix)
    prev_key_index = key_index

for l in range(len(mat_list)):
    if mat_list[l] == "A":
        for a in range(1,n+1):
            key = str(ind_list[l]) + "," + str(a)
            print "%s\t%s\t%s"%(str(prev_key_index),key,str(val_list[l]))
                    #we use tab to get rid of the problem of negative number
    else:
        for a in range(1,p+1):
            key = str(a) + "," + str(ind_list[l])
            print "%s\t%s\t%s"%(str(prev_key_index),key,str(val_list[l]))

##!/usr/bin/python
#
#import sys
#
###get the size of the matrices from a size file:
##info = open("matrix_size.txt").readlines()
##for info_line in info:
##    info_line = info_line.strip()
##    matrix,i,j = info_line.split(",")
##    if matrix == "A":
##        #error prone type conversion
##        try:
##            A_i = int(i)
##            A_j = int(j)
##        except ValueError:
##            continue
##    else:
##        try:
##            B_i = int(i)
##            B_j = int(j)
##        except ValueError:
##            continue
#
##initialize row and column vector:
#m = int(2)
#p = int(2)
#n = int(2)
#
## A (n x p) ; B (p x m)
#
#ind_list=[]
#val_list=[]
#mat_list=[]
#
#prev_key_index= None
#
#for line in sys.stdin:
#    #strip and get the values in each line (i.e. the key, the index and the value)
#    line = line.strip()
#    key_index, matrix, ind, v = line.split("\t")
#    #error-prone type conversion to integer:
#    try:
#        key_index = int(key_index)
#        ind = int(ind)
#        v = int(v)
#    except ValueError:
#        continue
#
#    if (key_index != prev_key_index) & (prev_key_index!=None):
#        for l in range(len(mat_list)):
#            if mat_list[l] == "A":
#                for a in range(1,n+1):
#                    key = str(ind_list[l]) + "," + str(a)
#                    print "%s\t%s\t%s"%(key,str(prev_key_index),str(val_list[l]))
#            #we use tab to get rid of the problem of negative number
#            else:
#                for a in range(1,p+1):
#                    key = str(a) + "," + str(ind_list[l])
#                    print "%s\t%s\t%s"%(key,str(prev_key_index),str(val_list[l]))
##initialize row and column vector:
#ind_list=[]
#    val_list=[]
#        mat_list=[]
#    
#    ind_list.append(ind)
#    val_list.append(v)
#    mat_list.append(matrix)
#    prev_key_index = key_index
#
#for l in range(len(mat_list)):
#    if mat_list[l] == "A":
#        for a in range(1,n+1):
#            key = str(ind_list[l]) + "," + str(a)
#            print "%s\t%s\t%s"%(key,str(prev_key_index),str(val_list[l]))
#    #we use tab to get rid of the problem of negative number
#else:
#    for a in range(1,p+1):
#        key = str(a) + "," + str(ind_list[l])
#            print "%s\t%s\t%s"%(key,str(prev_key_index),str(val_list[l]))
