/*
 *
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    Example 1:
    Input: [1,3,5,6], 5
    Output: 2

    Example 2:
    Input: [1,3,5,6], 2
    Output: 1

    Example 3:
    Input: [1,3,5,6], 7
    Output: 4

    Example 4:
    Input: [1,3,5,6], 0
    Output: 0
 *
*/

#include <vector>
#include <iostream>

using namespace std;


class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

        // adjusted binary search
        int l_bound = 0, u_bound = nums.size()-1;

        int pos(0);
        do {
            pos = (l_bound + u_bound) / 2;
            if (nums[pos] > target)
                u_bound = pos;
            else
                l_bound = pos;

        } while (l_bound < u_bound);

        return pos;
    }
};

int main() {

    Solution sol;

    // Example 1:
    // Expected Output: 2
    vector<int> nums1({1,3,5,6});
    cout << "Example 1 answer: " << sol.searchInsert(nums1, 5) << endl;

    // Example 2:
    // Expected Output: 1
    vector<int> nums2({1,3,5,6});
    cout << "Example 2 answer: " << sol.searchInsert(nums2, 2) << endl;

    // Example 3:
    // Expected Output: 4
    vector<int> nums3({1,3,5,6});
    cout << "Example 3 answer: " << sol.searchInsert(nums3, 7) << endl;

    // Example 4:
    // Expected Output: 0
    vector<int> nums4({1,3,5,6});
    cout << "Example 4 answer: " << sol.searchInsert(nums4, 0) << endl;


    return 0;
}
