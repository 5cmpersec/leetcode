import collections

class Solution:
	def findLadders_1(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: List[List[str]]
		"""
		wordSet = set(wordList)

		if endWord not in wordSet:
			return []

		if beginWord == endWord:
			return [[endWord]]

		q = []
		res = []
		seen = set()
		q.append([beginWord])
		all_chars = 'abcdefghijklmnopqrstuvwxyz'
		while q:
			size = len(q)
			seen_at_level = set()
			found = False
			for i in range(size):
				words = q.pop(0)
				last = words[-1]
				for i in range(len(last)):
					for j in range(len(all_chars)):
						if last[i] == all_chars[j]:
							continue
						newlast = list(last)
						newlast[i] = all_chars[j]
						newlaststr = ''.join(newlast)
						if newlaststr == endWord:
							newwords = list(words)
							newwords.append(newlaststr)
							res.append(newwords)
							found = True
						elif newlaststr not in seen and newlaststr in wordSet:
							newwords = list(words)
							newwords.append(newlaststr)
							q.append(newwords)
							seen_at_level.add(newlaststr)
			else:
				if found:
					return res
				else:
					seen.union(seen_at_level)
		return []

	def findLadders(self, beginWord, endWord, wordList):
		wordSet = set(wordList)

		if endWord not in wordSet:
			return []

		if beginWord == endWord:
			return [[endWord]]

		q = []
		
		seen = collections.defaultdict(set)
		q.append(beginWord)
		all_chars = 'abcdefghijklmnopqrstuvwxyz'
		found = False
		while q:
			size = len(q)
			seen_at_level = collections.defaultdict(set)
			for i in range(size):
				last = q.pop(0)
				for i in range(len(last)):
					for j in range(len(all_chars)):
						if last[i] == all_chars[j]:
							continue
						newlaststr = last[:i] + all_chars[j]+ last[i+1:]
						if newlaststr == endWord:
							seen_at_level[newlaststr].add(last)
							found = True
						elif newlaststr not in seen and newlaststr in wordSet:
							seen_at_level[newlaststr].add(last)
							q.append(newlaststr)
			else:
				seen.update(seen_at_level)
				if found:
					break
		if found:
			res = [[endWord]]
			while res and res[0][0] != beginWord:
				res = [[p]+r for r in res for p in seen[r[0]]]
			return res

		return []


if __name__ == '__main__':
	sol = Solution()
	print(sol.findLadders('hit','cog',  ["hot","dot","dog","lot","log","cog"]))
	print(sol.findLadders('hit','cog',  ["hot","dot","dog","lot","log"]))
	print(sol.findLadders('a','c',  ["a","b","c"]))
	print(sol.findLadders('red','tax',  ["ted","tex","red","tax","tad","den","rex","pee"]))