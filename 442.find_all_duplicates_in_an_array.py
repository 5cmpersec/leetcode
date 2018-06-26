class Solution:
	def findDuplicates(self, nums):
		res = []
		for x in nums:
			if nums[abs(x)-1] < 0:
				res.append(abs(x))
			else:
				nums[abs(x) -1] *= -1
		return res


if __name__ == '__main__':
	sol = Solution()
	print(sol.findDuplicates([4,3,2,7,8,2,3,1]))

