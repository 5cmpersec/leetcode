class Solution:
	def findWords(self, board, words):
		K = len(words)
		trie = buildTrie(words)
		res = []
		M = len(board)
		N = len(board[0])
		for i in range(M):
			for j in range(N):
				dfs(i, j, board, trie, res)
		return res

def dfs(i, j, board, p, res):
	c = board[i][j]
	if c == '#' or not p.children[ord(c) - ord('a')]:
		return
	p = p.children[ord(c) - ord('a')]
	if p.word:
		res.append(p.word)
		p.word = None
	board[i][j] = '#'
	dx = [1, 0, -1, 0]
	dy = [0, -1, 0, 1]
	M = len(board)
	N = len(board[0])
	for d in range(4):
		x = i + dx[d]
		y = j + dy[d]
		if x < 0 or x > M-1 or y < 0 or y > N-1:
			continue
		dfs(x,y,board,p,res)
	board[i][j] = c
		

def buildTrie(words):
	root = TrieNode('')
	for word in words:
		p = root
		for c in word:
			pos = ord(c) - ord('a')
			if not p.children[pos]:
				p.children[pos] = TrieNode(c)
			p = p.children[pos]
		p.word = word
	return root

class TrieNode:
	def __init__(self, val):
		self.val = val
		self.word = None
		self.children = [None] * 26
		
if __name__ == '__main__':
	sol = Solution()
	words = ["oath","pea","eat","rain"]
	board = [
		['o','a','a','n'],
		['e','t','a','e'],
		['i','h','k','r'],
		['i','f','l','v']
	]
	# print(sol.findWords(board, words))
	print(sol.findWords([["b"],["a"],["b"],["b"],["a"]],["baa","abba","baab","aba"]))

