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

if __name__ == '__main__':

	the_list = [17,87,6,22,54,3,13,41]
	print(the_list)
	n = len(the_list)
	for i in range(n//2-1, -1, -1):
		#heapify from last element with child to top
		heapify(the_list, n, i)
	for i in range(len(the_list))
	print(the_list)