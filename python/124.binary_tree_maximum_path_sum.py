class Solution:
	def maxPathSum(self, root):
		max_so_far = [root.val]
		path = self.postorder(root, max_so_far)
		return max_so_far[0]

	def postorder(self, node, max_so_far):
		if not node: return 0
		left = self.postorder(node.left, max_so_far)
		right = self.postorder(node.right, max_so_far)
		path = max(0, node.val + max(left,right))
		max_so_far[0] = max(max_so_far[0], node.val+left+right)
		return path

if __name__ == '__main__':
	sol = Solution()
