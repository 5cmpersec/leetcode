class Solution(object):
	def minDistance(self, word1, word2):
		M = len(word1)
		N = len(word2)
		c = [[0 for i in range(N+1)] for j in range(M+1)]
		for i in range(M+1):
			c[i][0] = i
		for i in range(N+1):
			c[0][i] = i
		for i in range(1, M+1):
			for j in range(1, N+1):
				if word1[i-1] == word2[j-1]:
					c[i][j] = c[i-1][j-1]
				else:
					c[i][j] = min(c[i][j-1], c[i-1][j], c[i-1][j-1]) + 1
		return c[M][N]

if __name__ == '__main__':
	sol = Solution()
	assert(sol.minDistance('horse','ros') == 3)
	assert(sol.minDistance('intention', 'execution') == 5)
	assert(sol.minDistance('geek', 'gesek') == 1)
	assert(sol.minDistance('cat', 'cut') == 1)



