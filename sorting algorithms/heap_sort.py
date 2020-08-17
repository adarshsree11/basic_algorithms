def heapify(the_list, length, i):
	largest = i    # considering as root
	left = 2*i+1   # index of left child
	right = 2*i+2  # index of right child

	#see if left child exist and greater than root
	if left<length and the_list[i]<the_list[left]:
		largest = left

	#see if right child exist and greater than root
	if right<length and the_list[largest]<the_list[right]:
		largest = right

	#change root if larger number caught as left or right child
	if largest!=i:
		the_list[i],the_list[largest]=the_list[largest],the_list[i]
		# heapify the new root
		heapify(the_list, length, largest)


def heapSort(the_list):
	n = len(the_list)

	#heapify the full list
	for i in range(n//2-1, -1, -1):
		#heapify from last element with child to top
		heapify(unsorted_list, n, i)

	#heapsort sxtracting elements one by one
	for i in range(n-1, 0, -1):
		#swapping the root element which is max to its position
		the_list[i],the_list[0] = the_list[0],the_list[i]
		#heapify from root again length reduced to 'i' to keep sorted elements unchanged
		heapify(the_list, i, 0)


if __name__ == '__main__':

	unsorted_list = [17,87,6,22,54,3,13,41]
	print(unsorted_list)
	heapSort(unsorted_list)
	print(unsorted_list)