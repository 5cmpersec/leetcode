class Solution:
	def isInterleaveRecursive(self, s1, s2, s3):
		if not s1:
			return s2==s3
		if not s2:
			return s1==s3
		if not s3:
			return False
		return ((s1[0] == s3[0] and self.isInterleaveRecursive(s1[1:],s2,s3[1:]))
			or (s2[0] == s3[0] and self.isInterleaveRecursive(s1,s2[1:],s3[1:])))

	def isInterleave(self, s1, s2, s3):
		M = len(s1)
		N = len(s2)
		if len(s3) != (M + N):
			return False
		elif M==0:
			return s2==s3
		elif N==0:
			return s1==s3

		dp = [[False for i in range(N+1)] for j in range(M+1)]
		for i in range(M+1):
			for j in range(N+1):
				if i == 0 and j == 0:
					dp[i][j] = True
				elif i == 0 and s2[j-1] == s3[j-1]:
					dp[i][j] = dp[i][j-1]
				elif j == 0 and s1[i-1] == s3[i-1]:
					dp[i][j] = dp[i-1][j]
				elif s1[i-1] == s3[i+j-1] and s2[j-1] != s3[i+j-1]:
					dp[i][j] = dp[i-1][j]
				elif s1[i-1] != s3[i+j-1] and s2[j-1] == s3[i+j-1]:
					dp[i][j] = dp[i][j-1]
				elif s1[i-1] == s3[i+j-1] and s2[j-1] == s3[i+j-1]:
					dp[i][j] = dp[i-1][j] or dp[i][j-1]
		return dp[M][N]

if __name__ == '__main__':
	sol = Solution()
	assert(sol.isInterleave('aabcc','dbbca', 'aadbbcbcac') == True)
	assert(sol.isInterleave('aabcc', 'dbbca', 'aadbbbaccc') == False)
	assert(sol.isInterleave('a', '', 'c') == False)
