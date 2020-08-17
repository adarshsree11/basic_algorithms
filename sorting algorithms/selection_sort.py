def selectionSort(the_list):
	for i in range(len(the_list)):
		min_index = i
		for j in range(i+1, len(the_list)):
			if the_list[j] < the_list[min_index]:
				min_index = j
		if min_index != i:
			the_list[i],the_list[min_index] = the_list[min_index],the_list[i]

if __name__ == '__main__':

	unsorted_list = [17,87,6,22,54,3,13,41]
	print(unsorted_list)
	selectionSort(unsorted_list)
	print(unsorted_list)