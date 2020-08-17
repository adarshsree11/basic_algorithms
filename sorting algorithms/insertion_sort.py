def insertionSort(the_list):
	for i in range(1, len(the_list)):
		j = i
		while j > 0 and the_list[j-1] > the_list[j]:
			the_list[j-1], the_list[j] = the_list[j], the_list[j-1]
			j -= 1

if __name__ == '__main__':

	unsorted_list = [17,87,6,22,54,3,13,41]
	print(unsorted_list)
	insertionSort(unsorted_list)
	print(unsorted_list)