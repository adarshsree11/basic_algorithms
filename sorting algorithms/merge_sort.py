def mergeSort(the_list):
	if len(the_list) > 1:
		middle = len(the_list) // 2

		left = the_list[:middle]
		right = the_list[middle:]

		mergeSort(left)
		mergeSort(right)

		merge(the_list, left, right)

def merge(the_list, left, right):

	i = j = k= 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			the_list[k] = left[i]
			i += 1
		else:
			the_list[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		the_list[k] = left[i    ]
		i += 1
		k += 1

	while j < len(right):
		the_list[k] = right[j]
		j += 1
		k += 1


if __name__ == '__main__':

	unsorted_list = [17,87,6,22,41,3,13,54]
	print(unsorted_list)
	mergeSort(unsorted_list)
	print(unsorted_list)