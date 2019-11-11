class Solution {
public:
    int maxDistToClosest(vector<int>& a) {
        int n = a.size();
        vector<int> L(n), R(n);

        L[0] = (a[0]==1)? 0: 1;
        for (int i = 1; i < n; ++i) {
            if (a[i] == 0) L[i] = L[i-1]+1;
            else L[i] = 0;
        }
        R[n-1] = (a[n-1]==1)? 0: 1;
        for (int i = n-2; i >= 0; --i) {
            if (a[i] == 0) R[i] = R[i+1]+1;
            else R[i] = 0;
        }

        int maxpos = -1;
        for (int i = 0; i < n; ++i) {
            if (a[i] == 0) {
                if (i == 0 || i == n-1) {
                    maxpos = max(maxpos, max(L[i], R[i]));
                } else {
                    maxpos = max(maxpos, min(L[i], R[i]));
                }

            }
        }
        return maxpos;
    }
};
