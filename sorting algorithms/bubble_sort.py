def BubbleSort(list_to_sort):
	#print("in bubble sort")
	length = len(list_to_sort)
	while(length > 1):
		#print("in while")
		#bubble = list_to_sort[1]
		for i in range(length-1):
			#print("in for")
			if list_to_sort[i]>list_to_sort[i+1]:
				#print("in if")
				list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
		length -= 1


unsorted_list = [93,77,31,55,44,54,26,17,20]

print('unsorted list input is ' + str(unsorted_list))

#QuickSort(unsorted_list, 0, len(unsorted_list)-1)
BubbleSort(unsorted_list)

print('sorted list output is ' + str(unsorted_list))