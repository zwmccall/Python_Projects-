def mymax(lst):
    """This function finds maximum element of a list using recursion. This uses technique involved in Bubble Sort"""
    if len(lst)==1:
        return lst[0]
    else:
        if lst[0]>lst[1]:
            lst[0],lst[1]=lst[1],lst[0]
        return mymax(lst[1:])
    
lst=[2,-9,78,45,65,100,34,24,45,34]
print "Input:",lst
print "largest:",mymax(lst)
