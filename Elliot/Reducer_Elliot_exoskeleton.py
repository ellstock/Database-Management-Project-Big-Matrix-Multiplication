for line in sys.stdin : 
	ls = line.rstrip().split(\t)
	future_block = ls[0]
	past_block = ls[1]
	provenance = ls[2]
	value = ls[3]
	provenance_details = provenance.split(',')
	provenance_matrix = provenance_details[0]
	i = provenance_details[1]
	j = provenance_details[2]


	if future_block = "C00" :
		A0000 = []   					# first three elements of list name are the past block and last two digits represent i and j of future block.
		B0000 = []
		A0100 = []
		B1000 = []
		if past_block == "A00" : 
			A0000 = A0000.append(value)
		elif past_block == "B00" :
			B0000 = B0000.append(value)
		elif past_block == "A01" :
			A0100 = A0100.append(value)
		else :
			B1000 = B1000.append(value)




	if future_block = "C01" :
		A0001 = []   					
		B0101 = []
		A0101 = []
		B1101 = []
		if past_block == "A00" : 
			A0001 = A0001.append(value)
		elif past_block == "B01" :
			B0101 = B0101.append(value)
		elif past_block == "A01" :
			A0101 = A0101.append(value)
		else :
			B1101 = B1101.append(value)




	if future_block = "C10" :
		A1010 = []   					
		B0010 = []
		A1110 = []
		B1010 = []
		if past_block == "A10" : 
			A1010 = A1010.append(value)
		elif past_block == "B00" :
			B0010 = B0010.append(value)
		elif past_block == "A11" :
			A1110 = A1110.append(value)
		else :
			B1010 = B1010.append(value)




	if future_block = "C11" :
		A1011 = []   					
		B0111 = []
		A1111 = []
		B1111 = []
		if past_block == "A10" : 
			A1011 = A1011.append(value)
		elif past_block == "B01" :
			B0111 = B0111.append(value)
		elif past_block == "A11" :
			A1111 = A1111.append(value)
		else :
			B1111 = B1111.append(value)



	C00 = A0000*B0000 + A0100*B1000
	C01 = A0001*B0101 + A0101*B1101
	C10 = A1010*B0010 + A1110*B1010
	C11 = A1011*B0111 + A1111*B1111

	print(C00)
	print(C01)
	print(C10)
	print(C11)
