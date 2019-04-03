/*
 * Question 36: Valid Sudoku
 * Medium
    Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/

#include <vector>
#include <cstdlib>
#include <utility>
#include <iostream>

using namespace std;


class Solution {

private:
    vector<vector<bool>> _rows;
    vector<vector<bool>> _cols;
    vector<vector<bool>> _subBox;

    void resetBoolVector(vector<vector<bool>>& x) {
        for (int i = 0; i < int(x.size()); ++i)
        for (int j = 0; j < int(x[0].size()); ++j)
            x[i][j] = false;
    }

    int getBoxIndex(int i, int j) {
        return (i/3) * 3 + (j/3);
    }

    /* Will update the vector that keeps track of the numbers used
     *
     * :returns: false if update is not 'successful', true otherwise
     */
    bool tryUpdate(vector<vector<bool>>& x, int index, int numIndex) {
        if (x[index][numIndex])
            return false;
        else
            x[index][numIndex] = true;
        return true;
    }

    void resetCacheVector(vector<vector<bool>>& x) {
        for (auto &a : x)
            fill(a.begin(), a.end(), false);
    }

public:

    // make the storage vectors larger so the index does not
    // have to be adjusted (because of lack of '0' in sudoku)
    Solution() : _rows(9, vector<bool>(10, false)),
                 _cols(9, vector<bool>(10, false)),
                 _subBox(9, vector<bool>(10, false)) {}

    bool isValidSudoku(vector<vector<char>>& board) {
        resetCacheVector(_rows);
        resetCacheVector(_cols);
        resetCacheVector(_subBox);

        int boardValue = 0;
        for (int rowInd = 0; rowInd < 9; ++rowInd)
        for (int colInd = 0; colInd < 9; ++colInd)
            if (board[rowInd][colInd] != '.') {

                boardValue = static_cast<int>(board[rowInd][colInd] - '0');
                if (
                    (!tryUpdate(_rows, rowInd, boardValue)) ||
                    (!tryUpdate(_cols, colInd, boardValue)) ||
                    (!tryUpdate(
                        _subBox, getBoxIndex(rowInd, colInd), boardValue))) {

                    return false;
                }
            }

        return true;
    }
};


string convertBool(bool x) {
    return x ? "True" : "False";
}


int main() {
    Solution sol;

    // expected true
    vector<vector<char>> board1({
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    });
    // expected false
    vector<vector<char>> board2({
      {'8','3','.','.','7','.','.','.','.'},
      {'6','.','.','1','9','5','.','.','.'},
      {'.','9','8','.','.','.','.','6','.'},
      {'8','.','.','.','6','.','.','.','3'},
      {'4','.','.','8','.','3','.','.','1'},
      {'7','.','.','.','2','.','.','.','6'},
      {'.','6','.','.','.','.','2','8','.'},
      {'.','.','.','4','1','9','.','.','5'},
      {'.','.','.','.','8','.','.','7','9'}
    });

    cout << "board1: " << convertBool(sol.isValidSudoku(board1)) << endl;
    cout << "board2: " << convertBool(sol.isValidSudoku(board2)) << endl;

    return 0;
}
