def Transverse(matrix):
	'''This function is used to find transpose of a matrix'''
	transverse_matrix=[]
	for i in range(len(matrix[0])):
		row=[]#Creates a empty list
		for j in range(len(matrix)):
			row.append(matrix[j][i])#finds transpose of a column
		transverse_matrix.append(row)
	return transverse_matrix	
matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print 'Initial matrix :\n',matrix
transverse_matrix=Transverse(matrix)
print 'After transpose :\n',transverse_matrix
