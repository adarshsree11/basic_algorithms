def LinearSearch(listt, value):
	for element in listt:
		if element == value:
			print(str(value) +" is found")
			break
	else:
		print(str(value) +" is not found")

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

value = int(input("Search: "))

LinearSearch(sorted_list, value)