import numpy as np
import timeit

### Completed: Finished the mergeSort and BubbleSort functions
#	Still need to implement a random array list based on size given
#	by users, and also need to implement a timer to determine performance


def mergeSort(lst):
	tmpList = []
	if len(lst) <=1:
		return lst

	mid = int(len(lst)/2)

	y = mergeSort(lst[:mid])
	z = mergeSort(lst[mid:])
	while len(y)>0 and len(z)>0:
		if y[0] > z[0]:
			tmpList.append(z[0])
			z.pop(0)

		else:
			tmpList.append(y[0])
			y.pop(0)

	tmpList += y
	tmpList += z
	return tmpList


def bubbleSort(lst):
	tmpList = []
	if len(lst) <=1: 
		return lst

	changed = True
	while changed:
		changed = False
		for i in xrange(len(lst)-1):
			if lst[i] > lst[i+1]:
				lst[i], lst[i+1] = lst[i+1], lst[i]
				changed = True

	return lst

if __name__ == "__main__":
    lst = [5,2,4,6,1,3,2,6]

    print "Unsorted:",lst
    print "BubbleSort:", bubbleSort(lst)
    print "MergeSort", mergeSort(lst)

