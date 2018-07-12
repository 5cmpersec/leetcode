from fractions import Fraction
class Solution:
    def maxPoints(self, points):
        N = len(points)
        if N < 3:
            return N
        ans = 0
        for i in range(N):
            duplicate = 0
            vertical = 0
            mapping = collections.defaultdict(int)
            local_max = 0
            for j in range(i+1, N):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicate += 1
                elif points[i].x == points[j].x:
                    vertical += 1
                else:
                    f = Fraction(points[j].y-points[i].y, points[j].x-points[i].x)
                    mapping[f] += 1
            max_slope = max(mapping.values()) if mapping else 0
            local_max = max(max_slope, vertical)
            ans = max(ans, local_max+duplicate+1)
        return ans

if __name__ == '__main__':
    sol = Solution()
