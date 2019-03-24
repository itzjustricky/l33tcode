/*

    1020. Partition Array Into Three Parts With Equal Sum My SubmissionsBack to Contest


    Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

    Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])


    Example 1:

    Input: [0,2,1,-6,6,-7,9,1,2,0,1]
    Output: true
    Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
    Example 2:

    Input: [0,2,1,-6,6,7,9,-1,2,0,1]
    Output: false
    Example 3:

    Input: [3,3,6,5,-2,2,5,1,-9,4]
    Output: true
    Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


    Note:

    3 <= A.length <= 50000
    -10000 <= A[i] <= 10000
*/


#include <vector>
#include <iostream>

using namespace std;


class Solution {

private:

    vector<int> cumSum(const vector<int>& A) {
        int N = A.size();
        vector<int> cumSumA(N, 0);

        cumSumA[0] = A[0];
        for (int i = 1; i < N; ++i)
            cumSumA[i] = cumSumA[i-1] + A[i];

        return cumSumA;
    }

    bool canEqualPartition(const vector<int>& cumSum, int target, int startInd) {

        int N = cumSum.size();
        for (int i = startInd+1; i < N-1; ++i) {
            if (((cumSum[i] - cumSum[startInd]) == target) &&
                ((cumSum[N-1] - cumSum[i]) == target))
                return true;
        }
        return false;
    }

public:
    bool canThreePartsEqualSum(vector<int>& A) {

        int N = A.size();
        if (N < 3) return false;

        vector<int> cumSumA(cumSum(A));
        if ((cumSumA[N-1] % 3) != 0) return false;

        int targetSum = cumSumA[N-1] / 3;
        for (int i = 0; i < N-2; ++i) {
            if ((cumSumA[i] == targetSum) &&
                canEqualPartition(cumSumA, targetSum, i))
                return true;
        }

        return false;
    }
};
