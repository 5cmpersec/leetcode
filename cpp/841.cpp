class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        queue<int> Q;
        vector<bool> visited(n);
        visited[0] = true;
        Q.push(0);

        while (!Q.empty()) {
            int cur = Q.front();
            Q.pop();
            for (auto& i:rooms[cur]) {
                if (!visited[i]) {
                    visited[i] = true;
                    Q.push(i);
                }
            }
        }

        int sum = 0;
        for (auto v : visited) sum +=v;
        return sum == n;
    }
};
