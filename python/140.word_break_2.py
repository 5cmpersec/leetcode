import collections
class Solution:
    def wordBreak(self, s, wordDict):
        N = len(s)
        wordSet = set(wordDict)
        # dp[i]=True means can break string s[i:]
        dp = [False] * (N+1)
        # can break empty string
        dp[N] = True
        parents = collections.defaultdict(list)
        for i in range(N-1, -1, -1):
            for j in range(N, i-1, -1):
                if dp[j] and s[i:j] in wordSet:
                    dp[i] = True
                    parents[j].append(i)
        if dp[0]:
            return self.makeResult(s, parents)
        return []

    def makeResult(self, s, parents):
        def dfs(i):
            res = []
            for j in parents[i]:
                if j == 0:
                    res.append(s[0:i])
                else:
                    prefix = dfs(j)
                    for item in prefix:
                        res.append(item + " " + s[j:i])
            return res
        return dfs(len(s))

    def wordBreakRecursive(self, s, wordDict):
        res = []
        for i in range(len(s)):
            w = s[:i+1]
            print
            if w in wordDict:
                rest = self.wordBreakRecursive(s[i+1:], wordDict)
                if rest:
                    for item in rest:
                        res.append(w + " " + item)
                else:
                    res.append(w)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]))
    print(sol.wordBreak('pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"]))
    print(sol.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))