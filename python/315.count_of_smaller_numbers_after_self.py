class Solution:
	def countSmaller(self, nums):
		N = len(nums)
		if N < 2: return [0] * N
		tree = BST()
		ans = []
		for i in range(N-1, -1, -1):
			node = TreeNode(nums[i])
			TreeInsert(tree, node)
			ans.append(node.num_less_keys)
		ans.reverse()
		return ans

class BST:
	def __init__(self, root=None):
		self.root = root

class TreeNode:
	def __init__(self, key, parent=None, left=None, right=None):
		self.key = key
		self.p = parent
		self.left = left
		self.right = right
		self.num_lefts = 0
		self.num_rights = 0
		self.num_less_keys = 0

def TreeInsert(tree, node):
	y = None
	x = tree.root
	less = 0
	while x:
		y = x
		if node.key <= x.key:
			x.num_lefts += 1
			x = x.left
		else:
			x.num_rights += 1
			less += x.num_lefts+1
			x = x.right
	node.p = y
	if not y:
		tree.root = node
	elif node.key <= y.key:
		y.left = node
	else:
		y.right = node
	node.num_less_keys = less

if __name__ == '__main__':
	sol = Solution()
	print(sol.countSmaller([5,2,6,1]))

