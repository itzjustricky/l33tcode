/*
 * Description:
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
 *
 * The robot can only move either down or right at any point in time.
 * The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
 *
 * How many possible unique paths are there?
 *
 * @author: Ricky Chang
*/


#include <vector>
#include <iostream>

using namespace std;


class Solution {
public:
    int uniquePaths(int m, int n) {

        vector<vector<int>> countMap(m, vector<int>(n));
        // first initialize the count map
        for (int i = 0; i < m; ++i)  countMap[i][0] = 1;
        for (int i = 0; i < n; ++i)  countMap[0][i] = 1;

        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                countMap[i][j] = countMap[i-1][j] + countMap[i][j-1];
            }
        }
        return countMap[m-1][n-1];
    }
};


int main() {

    Solution sol;

    cout << "for m=7, n=3 (expected: 28)" << endl;
    cout << sol.uniquePaths(7, 3) << endl;

    cout << "for m=3, n=2 (expected: 3)" << endl;
    cout << sol.uniquePaths(3, 2) << endl;

    return 0;
}
