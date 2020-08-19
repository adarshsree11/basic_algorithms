def interpolationSearch(listt, lo, hi, value):
	global count
	count += 1
	if lo<=hi and value>=listt[lo] and value <= listt[hi]:

		mid = int(lo + (((hi-lo)/(listt[hi]-listt[lo]))*(value-listt[lo])))
		if listt[mid] == value:
			return mid

		elif listt[mid] < value:
			return interpolationSearch(listt, mid+1, hi, value)

		else:
			return interpolationSearch(listt, lo, mid-1, value)

	return -1

sorted_list = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44,  46, 48, 49, 50, 56, 67, 84, 85, 86, 93, 95, 97, 112, 125, 126, 126, 131, 132, 138, 150]
#count to count the no. of iteration there by prove efficiency of the algorithm
count = 0

value = int(input("Search: "))
found = interpolationSearch(sorted_list, 0, len(sorted_list)-1, value)
if found != -1:  
    print("Element found at index", found) 
else:  
    print("Element not found")
print("iterations--"+str(count))