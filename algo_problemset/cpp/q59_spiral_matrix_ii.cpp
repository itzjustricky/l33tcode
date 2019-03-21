/*
 * Question 59:
    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    Example:

    Input: 3
    Output:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
*/

#include <tuple>
#include <vector>
#include <iostream>

using namespace std;


void printMatrix(const vector<vector<int>>& squareMatrix);


class Solution {
private:

    enum Command { right, down, left, up };

    Command switchCommand(Command prevCommand) {
        switch (prevCommand) {
            case right: return down;
            case down: return left;
            case left: return up;
            case up: return right;
        }
    }

    bool needToSwitchCommand(
            int i, int j,
            Command command,
            const vector<vector<int>>& matrix) {

        int n = matrix.size();
        switch (command) {
            case right:
                return (((j+1) >= n) || (matrix[i][j+1] != -1));
            case down:
                return (((i+1) >= n) || (matrix[i+1][j] != -1));
            case left:
                return (((j-1) < 0) || (matrix[i][j-1] != -1));
            case up:
                return (((i-1) < 0) || (matrix[i-1][j] != -1));
        }
    }

    pair<int, int> incrementIndex(int i, int j, Command command) {
        switch (command) {
            case right: return make_pair(i, j+1);
            case down: return make_pair(i+1, j);
            case left: return make_pair(i, j-1);
            case up: return make_pair(i-1, j);
        }
    }

public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> matrix(n, vector<int>(n, -1));

        Command command = right;
        int i = 0, j = 0, nSquared = n*n;
        for (int val = 1; val <= nSquared; ++val) {
            matrix[i][j] = val;
            if (needToSwitchCommand(i, j, command, matrix))
                command = switchCommand(command);
            tie(i, j) = incrementIndex(i, j, command);
        }

        return matrix;
    }
};


void printMatrix(const vector<vector<int>>& squareMatrix) {
    int n = squareMatrix.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << squareMatrix[i][j] << ' ';
        }
        cout << '\n';
    }
}


int main() {

    Solution sol;

    vector<vector<int>> matrix;
    matrix = sol.generateMatrix(10);
    printMatrix(matrix);

    return 0;
}
