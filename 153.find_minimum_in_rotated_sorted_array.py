class Solution:
	def findMin(self, nums):
		return self.findMinBS(nums, 0, len(nums)-1)

	def findMinBS(self, nums, left, right):
		if left == right or nums[left] < nums[right]:
			return nums[left]

		mid = int((left+right) / 2)
		if nums[mid] > nums[left]:
			return self.findMinBS(nums, mid+1, right)
		elif nums[mid] < nums[left]:
			return self.findMinBS(nums, left, mid)
		elif nums[mid] == nums[left]:
			return self.findMinBS(nums, mid+1, right)

if __name__ == '__main__':
	sol = Solution()
	print(sol.findMin([4,5,6,7,0,1,2]))
	print(sol.findMin([3,4,5,1,2]))
	print(sol.findMin([1]))
	print(sol.findMin([2,1]))