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
	
	def __init__(self, head = None):
		self.head = head
		self.size = 0
	
	def get_size(self):
		return self.size
	
	def add(self, data):
		if self.head == None:
			new_node = node(data)
			new_node.set_next(new_node)
			self.head = new_node
			self.size += 1
		else:
			this_node = self.head
			new_node = node(data, this_node.get_next())
			this_node.set_next(new_node)
			
	def remove(self, data):
		this_node = self.head
		prev_node = None
		
		while this_node:
			
			if this_node.get_data() == data:
				
				if prev_node:
					prev_node.set_next(this_node.get_next())
				
				else:
					self.head = this_node.get_next()
				self.size -= 1
				return True
			
			else:
				prev_node = this_node
				this_node = this_node.get_next()
		
		return False

	def find(self, data):
		this_node = self.head
		pos = 0

		while this_node:
			
			if this_node.get_data() == data:
				return data, pos
			
			else:
				this_node = this_node.get_next()
				pos += 1
		
		return None

	def printList(self):
		this_node = self.head
		visited = this_node.get_data()
		linked_arr = []

		while this_node:
			if this_node.get_next().get_data() == visited:
				linked_arr.append(this_node.get_data())
				break
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
				print(str(data))
		elif choice == 6:
			live = False