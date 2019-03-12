/*
 * Question 542

    Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

    The distance between two adjacent cells is 1.
    Example 1:
        Input:
        0 0 0
        0 1 0
        0 0 0
        Output:
        0 0 0
        0 1 0
        0 0 0

    Example 2:
        Input:
        0 0 0
        0 1 0
        1 1 1
        Output:
        0 0 0
        0 1 0
        1 2 1

    Note:
        1. The number of elements of the given matrix will not exceed 10,000.
        2. There are at least one 0 in the given matrix.
        3. The cells are adjacent in only four directions: up, down, left and right.
 *
 *
*/

#include <tuple>
#include <vector>
#include <utility>
#include <iostream>

using namespace std;


template <class T>
void printMatrix(vector<vector<T>>& matrix) {
    int n = matrix.size(),
        m = matrix[0].size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}


class Solution {
private:
    int _numOfRows;
    int _numOfCols;

    typedef pair<int, int> int_pair;
    typedef vector<int_pair> pair_vector;

    pair_vector findZeros(vector<vector<int>>& matrix) {
        pair_vector zeroIndices;

        for (int i = 0; i < _numOfRows; ++i) {
            for (int j = 0; j < _numOfCols; ++j) {
                if (matrix[i][j] == 0)
                    zeroIndices.emplace_back(i, j);
            }
        }
        return zeroIndices;
    }

    pair_vector updateOneStep(
            pair_vector& indices,
            vector<vector<int>>& updatedMatrix) {
        int i(0), j(0), currVal(0);
        pair_vector newIndices({});

        for (auto index: indices) {
            tie(i, j) = index;
            currVal = updatedMatrix[i][j];

            if (((i-1) >= 0) && (updatedMatrix[i-1][j] == -1)) {
                updatedMatrix[i-1][j] = currVal+1; newIndices.emplace_back(i-1, j);
            }
            if (((i+1) < _numOfRows) && (updatedMatrix[i+1][j] == -1)) {
                updatedMatrix[i+1][j] = currVal+1; newIndices.emplace_back(i+1, j);
            }
            if (((j-1) >= 0) && (updatedMatrix[i][j-1] == -1)) {
                updatedMatrix[i][j-1] = currVal+1; newIndices.emplace_back(i, j-1);
            }
            if (((j+1) < _numOfCols) && (updatedMatrix[i][j+1] == -1)) {
                updatedMatrix[i][j+1] = currVal+1; newIndices.emplace_back(i, j+1);
            }
        }
        return newIndices;
    }

public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        _numOfRows = matrix.size(),
        _numOfCols = matrix[0].size();

        vector<vector<int>> updatedMatrix(_numOfRows, vector<int>(_numOfCols, -1));

        int i(0), j(0);
        pair_vector indices(findZeros(matrix)), newIndices({});
        // first populate the update matrix with the zeros
        for (auto index: indices) { tie(i, j) = index; updatedMatrix[i][j] = 0; }
        while (!indices.empty())
            indices = updateOneStep(indices, updatedMatrix);

        return updatedMatrix;
    }
};


int main() {

    Solution sol;

    vector<vector<int>> matrix1(
        {{0, 0, 0},
         {0, 1, 0},
         {0, 0, 0}});

    vector<vector<int>> matrix2(
        {{0, 0, 0},
         {0, 1, 0},
         {1, 1, 1}});

    vector<vector<int>> updatedMatrix1(sol.updateMatrix(matrix1));
    vector<vector<int>> updatedMatrix2(sol.updateMatrix(matrix2));

    printMatrix(updatedMatrix1);
    cout << endl;
    printMatrix(updatedMatrix2);

    return 0;
}
