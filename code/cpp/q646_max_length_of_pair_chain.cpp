/*
 *
 *
 * @author: Ricky Chang
 */

#include <iostream>

#include <vector>
#include <algorithm>

using namespace std;


class Solution {

private:

    static bool comparePairs(const vector<int>& p1,
                      const vector<int>& p2) {
        return p1[1] < p2[1];
    }

public:

    int findLongestChain(vector<vector<int>>& pairs) {
        int n = pairs.size(), longestChain = 1;
        if (n == 0) { return 0; }

        sort(pairs.begin(), pairs.end(), comparePairs);

        vector<int>& pair = pairs[0];

        for (int i = 1; i < n; ++i) {
            if (pair[1] < pairs[i][0]) {
                pair = pairs[i];
                ++longestChain;
            }
        }
        return longestChain;
    }
};


int main() {

    vector<vector<int>> pairs = {
        {1, 2}, {4, 5}, {8, 9},
        {-1, 0}, {10, 12}, {3, 10},
    };

    Solution sol;
    cout << "The longest chain is " << sol.findLongestChain(pairs) << endl;


    return 0;
}
