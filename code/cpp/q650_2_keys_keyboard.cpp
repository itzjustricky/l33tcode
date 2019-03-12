/*
 * Question 650:

    Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

    Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.
    Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

    Example 1:
    Input: 3
    Output: 3
    Explanation:
    Intitally, we have one character 'A'.
    In step 1, we use Copy All operation.
    In step 2, we use Paste operation to get 'AA'.
    In step 3, we use Paste operation to get 'AAA'.

    Note:
    The n will be in the range [1, 1000].
 *
*/

#include <vector>
#include <limits>
#include <iostream>

using namespace std;

void printMatrix(vector<vector<int>> matrix, int n);


class Solution {

private:
    typedef vector<vector<int>> vvi;
    // row is <notepad char count>, column is <clipboard char count>
    // given these 2, this records what is minimum steps to reach n
    int _desiredNum;
    int _maxClipboard;
    vvi _hashMap;

    /*
     * n: is the # of 'A' on the notepad
     * c: is the # of 'A' characters copied to clipboard
     */
    int minSteps(int n, int c) {
        int minStepsFromState = 0;

        // if goes over clipboard size
        if (c >= _maxClipboard) return numeric_limits<int>::max();
        // if computed already return hash
        if (_hashMap[n-1][c-1] != -1) return _hashMap[n-1][c-1];
        // no path to reach desired # of letters
        if (((_desiredNum - n) < c) || (n > _desiredNum))
            return _hashMap[n-1][c-1] = numeric_limits<int>::max();

        // current clipboard matches # of characters on notepad
        if (n == c) {
            minStepsFromState = minSteps(n+c, c);
        } else {
            // min between copying from notepad vs. pasting on notepad
            minStepsFromState = min(
                minSteps(n, n), minSteps(n+c, c));
        }

        if (minStepsFromState == numeric_limits<int>::max())
            return _hashMap[n-1][c-1] = minStepsFromState;
        else
            return _hashMap[n-1][c-1] = (minStepsFromState + 1);
    }

public:
    int minSteps(int n) {
        if (n == 1) return 0;

        _desiredNum = n;
        _maxClipboard = n/2 + 1;
        _hashMap.resize(n, vector<int>(_maxClipboard, -1));
        for (int i = 0; i < _maxClipboard; ++i) _hashMap[n-1][i] = 0;

        // first step must be to copy to clipboard
        return minSteps(1, 1) + 1;
    }
};


void printMatrix(vector<vector<int>> matrix, int n) {
    for (int i = n; i >= 0; --i) {
        for (int j = 0; j <= n; ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}


int main() {
    Solution sol;

    int steps = 3;
    cout << "For " << steps << " steps, solution is: " << sol.minSteps(steps) << endl;

    return 0;
}
