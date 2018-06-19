class Solution:
	def maxProfit1(self, k, prices):
		import sys
		N = len(prices)
		if N < 2 or k <= 0:
			return 0
		
		dp = [[0 for i in range(N+1)] for j in range(k+1)]
		for i in range(1, k+1):
			for j in range(1, N+1):
				diff = -sys.maxsize-1
				for m in range(0, j-1):
					diff = max(diff, dp[i-1][m] + prices[j-1] - prices[m])
				dp[i][j] = max(dp[i][j-1], diff)
		return dp[k][N]

	def maxProfit(self, k, prices):
		import sys
		N = len(prices)
		if N < 2 or k <= 0:
			return 0
		if k >= N >> 1:
			return sum([
				max(prices[i] - prices[i - 1], 0) for i in xrange(1, N)])
		dp = [[0 for i in range(N+1)] for j in range(k+1)]
		for i in range(1, k+1):
			diff = -sys.maxsize-1
			for j in range(1, N+1):
				diff = max(diff, dp[i-1][j-1] - prices[j-1])
				dp[i][j] = max(dp[i][j-1], diff + prices[j-1])
		return dp[k][N]



if __name__ == '__main__':
	sol = Solution()
	assert(sol.maxProfit(2, [2,4,1]) == 2)
	assert(sol.maxProfit(2, [3,3,5,0,0,3,1,4]) == 6)
	assert(sol.maxProfit(2, [1,2,3,4,5]) == 4)
	assert(sol.maxProfit(2, [7,6,4,3,1]) == 0)
