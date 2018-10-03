def fibonacci(n):
  """This function finds Nth tems of fibonacci series using recursion"""
	if n==1:
		return 1
	elif n==2:
		return 1
	return fibonacci(n-1)+fibonacci(n-2)

n=input()
print fibonacci(n)
