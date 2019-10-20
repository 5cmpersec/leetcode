class Solution:
	def firstMissingPositive(self, nums):
		N = len(nums)
		for i in range(N):
			while 0 < nums[i] < N and nums[i] != nums[nums[i]-1]:
				nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
		for i in range(N):
			if nums[i] != i+1:
				return i+1
		return N+1

if __name__ == '__main__':
	sol = Solution()
	print(sol.firstMissingPositive([3,4,-1,1]))
	print(sol.firstMissingPositive([]))
	print(sol.firstMissingPositive([-1,4,2,1,9,10]))
	print(sol.firstMissingPositive([-1,-4,-2,1,9,10]))
	print(sol.firstMissingPositive([-1]))
	print(sol.firstMissingPositive([1,1]))
