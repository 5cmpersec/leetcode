import sys
class Solution:
	def shortestPathLength(self, graph):
		N = len(graph)
		M = 1 << N
		visit = [[-1] * N for _ in range(M)]
		q = []
		for i in range(N):
			visit[1 << i][i] = 0
			q.append((i, 1 << i))
		while q:
			node, state = q.pop(0)
			for adj in graph[node]:
				next_state = state | (1 << adj)
				if visit[next_state][adj] >= 0:
					continue
				visit[next_state][adj] = visit[state][node] + 1
				q.append((adj, next_state))
		ret = min(visit[M-1][i] for i in range(N) if i>=0)
		return ret

if __name__ == '__main__':
	sol = Solution()
	assert(sol.shortestPathLength([[1,2,3],[0],[0],[0]]) == 4)
	assert(sol.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]) == 4)
