import collections
class Solution:
	def maxSlidingWindow(self, nums, k):
		N = len(nums)
		q = collections.deque()
		ans = []
		for i in range(N):
			while q and nums[q[-1]] < nums[i]:
				q.pop()
			while q and q[0] < i-k+1:
				q.popleft()
			q.append(i)
			if i >= k-1:
				ans.append(nums[q[0]])
		return ans
		
if __name__ == '__main__':
	sol = Solution()
	print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))