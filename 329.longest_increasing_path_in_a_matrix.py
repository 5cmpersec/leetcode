class Solution:
    def longestIncreasingPath(self, matrix):
        M = len(matrix)
        if M < 1: return 0
        N = len(matrix[0])
        if N < 1: return 0
        dp = [[0] * N for _ in range(M)]
        maxval = [0]
        for i in range(M):
            for j in range(N):
                dfs(i, j, matrix, dp, maxval)
        return maxval[0]

def dfs(i, j, matrix, dp, maxval):
    if dp[i][j] > 0: return
    M = len(matrix)
    N = len(matrix[0])
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    dp[i][j] = 1
    for d in range(4):
        x = i + dx[d]
        y = j + dy[d]
        if x < 0 or x > M-1 or y < 0 or y > N-1:
            continue
        if matrix[i][j] >= matrix[x][y]:
            continue
        if dp[x][y] == 0:
            dfs(x, y, matrix, dp, maxval)
        dp[i][j] = max(dp[i][j], 1 + dp[x][y])
    maxval[0] = max(maxval[0], dp[i][j])

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
    print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
