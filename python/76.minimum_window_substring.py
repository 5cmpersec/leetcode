import collections, sys
class Solution:
    def minWindow(self, s, t):
        map, required = collections.Counter(t), len(t)
        end = begin = head = 0
        minWin = sys.maxsize
        while end < len(s):
            if map[s[end]] > 0: required -= 1
            map[s[end]] -= 1
            end += 1
            while required == 0:
                if minWin > end-begin:
                    minWin = end-begin
                    head = begin
                map[s[begin]] += 1
                if map[s[begin]] > 0: required += 1
                begin += 1
        return "" if minWin == sys.maxsize else s[head:head+minWin]

if __name__ == '__main__':
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC","ABC") == "BANC"
    assert sol.minWindow("aa","aa") == "aa"