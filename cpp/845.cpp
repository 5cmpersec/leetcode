class Solution {
public:
    int longestMountain(vector<int>& A) {
        int n = A.size();
        if (!n) return 0;

        vector<int> L(n), R(n);
        L[0] = 1;
        for (int i = 1; i < n; ++i) {
            if (A[i] > A[i-1]) {
                L[i] = L[i-1] + 1;
            } else {
                L[i] = 1;
            }
        }

        R[n-1] = 1;
        for (int i = 1; i < n; ++i) {
            if (A[n-i-1] > A[n-i]) {
                R[n-i-1] = R[n-i] + 1;
            } else {
                R[n-i-1] = 1;
            }
        }

        int ret = 0;
        for (int i = 0; i < n; ++i) {
            if (L[i] != 1 && R[i] != 1) {
                ret = max(ret, L[i] + R[i] -1);
            }
        }
        return ret;
    }
};
