class Solution {
public:
    string solve(string& s) {
        string ret;
        for (auto& c : s) {
            if (c == '#') {
                if (!ret.empty()) ret.pop_back();
            } else {
                ret.push_back(c);
            }
        }
        return ret;
    }

    bool backspaceCompare(string S, string T) {
        return solve(S) == solve(T);
    }
};
