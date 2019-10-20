class Solution:
	def makeRLE(self, word):
		if not word:
			return [],[]
		key = [word[0]]
		value = [1]
		for i in range(1, len(word)):
			if word[i] != word[i-1]:
				key.append(word[i])
				value.append(1)
			else:
				value[-1] +=1
		return key,value

	def expressiveWords(self, S, words):
		key,value = self.makeRLE(S)

		res = 0
		for word in words:
			keyw, valuew = self.makeRLE(word)
			if key != keyw:
				continue
			for i in range(len(value)):
				if value[i] < valuew[i]:
					break
				elif value[i] < 3 and value[i] != valuew[i]:
					break
			else:
				res+=1
		return res

if __name__ == '__main__':
	sol = Solution()
	print(sol.expressiveWords('heeellooo', ["hello", "hi", "helo"]))