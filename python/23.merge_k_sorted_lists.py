#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def mergeKLists(self, lists):
		""" NLog(K) time using priority queue """        
		h = []
		for i in range(len(lists)):
			if lists[i]:
				heapq.heappush(h, (lists[i].val, i, lists[i]))
		res = None
		curr = None
		while h:
			val, i, next_node = heapq.heappop(h)
			if curr:
				curr.next = next_node
			curr = next_node
			if not res:
				res = curr
			if next_node.next:
				heapq.heappush(h, (next_node.next.val, i, next_node.next))
		return res

if __name__ == '__main__':
	sol = Solution()