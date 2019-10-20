class Solution:
	def findDuplicate(self, nums):
		"""
		Use slow-fast pointer same to linked-list cycle detection
		SC: O(1)
		TC: O(n)
		"""
		slow = 0
		fast = 0
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			if nums[slow] == nums[fast]:
				break
		slow = 0
		while nums[slow] != nums[fast]:
			slow = nums[slow]
			fast = nums[fast]
		return nums[slow]

	def findDuplicate_3(self, nums):
		"""
		Use binary search
		SC: O(1)
		TC: O(nlogn)
		"""
		low = 1
		high = len(nums)-1
		while low < high:
			mid = (low+high) // 2
			count = 0
			for num in nums:
				count = count+1 if num <= mid else count
			if count > mid:
				high = mid
			else:
				low = mid+1
		return low

	def findDuplicate_2(self, nums):
		"""
		Count number of occurences of all numbers,
		duplicated number has number of occurences more than 1
		SC: O(n)
		TC: O(n)
		"""
		count = [0] * len(nums)

		for i in nums:
			count[i-1] +=1
		for i in range(len(count)):
			if count[i] > 1:
				return i+1

	def findDuplicate_1(self, nums):
		"""
		First, sorts the arrays
		then find the number has same value to the next one.
		O(n) space and O(nlogn) running time.
		"""
		nums_sorted = sorted(nums)

		for i in range(len(nums_sorted)-1):
			if nums_sorted[i] == nums_sorted[i+1]:
				return nums_sorted[i]

if __name__ == '__main__':
	sol = Solution()
	print(sol.findDuplicate([1,3,4,2,2]))
	print(sol.findDuplicate([1,1]))