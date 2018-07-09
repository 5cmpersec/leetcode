class Solution:
    def trapRainWater(self, heightMap):
        M = len(heightMap)
        if M < 3:
            return 0
        N = len(heightMap[0])
        if N < 3:
            return 0
        visited = [[False] * N for _ in range(M)]
        level = [[sys.maxsize] * N for _ in range(M)]
        ans = 0
        h = []
        for i in range(M):
            for j in range(N):
                if i == 0 or i == M-1 or j == 0 or j == N-1:
                    level[i][j] = heightMap[i][j]
                    heapq.heappush(h, (level[i][j], i, j))
                    visited[i][j] = True
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        while h:
            curr, x, y = heapq.heappop(h)
            for k in range(4):
                i,j = x+dx[k], y+dy[k]
                if i<0 or i>=M or j<0 or j>=N or visited[i][j]:
                    continue
                level[i][j] = max(heightMap[i][j], min(level[i][j], curr))
                heapq.heappush(h, (level[i][j], i, j))
                visited[i][j] = True
            ans += curr - heightMap[x][y]
        return ans

