#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string shiftingLetters(string S, vector<int>& a) {
        int n = a.size();
        for (int i = n-2; i >= 0; --i) {
            a[i] += a[i+1];
            a[i] %= 26;
        }

        for (int i = 0; i < n; ++i) {
            int k = S[i] - 'a';
            k = (k+a[i]) % 26;
            S[i] = (char) ('a' + k);
        }
        return S;
    }
};


int main()
{
    string s = "abc";
    vector<int> v = {3,5,9};
    Solution sol;

    string g = sol.shiftingLetters(s, v);
    cout << g << endl;
}
