import math
class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def PreOrderTraversal(root, cb):
	cb(root.value, end=' ')
	if root.left is not None:
		PreOrderTraversal(root.left, cb)
	if root.right is not None:
		PreOrderTraversal(root.right, cb)
	return cb

def InOrderTraversal(root, cb):
	if root.left is not None:
		InOrderTraversal(root.left, cb)
	cb(root.value, end=' ')
	if root.right is not None:
		InOrderTraversal(root.right, cb)
	return cb


def PostOrderTraversal(root, cb):
	if root.left is not None:
		PostOrderTraversal(root.left, cb)
	if root.right is not None:
		PostOrderTraversal(root.right, cb)
	cb(root.value, end=' ')
	return cb

def CompleteTree(tree_serialized):
	root = Node(tree_serialized.pop(0))
	stack = list()
	stack.append(root)
	while len(stack) > 0:
		this = stack.pop(0)
		if len(tree_serialized) > 0 :
			new_node = Node(tree_serialized.pop(0))
			this.left = new_node
			stack.append(this.left)
		if len(tree_serialized) > 0 :
			new_node = Node(tree_serialized.pop(0))
			this.right = new_node
			stack.append(this.right)
	return root

def BuildBST(tree_serialized, start, end, balance='left'):
	if start > end:
		return None
	if balance == 'right':
		mid = math.ceil((end+start) / 2)
	elif balance == 'left':
		mid = math.floor((end+start) / 2)
	else:
		mid = int((end+start) / 2)
	root = Node(tree_serialized[mid])
	# print(root.value)
	# because the mid is used above
	root.left = BuildBST(tree_serialized, start, mid-1)
	root.right = BuildBST(tree_serialized, mid+1, end)
	return root

if __name__ == "__main__":
	t1 = [1,2,3,4,5,6,7]
	print(t1)
	# test = CompleteTree(t1)
	root = BuildBST(t1, 0, len(t1)-1, 'middle')
	print('root', root.value)
	InOrderTraversal(root, print)
	print()
	PreOrderTraversal(root, print)
	print()
	PostOrderTraversal(root, print)