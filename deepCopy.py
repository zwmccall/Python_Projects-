def deep_copy(lst):
  """This program takes a list as input and then recursively finds the copy of the list"""
	m=[]
	for i in lst:
		if type(i)==list:
			m.append(deep_copy(i))
		else:
			m.append(i)
	return m


lst=[[1,2],3,4,[5,6,[7,8,[9,10],11],12,13],[14,15,16,[17],[18,19],20],21,22]
print 'Output:',deep_copy(lst)
