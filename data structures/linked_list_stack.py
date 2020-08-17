class node(object):
	
	def __init__(self, data, next_node = None):
		self.data = data
		self.next_node = next_node
	
	def get_next(self):
		return self.next_node
	
	def set_next(self, next_node):
		self.next_node = next_node
	
	def get_data(self):
		return self.data
	
	def set_data(self,data):
		self.data = data


class LinkedList(object):
	
	def __init__(self, tail = None):
		self.tail = tail
		self.size = 0
	
	def get_size(self):
		return self.size
	
	def add(self, data):
		new_node = node(data,self.tail)
		self.tail = new_node
		self.size += 1
	
	def remove(self, data):
		this_node = self.tail
		prev_node = None
		
		while this_node:
			
			if this_node.get_data() == data:
				
				if prev_node:
					prev_node.set_next(this_node.get_next())
				
				else:
					self.tail = this_node.get_next()
				self.size -= 1
				return True
			
			else:
				prev_node = this_node
				this_node = this_node.get_next()
		
		return False

	def find(self, data):
		this_node = self.tail
		pos = 0

		while this_node:
			
			if this_node.get_data() == data:
				return data, pos
			
			else:
				this_node = this_node.get_next()
				pos += 1
		
		return None

	def printList(self):
		this_node = self.tail
		linked_arr = []

		while this_node:
			linked_arr.append(this_node.get_data())
			this_node = this_node.get_next()

		return linked_arr

if __name__ == '__main__':

	new_list = LinkedList()
	live = True
	
	while(live):
		choice = int(input("Choose\n\n1.add\n2.remove\n3.find\n4.get_size\n5.Print\n6.Exit\n"))
		
		if choice == 1:
			value = int(input("Data: "))
			new_list.add(value)
		
		elif choice == 2:
			value = int(input("Remove: "))
			
			if new_list.remove(value):
				print("removed: " + str(value) + "\n")
			
			else:
				print("Err404: "+ str(value) + " not Found\n")
		
		elif choice == 3:
			value = int(input("Find = "))
			
			if new_list.find(value):
				print("Found: " + str(new_list.find(value)[0]) + " at: " + str(new_list.find(value)[1]) + "\n")
			
			else:
				print("Err404: "+ str(value) + " not Found\n")
		
		elif choice == 4:
			print("Current size of List: " + str(new_list.get_size()))
		
		elif choice == 5:
			li_array = new_list.printList()
			for data in li_array:
				print(str(data) + "\n")
		elif choice == 6:
			live = False