def shellSort(the_list):
	n = len(the_list)
	gap = n//2

	while gap > 0:
		for i in range(0, n-gap):
			if (the_list[i] > the_list[i+gap]):
				the_list[i],the_list[i+gap] = the_list[i+gap],the_list[i]
		gap = gap-1		



if __name__ == '__main__':

	unsorted_list = [17,87,6,22,54,3,13,41]
	print(unsorted_list)
	shellSort(unsorted_list)
	print(unsorted_list)