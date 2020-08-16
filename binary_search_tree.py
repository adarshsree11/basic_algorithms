class node(object):
	
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
	
	def get_left(self):
		return self.left
	
	def set_left(self, left):
		self.left = left

	def get_right(self):
		return self.right
	
	def set_right(self, right):
		self.right = right
	
	def get_data(self):
		return self.data
	
	def set_data(self,data):
		self.data = data


class binarySearchTree(object):
	
	def __init__(self, root = None):
		self.root = root
		self.size = 0
	
	def get_size(self):
		return self.size
	
	def insert(self, data):
		new_node = node(data)
		if self.root == None :
			self.root = new_node
		else:
			curr_node = self.root
			parent_node = None

			while True:
				parent_node = curr_node
				print(new_node.data)
				print(parent_node.data)
				if new_node.data < parent_node.data:
					curr_node = curr_node.get_left()

					if curr_node == None:
						parent_node.set_left(new_node)
						break

				else:
					curr_node = curr_node.get_right()

					if curr_node == None:
						parent_node.set_right(new_node)
						break

		self.size += 1

	def search(self, data):
		curr_node = self.root

		while curr_node.get_data() != data:
			if data < curr_node.data:
				curr_node = curr_node.get_left()
			else:
				curr_node = curr_node.get_right()
			if curr_node == None:
				return None

		return curr_node
	

	def inorder(self, node):
		visited = []
		if node:
			visited = self.inorder(node.left)
			visited.append(node.data)
			visited = visited + self.inorder(node.right)
		return visited

	def preorder(self, node):
		visited = []
		if node:
			visited.append(node.data)
			visited = visited + self.preorder(node.left)
			visited = visited + self.preorder(node.right)
		return visited

	def postorder(self, node):
		visited = []
		if node:
			visited = self.postorder(node.left)
			visited = visited + self.postorder(node.right)
			visited.append(node.data)
		return visited


if __name__ == '__main__':

	bst = binarySearchTree()
	live = True
	
	while(live):
		choice = int(input("Choose\n\n1.insert\n2.preorder\n3.inorder\n4.postorder\n5.search\n6.Exit\n"))
		
		if choice == 1:
			value = int(input("Data: "))
			bst.insert(value)
		
		elif choice == 2:
			print("preorder: ")
			print(bst.preorder(bst.root))

		elif choice == 3:
			print("inorder: ")
			print(bst.inorder(bst.root))

		elif choice == 4:
			print("postorder: ")
			print(bst.postorder(bst.root))
		
		elif choice == 5:
			value = int(input("Search: "))
			if(bst.search(value) == None):
				print('Sorry ' + str(value) + ' is unavailable in binary search tree')
			else:
				print(str(value) + ' is Available in binary search tree')
		elif choice == 6:
			live = False