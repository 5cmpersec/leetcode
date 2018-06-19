class Solution:
	def maxProfit(self, prices):
		N = len(prices)
		if N < 2:
			return 0
		dpLR = [0] * (N+1)
		minLR = prices[0]
		for i in range(1, N):
			minLR = min(minLR, prices[i])
			dpLR[i] = max(dpLR[i-1], prices[i] - minLR)
		dpRL = [0] * (N+1)
		maxRL = prices[-1]
		for i in range(N-2, -1, -1):
			maxRL = max(maxRL, prices[i])
			dpRL[i] = max(dpRL[i+1], maxRL - prices[i])
		maxProfit = 0
		for i in range(0, N):
			maxProfit = max(maxProfit, dpLR[i] + dpRL[i+1])
		return maxProfit


if __name__ == '__main__':
	sol = Solution()
	assert(sol.maxProfit([3,3,5,0,0,3,1,4]) == 6)
	assert(sol.maxProfit([1,2,3,4,5]) == 4)
	assert(sol.maxProfit([7,6,4,3,1]) == 0)
