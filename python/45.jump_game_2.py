import sys
import collections

class Solution:
	def jump(self, nums):
		"""
		Use BFS to build a tree
		least jums step is level of end node.
		"""
		N = len(nums)
		if N < 2:
			return 0
		level = 0
		end = 0
		next_end = 0
		for i in range(len(nums)):
			next_end = max(next_end, i+nums[i])
			if next_end >= N-1:
				return level+1
			if i == end:
				level+=1
				end = next_end

	def jump_3(self, nums):
		"""
		Use BFS
		"""
		N = len(nums)
		q=[]
		seen = collections.defaultdict(list)
		q.append(0)
		while q:
			top = q.pop(0)
			if nums[top] == 0:
				continue
			found = False
			for i in range(top+nums[top], top, -1):
				if i >= N-1:
					found = True
					seen[N-1].append(top)
					break
				if i not in seen and nums[i] != 0:
					seen[i].append(top)
					q.append(i)
			if found:
				break
		count = 0
		index = N-1
		while index != 0:
			count+=1
			index = seen[index][0]
			
		return count

	def jump_2(self, nums):
		"""
		Use dynamic programming
		O(n) space and O(n2) time
		"""
		N = len(nums)
		if N == 1:
			return 0
		dp = [0]*N
		for i in range(N-2, -1, -1):
			if nums[i] == 0:
				dp[i] = sys.maxsize
			elif i + nums[i] >= N-1:
				dp[i] = 1
			else:
				dp[i] = 1+min(dp[i+j] for j in range(1,nums[i]+1))
		return dp[0]

	def jump_1(self, nums):
		"""
		Recursive with memoi
		O(n) space and O(n2) time
		"""
		N = len(nums)
		if N == 1:
			return 0
		memo = [0]*N
		return self.jumpRecursive(nums, 0, N-1, memo)

	def jumpRecursive(self, nums, start, end, memo):
		if memo[start] > 0:
			return memo[start]

		res = 0
		if nums[start] == 0:
			res = sys.maxsize
		elif end - start <= nums[start]:
			res = 1
		else:
			minStep = sys.maxsize
			for i in range(1, nums[start]+1):
				minStep = min(minStep, self.jumpRecursive(nums, start+i, end, memo))
			res = minStep+1
		memo[start] = res
		return res

if __name__ == '__main__':
	sol = Solution()
	print(sol.jump([2,3,1,1,4]))
	print(sol.jump([1,0]))
	# print(sol.jump([2, 1]))