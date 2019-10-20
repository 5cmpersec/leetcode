class Solution:
	def search(self, nums, target):
		if not nums:
			return False
		return self.binarySearch(nums, target, 0, len(nums)-1)

	def binarySearch(self, nums, target, left, right):
		mid  = int((left + right) / 2)
		if nums[mid] == target:
			return True
		if left > right:
			return False
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
				if (nums[mid] != nums[right]):
					return self.binarySearch(nums, target, mid+1, right)
				else:
					return self.binarySearch(nums, target, left, mid-1) or self.binarySearch(nums, target, mid+1, right)
		return False


if __name__ == '__main__':
	sol = Solution()
	print(sol.search([2,5,6,0,0,1,2], 0))
	print(sol.search([2,5,6,0,0,1,2], 3))
