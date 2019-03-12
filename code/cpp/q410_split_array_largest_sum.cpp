/*
 * Question 410: Split Array Largest Sum
 * Difficulty: Hard

    Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

    Note:
    If n is the length of array, assume the following constraints are satisfied:

    1 ≤ n ≤ 1000
    1 ≤ m ≤ min(50, n)
    Examples:

    Input:
    nums = [7,2,5,10,8]
    m = 2

    Output:
    18

    Explanation:
    There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8],
    where the largest sum among the two subarrays is only 18.
 *
 */


#include <vector>
#include <numeric>
#include <iostream>
#include <algorithm>

using namespace std;


class Solution {
private:

    bool validLargestSum(int largestSum, int allowedCuts, const vector<int>& nums) {
        int numsSize = nums.size(),
            accmTracker = 0, cutsUsed = 0;

        for (int i = 0; i < numsSize; ++i) {
            if (nums[i] > largestSum) return false;

            accmTracker += nums[i];
            if (accmTracker > largestSum) {
                accmTracker = nums[i];
                if (++cutsUsed > allowedCuts) return false;
            }
        }

        return true;
    }

    int binarySearchMinLargestSum(
            int start, int end,
            int allowedCuts,
            const vector<int>& nums) {
        int largestSum = (start + end) / 2;
        while ((end - start) > 1) {
            if (validLargestSum(largestSum, allowedCuts, nums))
                end = largestSum;
            else
                start = largestSum;

            largestSum = (start + end) / 2;
        }
        return validLargestSum(start, allowedCuts, nums) ? start : end;
    }

public:
    int splitArray(vector<int>& nums, int m) {
        int numsSize = nums.size();

        long long numSum = (numsSize > 0) ? nums[0] : 0;
        int maxNum = (numsSize > 0) ? nums[0] : 0;
        for (int i = 1; i < numsSize; ++i) {
            numSum += nums[i];
            maxNum = max(maxNum, nums[i]);
        }

        if (numsSize == m) return maxNum;
        // sum_of_elems = std::accumulate(vector.begin(), vector.end(), 0);
        return binarySearchMinLargestSum(
            maxNum, numSum, m-1, nums);
    }
};


int main() {

    Solution sol;

    int m1 = 2;
    vector<int> nums1({7,2,5,10,8});
    cout << "The largest sum for test 1 is: " << sol.splitArray(nums1, m1) << endl;

    int m2 = 5;
    vector<int> nums2({2,3,1,2,4,3});
    cout << "The largest sum for test 2 is: " << sol.splitArray(nums2, m2) << endl;

    return 0;
}
