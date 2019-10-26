#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int, int> ii;
const int N = 12;
int visit[1 << N][N];

class Solution {
public:
    // shortest path visiting all nodes with given starting node.
    int shortestPathLength(vector<vector<int>>& g, int start) {
        auto n = g.size();
        memset(visit, 255, sizeof(visit));
        queue<ii> Q;
        visit[1 << start][start] = 0;
        Q.push({1 << start, start});

        while (!Q.empty()) {
            auto it = Q.front();
            Q.pop();
            int mask = it.first;
            int cur = it.second;
            for (auto& e : g[cur]) {
                int nxt_mask = mask | (1 << e);
                if (visit[nxt_mask][e] >= 0) continue;
                Q.push({nxt_mask, e});
                visit[nxt_mask][e] = visit[mask][cur] + 1;
            }
        }
        int ret = 1 << 30;
        for (int i = 0; i < n; ++i) {
            if (visit[(1 << n)-1][i] >= 0) ret = min(ret, visit[(1 << n)-1][i]);
        }
        return ret;
    }
};


int main() {
    Solution sol;
    vector<vector<int>> g = {{1,2,3}, {0}, {0}, {0}};
    cout << sol.shortestPathLength(g, 0) << endl;

    return 0;
}
