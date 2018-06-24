class Solution:
	def isValid(self, s):
		count = 0
		for i in range(len(s)):
			if s[i]=='(':
				count+=1
			if s[i]==')':
				count-=1
			if count <0:
				return False
		return count==0
	def removeInvalidParentheses(self, s):
		N = len(s)
		q = []
		checked=set()
		q.append(s)
		found = False
		res = []
		while q:
			current = q.pop(0)
			if self.isValid(current):
				res.append(current)
				found = True
			if found:
				continue
			for i in range(len(current)):
				if current[i] != '(' and current[i] != ')':
					continue
				newStr = current[:i] + current[i+1:]
				if newStr not in checked:
					checked.add(newStr)
					q.append(newStr)
		return res

if __name__ == '__main__':
	sol = Solution()
	assert(sorted(sol.removeInvalidParentheses('()())()'))) == sorted(['()()()', '(())()'])
	assert(sorted(sol.removeInvalidParentheses('x('))) == sorted(['x'])


