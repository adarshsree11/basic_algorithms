if __name__ == '__main__':

	stack = []
	live = True
	
	while(live):
		choice = int(input("Choose\n\n1.push\n2.pop\n3.find\n4.get_size\n5.Print\n6.Exit\n"))
		
		if choice == 1:
			value = int(input("Data: "))
			stack.insert(0, value)
		
		elif choice == 2:

			if(len(stack) != 0):
				print("removed: " + str(stack.pop(0)) + "\n")
			else:
				print("stack Empty!\n")
		
		elif choice == 3:
			flag = True
			value = int(input("Find = "))
			
			for element in stack:
				if element == value:
					print("Found: " + str(value) + " at: " + str(stack.index(element)) + "\n")
					flag = False
			if flag:
				print("Err404: "+ str(value) + " not Found\n")
		
		elif choice == 4:
			print("\n")
			print("Current size of stack: " + str(len(stack)))
		
		elif choice == 5:
			print("\n")
			for element in stack:
				print(str(element))
		elif choice == 6:
			live = False
