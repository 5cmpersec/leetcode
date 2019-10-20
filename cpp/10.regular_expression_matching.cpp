#include <iostream>
#include <string>
#include <cassert>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.empty())
            return s.empty();

        bool firstMatched = !s.empty() && ((p[0] == s[0]) || p[0] == '.');
        if (p.size() >=2 && p[1] == '*')
            return isMatch(s, p.substr(2)) || (firstMatched && isMatch(s.substr(1), p));
        else
            return firstMatched && isMatch(s.substr(1), p.substr(1));
    }
};

class Solution1 {
public:
    bool isMatch(string s, string p) {
        if (p.empty())
            return s.empty();

        bool firstMatched = !s.empty() && ((p[0] == s[0]) || p[0] == '.');
        if (p.size() >=2 && p[1] == '*')
            return isMatch(s, p.substr(2)) || (firstMatched && isMatch(s.substr(1), p));
        else
            return firstMatched && isMatch(s.substr(1), p.substr(1));
    }
};


int main() {
    Solution s;

    assert(s.isMatch("aa", "a") == false);
    assert(s.isMatch("aa", "a*") == true);
    assert(s.isMatch("ab", ".*") == true);
    assert(s.isMatch("aab", "c*a*b") == true);
    assert(s.isMatch("mississippi", "mis*is*p*.") == false);
}
