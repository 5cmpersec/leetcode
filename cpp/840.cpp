class Solution {
public:
    bool check(vector<vector<int>>& a, int u, int v) {
        set<int> A;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                A.insert(a[u+i][v+j]);
            }
        }
        if (A.size() != 9 || *A.begin() != 1 || *A.rbegin() != 9) return false;
        set<int> B;
        // all rows
        for (int i = 0; i < 3; ++i) {
            int sum = 0;
            for (int j = 0; j < 3; ++j) {
                sum += a[u+i][v+j];
            }
            B.insert(sum);
        }
        // all columns
        for (int j = 0; j < 3; ++j) {
            int sum = 0;
            for (int i = 0; i < 3; ++i) {
                sum += a[u+i][v+j];
            }
            B.insert(sum);
        }
        // all diagonals
        int sum = 0;
        for (int i = 0; i < 3; ++i) {
            sum += a[u+i][v+i];
        }
        B.insert(sum);
        sum = 0;
        for (int i = 0; i < 3; ++i) {
            sum += a[u+2-i][v+i];
        }
        B.insert(sum);

        return B.size()==1;
    }
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int ret = 0;
        for (int i = 0; i+2 < m; ++i) {
            for (int j = 0; j+2 < n; ++j) {
                if (check(grid, i, j)) ++ret;
            }
        }
        return ret;
    }
};
