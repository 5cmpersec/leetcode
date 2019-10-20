class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        map<int, int> m;
        for (auto& item : hand) {
            m[item]++;
        }

        while (!m.empty()) {
            int first = m.begin()->first;
            m[first]--;
            if (m[first] == 0) m.erase(first);
            for (int i = 1; i < W; ++i) {
                int next = first + i;
                if (m.count(next) == 0) return false;
                m[next]--;
                if (m[next] == 0) m.erase(next);
            }
        }
        return true;
    }
};
