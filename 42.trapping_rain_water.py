class Solution:
	def trap(self, height):
		units, base, N = 0, 0, len(height)
		if N < 3:
			return 0
		for i in range(N):
			if base == i or height[i] < height[base]:
				continue
			elif i > base:
				for j in range(base, i):
					units += height[base] - height[j]
				base = i
		if base < N-1:
			new_base = N-1
			for j in range(N-2, base, -1):
				if height[j] > height[new_base]:
					new_base = j
				else:
					units+= height[new_base] - height[j]
		return units

	def trap_1(self, height):
		""" O(N) time and O(N) space """
		units, stack, N = 0, [], len(height)
		if N < 3:
			return 0
		for i in range(N):
			if not stack or height[i] < stack[0]:
				stack.append(height[i])
			elif stack:
				base = stack[0]
				while stack:
					units += base - stack.pop()
				stack.append(height[i])
		if stack:
			base = stack.pop()
			while stack:
				next_item = stack.pop()
				if next_item > base:
					base = next_item
				else:
					units+= base - next_item
		return units

if __name__ == '__main__':
	sol = Solution()
	assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

