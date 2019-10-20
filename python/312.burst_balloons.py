class Solution:
	def maxCoins(self, nums):
		nums = [1] + [i for i in nums if i > 0] + [1]
		N = len(nums)
		memo = {}
		def dp(i,j, m):
			if i+1 == j : return 0
			if (i,j) in m:
				return m[i,j]
			ans = 0
			for k in range(i+1, j):
				ans = max(ans, nums[i]*nums[k]*nums[j] + dp(i, k, m) + dp(k, j, m))
			m[i,j] = ans
			return m[i,j]
		return dp(0,N-1, memo)


if __name__ == '__main__':
	sol = Solution()
	print(sol.maxCoins([3,1,5,8]))