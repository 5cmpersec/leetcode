class Solution:
	def largestRectangleArea(self, heights):
		N = len(heights)
		ans = 0
		st = []
		for i in range(N+1):
			while st and (i==N or heights[st[-1]] > heights[i]):
				item = st.pop()
				next_lower_left = -1 if not st else st[-1]
				left = item - next_lower_left -1
				right = i - item - 1
				area = heights[item] * (left + right + 1)
				ans = max(ans, area)
			st.append(i)
		return ans
		
if __name__ == '__main__':
	sol = Solution()
	print(sol.largestRectangleArea([2,1,5,6,2,3]))