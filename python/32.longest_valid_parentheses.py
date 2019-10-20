class Solution(object):
	def longestValidParentheses(self, s):
		N = len(s)
		max_len = 0
		stack = []
		stack.append(-1)
		for i in range(0,N):
			if s[i] == '(':
				stack.append(i)
			else:
				stack.pop()
				if not stack:
					stack.append(i)
				else:
					max_len = max(max_len, i - stack[-1])
		return max_len
		

if __name__ == '__main__':
	sol = Solution()
	assert(sol.longestValidParentheses(')(')) == 0
	assert(sol.longestValidParentheses('(')) == 0
	assert(sol.longestValidParentheses('()')) == 2
	assert(sol.longestValidParentheses('()(()')) == 2


