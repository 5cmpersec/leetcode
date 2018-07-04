class Solution:
	def isMatch(self, s, p):
		""" Dynamic programming with bottom-up approach
		O(MN) time complexity and O(MN) space complexity
		"""
		M = len(s)
		N = len(p)
		dp = [[False] * (N+1) for _ in range(M+1)]
		dp[-1][-1] = True

		for i in range(M, -1, -1):
			for j in range(N-1, -1, -1):
				first_match = i < M and p[j] in {s[i], '?', '*'}
				if p[j] == '*':
					dp[i][j] = dp[i][j+1] or (first_match and dp[i+1][j])
				else:
					dp[i][j] = first_match and dp[i+1][j+1]
		return dp[0][0]

	def isMatch_2(self, s, p):
		""" Dynamic programming with memo"""
		# memo[i,j] is match of (s[:i], p[j:])
		memo = {}
		def dp(i, j):
			if (i, j) not in memo:
				if j == len(p):
					ans = i == len(s)
				else:
					first_match = (i < len(s) and p[j] in {s[i], '?', '*'})
					if p[j] == '*':
						ans = dp(i,j+1) or (first_match and dp(i+1,j))
					else:
						ans = first_match and dp(i+1,j+1)
				memo[i,j] = ans
			return memo[i,j]

		return dp(0,0)

	def isMatch_1(self, s, p):
		""" recursive approach"""
		if not p:
			return not s
		first_match = bool(s) and p[0] in {s[0], '?', '*'}

		if p[0] == '*':
			return self.isMatch(s,p[1:]) or (first_match and self.isMatch(s[1:],p))
		else:
			return first_match and self.isMatch(s[1:], p[1:])

if __name__ == '__main__':
	sol = Solution()
	assert sol.isMatch('aa','a') == False
	assert sol.isMatch('aa', '*') == True
	assert sol.isMatch('cb', '?a') == False
	assert sol.isMatch('adceb', '*a*b') == True
	assert sol.isMatch('acdcb', 'a*c?b') == False
	assert sol.isMatch("ababbabbbbbbbaaaaabaabb", "*b***ab*a") == False
