class Solution:
	def search(self, nums, target):
		if not nums:
			return -1
		return self.binarySearch(nums, target, 0, len(nums)-1)

	def binarySearch(self, nums, target, left, right):
		mid  = int((left + right) / 2)
		if nums[mid] == target:
			return mid
		if left > right:
			return -1
		if nums[mid] > nums[left]:
			if nums[left] <= target < nums[mid]:
				return self.binarySearch(nums, target, left, mid-1)
			else:
				return self.binarySearch(nums, target, mid+1, right)
		elif nums[mid] < nums[left]:
			if nums[mid] < target <= nums[right]:
				return self.binarySearch(nums, target, mid+1, right)
			else:
				return self.binarySearch(nums, target, left, mid-1)
		elif nums[mid] == nums[left]:
				return self.binarySearch(nums, target, mid+1, right)
		return -1


if __name__ == '__main__':
	sol = Solution()
	print(sol.search([4,5,6,7,0,1,2], 0))
	print(sol.search([4,5,6,7,0,1,2], 3))
	print(sol.search([1,3], 3))

