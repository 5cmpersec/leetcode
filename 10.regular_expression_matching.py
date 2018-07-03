class Solution:
	def isMatch(self, s, p):
		""" use dynamic programming:
			O(MN) space complexity
			O(MN) time complexity
		"""
		M, N = len(s), len(p)
		# dp[i][j] = True if string of length i match pattern of length j
		dp = [[False] * (N+1) for _ in range(M+1)]
		dp[0][0] = True
		#dp[0][1] = False
		for i in range(1,N):
			if p[i] == '*' and dp[0][i-1]:
				dp[0][i+1] = True
		for i in range(M):
			for j in range(N):
				if p[j] == '.':
					dp[i+1][j+1] = dp[i][j]
				elif p[j] == s[i]:
					dp[i+1][j+1] = dp[i][j]
				elif p[j] == '*':
					if p[j-1] == s[i] or p[j-1] == '.':
						dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or dp[i][j+1]
					else:
						dp[i+1][j+1] = dp[i+1][j-1]
		return dp[M][N]


	def isMatch_1(self, s, p):
		# use recursive approach
		return self.isMatchR(s,p,len(s)-1, len(p)-1)
	
	def isMatchR(self, s, p, i, j):
		if j < 0:
			return i < 0

		elif i >= 0 and s[i] == p[j]:
			return self.isMatchR(s,p,i-1,j-1)
		elif i >= 0 and p[j] == '.':
			return self.isMatchR(s,p,i-1,j-1)
		elif i >= 0 and p[j] == '*':
			if s[i] == p[j-1] or p[j-1] == '.':
				return self.isMatchR(s,p,i,j-2) or self.isMatchR(s,p,i,j-1) or self.isMatchR(s,p,i-1,j)
			elif s[i] != p[j-1]:
				return self.isMatchR(s,p,i,j-2)
		else:
			# i < 0 and j >= 0
			if p[j] == '*':
				return self.isMatchR(s,p,i,j-2)

		return False

if __name__ == '__main__':
	sol = Solution()
	assert sol.isMatch('aa','a') == False
	assert sol.isMatch('aa','a*')== True
	assert sol.isMatch('ab','.*') == True
	assert sol.isMatch('aab','c*a*b') == True
	assert sol.isMatch('mississippi','mis*is*p*.') == False
	assert sol.isMatch('mississippi','mis*is*ip*.') == True