if __name__ == '__main__':

	queue = []
	live = True
	
	while(live):
		choice = int(input("Choose\n\n1.push\n2.pop\n3.find\n4.get_size\n5.Print\n6.Exit\n"))
		
		if choice == 1:
			value = int(input("Data: "))
			queue.append(value)
		
		elif choice == 2:

			if(len(queue) != 0):
				print("removed: " + str(queue.pop(0)) + "\n")
			else:
				print("queue Empty!\n")
		
		elif choice == 3:
			flag = True
			value = int(input("Find = "))
			
			for element in queue:
				if element == value:
					print("Found: " + str(value) + " at: " + str(queue.index(element)) + "\n")
					flag = False
			if flag:
				print("Err404: "+ str(value) + " not Found\n")
		
		elif choice == 4:
			print("\n")
			print("Current size of Queue: " + str(len(queue)))
		
		elif choice == 5:
			print("\n")
			for element in queue:
				print(str(element))
		elif choice == 6:
			live = False
