def QuickSort(list_to_sort, first, last):

	if first < last :
		split_point = Partition(list_to_sort, first, last)

		QuickSort(unsorted_list, first, split_point - 1)
		QuickSort(unsorted_list, split_point + 1, last)

def Partition(data_list, first, last):

	pivot = data_list[first]
	#print('pivot is ' + str(pivot))
	p = first + 1
	q = last

	while p < q :
		while (data_list[p] <= pivot) and (q>=p) and (p < len(data_list)-1) :
			#print('p is ' + str(data_list[p]))
			p = p + 1
			#print(p)
		while (data_list[q] >= pivot) and (q>=p):
			#print('q is ' + str(data_list[q]))
			q = q - 1
		if p < q :
			#print('p is ' + str(data_list[p]))
			#print('q is ' + str(data_list[q]))
			data_list[p], data_list[q] = data_list[q], data_list[p]
	
	data_list[first], data_list[q] = data_list[q], data_list[first]
	return q
		
		

unsorted_list = [93,77,31,55,44,54,26,17,20]

print('unsorted list input is ' + str(unsorted_list))

QuickSort(unsorted_list, 0, len(unsorted_list)-1)

print('sorted list output is ' + str(unsorted_list))