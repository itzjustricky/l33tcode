/*
 * Question 36: Valid Sudoku
 * Medium
    Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/

#include <vector>
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
        return i + j / 3;
    }

    bool tryUpdate(vector<vector<bool>>& x) {

    }

public:
    Solution() : _rows(9, vector<bool>(9, false)),
                 _cols(9, vector<bool>(9, false)),
                 _subBox(9, vector<bool>(9, false)) {}

    bool isValidSudoku(vector<vector<char>>& board) {

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {

            }
        }

    }
};


int main() {
    Solution sol;

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

    cout << "board1: " << sol.isValidSudoku(board1) << endl;
    cout << "board2: " << sol.isValidSudoku(board2) << endl;

    return 0;
}
