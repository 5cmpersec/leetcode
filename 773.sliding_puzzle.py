class Solution:
	def slidingPuzzle(self, board):
		s = [str(board[i][j]) for i in range(2) for j in range(3)]
		q = []
		q.append(s)
		checked=set()
		checked.add(''.join(s))
		next=[[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
		ans =0
		while q:
			# control BFS level
			size = len(q)
			for i in range(size):
				current = q.pop(0)
				if current == ['1','2','3','4','5','0']:
					return ans
				else:
					index = current.index('0')
					adjs = next[index]
					for adj in adjs:
						newlist = list(current)
						newlist[index] = newlist[adj]
						newlist[adj] = '0'
						newliststr = ''.join(newlist)
						if newliststr not in checked:
							checked.add(newliststr)
							q.append(newlist)
			ans+=1
		return -1
				

if __name__ == '__main__':
	sol = Solution()
	assert(sol.slidingPuzzle([[1,2,3],[4,0,5]])) == 1
	assert(sol.slidingPuzzle([[1,2,3],[5,4,0]])) == -1
	assert(sol.slidingPuzzle([[4,1,2],[5,0,3]])) == 5
	assert(sol.slidingPuzzle([[3,2,4],[1,5,0]])) == 14



