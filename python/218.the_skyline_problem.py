import heapq
class Solution:
	def getSkyline(self, buildings):
		# convert buildings to list of events
		right_edges = list((item[1], 0, None) for item in buildings)
		events = sorted([(L, -H, R) for L, R, H in buildings] + right_edges)
		# list of return value with dummy.
		res = [[0,0]]
		# heap container: list of (Height,Right)
		heap = [(0, float('inf'))]
		for x in events:
			while x[0] >= heap[0][1]:
				heapq.heappop(heap)
			if x[1]:
				heapq.heappush(heap, (x[1], x[2]))
			height_changed = heap[0][0] + res[-1][1]
			if height_changed:
				res.append([x[0], -heap[0][0]])
		return res[1:]

if __name__ == '__main__':
	sol = Solution()
	print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
