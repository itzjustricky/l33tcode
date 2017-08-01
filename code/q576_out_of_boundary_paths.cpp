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

    const static int MAX_HEIGHT = 50,
                     MAX_WIDTH = 50,
                     MAX_MOVES = 50;
    const unsigned int ANSWER_MOD = pow(10, 9) + 7;

    int m_GridHash[MAX_HEIGHT][MAX_WIDTH][MAX_MOVES] = {{{0}}};
    bool m_GridHashIndicator[MAX_HEIGHT][MAX_WIDTH][MAX_MOVES] = {{{false}}};
    int m_GridHeight;
    int m_GridWidth;

    bool outOfWidthBounds(int j) {
        return (j < 0) || (j >= m_GridWidth);
    }

    bool outOfHeightBounds(int i) {
        return (i < 0) || (i >= m_GridHeight);
    }

    bool outOfBounds(int i, int j) {
        return outOfHeightBounds(i) || outOfWidthBounds(j);
    }

    int exploreGridPaths(int i, int j, int N) {
        if (outOfBounds(i, j)) {
            return 1;
        } else if (N == 0) {
            return 0;
        } else if (m_GridHashIndicator[i][j][N-1]) {
            return m_GridHash[i][j][N-1];
        }

        m_GridHash[i][j][N-1] = \
            (exploreGridPaths(i-1, j, N-1) + \
             exploreGridPaths(i+1, j, N-1) + \
             exploreGridPaths(i, j-1, N-1) + \
             exploreGridPaths(i, j+1, N-1)) % ANSWER_MOD;
        m_GridHashIndicator[i][j][N-1] = true;
        return m_GridHash[i][j][N-1];
    }

public:

    int findPaths(int m, int n, int N, int i, int j) {
        m_GridHeight = m; m_GridWidth = n;
        return exploreGridPaths(i, j, N);
    }
};


int main() {

    Solution sol;
    // cout << "Paths found: " << sol.findPaths(2, 2, 2, 0, 0) << endl;
    // cout << "Paths found: " << sol.findPaths(1, 3, 3, 0, 1) << endl;
    cout << "Paths found: " << sol.findPaths(45, 35, 47, 20, 31) << endl;

    return 0;
}
