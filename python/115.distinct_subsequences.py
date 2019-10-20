class Solution:
	def numDistinctRecursive(self, s, t):
		if len(t) == 0:
			return 1
		if len(s) == 0:
			return 0
		if s[-1] != t[-1]:
			return self.numDistinctRecursive(s[:-1], t)
		else:
			return self.numDistinctRecursive(s[:-1], t[:-1]) + self.numDistinctRecursive(s[:-1], t)

	def numDistinct(self, s, t):
		M = len(s)
		N = len(t)

		dp = [[0 for j in range(N+1)] for i in range(M+1)]

		for i in range(M+1):
			for j in range(N+1):
				if j == 0:
					dp[i][j] = 1
				elif i == 0:
					dp[i][j] = 0
				elif s[i-1] != t[j-1]:
					dp[i][j] = dp[i-1][j]
				elif s[i-1] == t[j-1]:
					dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
		return dp[M][N]


if __name__ == '__main__':
	sol = Solution()
	assert(sol.numDistinct('rabbbit','rabbit') == 3)
	assert(sol.numDistinct('babgbag', 'bag') == 5)
	assert(sol.numDistinct('babgbag', 'bag') == 5)
