class Solution:
    def wordBreak(self, s, wordDict):
        res = []
        for i in range(len(s)):
            w = s[:i+1]
            print
            if w in wordDict:
                rest = self.wordBreak(s[i+1:], wordDict)
                if rest:
                    for item in rest:
                        res.append(w + " " + item)
                else:
                    res.append(w)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]))