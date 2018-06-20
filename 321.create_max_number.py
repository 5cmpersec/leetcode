class Solution:
	def maxNumber(self, nums1, nums2, k):
		M = len(nums1)
		N = len(nums2)
		ans = []
		i = max(0, k-N)
		while i <= k and i <= M:
			candidate = self.merge(self.maxArray(nums1, i), self.maxArray(nums2, k-i))
			if self.greater(candidate, 0, ans, 0):
				ans = candidate
			i+=1
		return ans

	def maxArray(self, nums, k):
		"""
		Given one array of length n, create the maximum number of length k.
		time complexity = O(N)
		"""
		N = len(nums)
		ans = []
		for i in range(N):
			while ans and N-i+len(ans) > k and ans[-1] < nums[i]:
				ans.pop()
			if len(ans) < k:
				ans.append(nums[i])
		return ans

	def greater(self, nums1, i, nums2, j):
		while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
			i+=1
			j+=1
		return j==len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])

	def merge(self, nums1, nums2):
		"""
		Given two array of length m,n, create the maximum number of length k=m+n.
		time complexity = O(M+N)
		"""
		M = len(nums1)
		N = len(nums2)
		i = 0
		j = 0
		ans = []
		for r in range(M+N):
			if self.greater(nums1, i, nums2, j):
				ans.append(nums1[i])
				i+=1
			else:
				ans.append(nums2[j])
				j+=1
		return ans
		
		

if __name__ == '__main__':
	sol = Solution()
	# assert(sol.maxArray([3,4,6,5], 2) == [6,5])
	# assert(sol.maxArray([9,1,2,5,8,3], 3) == [9,8,3])
	# assert(sol.maxArray([9,1,2,5,8,3], 4) == [9,5,8,3])
	# assert(sol.merge([3,9], [8,9]) == [8,9,3,9])
	# assert(sol.merge([9], [8,9]) == [9,8,9])
	# assert(sol.merge([6,7], [6,0,4]) == [6,7,6,0,4])
	assert(sol.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5) == [9,8,6,5,3])
	assert(sol.maxNumber([6,7], [6,0,4], 5) == [6,7,6,0,4])
	assert(sol.maxNumber([3,9], [8,9], 3) == [9,8,9])








