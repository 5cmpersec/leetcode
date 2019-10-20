class Solution:
    def longestConsecutive(self, nums):
        N = len(nums)
        if N < 2: return N
        checked = {}
        ans = 0
        for i in nums:
            if i not in checked:
                left = checked[i-1] if i-1 in checked else 0
                right = checked[i+1] if i+1 in checked else 0
                checked[i] = left+right+1
                ans = max(ans, checked[i])
                if left: checked[i-left] = checked[i]
                if right: checked[i+right] = checked[i]
        return ans

if __name__ == '__main__':
    sol = Solution()
