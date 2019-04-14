/*
    1027. Longest Arithmetic Sequence
    Difficulty: Medium

    Given an array A of integers, return the length of the longest arithmetic
    subsequence in A.

    Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with
    0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic
    if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

    Example 1:
    Input: [3,6,9,12]
    Output: 4
    Explanation:
    The whole array is an arithmetic sequence with steps of length = 3.

    Example 2:
    Input: [9,4,7,2,10]
    Output: 3
    Explanation:
    The longest arithmetic subsequence is [4,7,10].

    Example 3:
    Input: [20,1,15,3,10,5,8]
    Output: 4
    Explanation:
    The longest arithmetic subsequence is [20,15,10,5].
 *
 */


#include <map>
#include <vector>
#include <iostream>

using namespace std;


class Solution {

private:
    typedef vector<map<int, int>> v_of_map;

    void updateMap(
            int diffValue,
            int fromInd,
            int toInd,
            v_of_map& hashMap) {

        // the hash to be updated might already have a value
        int currValue = \
            (hashMap[fromInd].find(diffValue) != hashMap[fromInd].end()) ?
            hashMap[fromInd][diffValue] : 0;

        if (hashMap[toInd].find(diffValue) != hashMap[toInd].end()) {
            hashMap[fromInd][diffValue] = max(hashMap[toInd][diffValue] + 1, currValue);
        } else {
            hashMap[fromInd][diffValue] = max(currValue, 2);
        }
    }

public:
    int longestArithSeqLength(vector<int>& A) {
        int N = A.size();
        v_of_map hashMap(N, map<int, int>());

        int diffValue = 0, maxSeqLength = 0;
        for (int i = N-1; i >= 0; --i) {
            for (int j = i+1; j < N; ++j) {
                diffValue = A[i] - A[j];
                updateMap(diffValue, i, j, hashMap);
                maxSeqLength = max(maxSeqLength, hashMap[i][diffValue]);
            }
        }

        return maxSeqLength;
    }
};


int main() {
    Solution sol;

    vector<int> seq1({3,6,9,12});
    vector<int> seq2({9,4,7,2,10});
    vector<int> seq3({20,1,15,3,10,5,8});
    vector<int> seq4({
        44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,
        20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,
        19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28});
    vector<int> seq5({1,1,1,1});

    cout << "Example 1: " << sol.longestArithSeqLength(seq1) << endl;
    cout << "Example 2: " << sol.longestArithSeqLength(seq2) << endl;
    cout << "Example 3: " << sol.longestArithSeqLength(seq3) << endl;
    cout << "Example 4: " << sol.longestArithSeqLength(seq4) << endl;
    cout << "Example 5: " << sol.longestArithSeqLength(seq5) << endl;

    return 0;
}
