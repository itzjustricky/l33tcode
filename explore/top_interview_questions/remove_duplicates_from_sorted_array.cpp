/*
 *
 *
 *
 *
 * Remove Duplicates from Sorted Array

    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    ========================================
    Example 1:
    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.
    ========================================

    Example 2:
    Given nums = [0,0,1,1,1,2,2,3,3,4],

    Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

    It doesn't matter what values are set beyond the returned length.
    ========================================

    Clarification:

    Confused why the returned value is an integer but your answer is an array?

    Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

    Internally you can think of this:

    // nums is passed in by reference. (i.e., without making a copy)
    int len = removeDuplicates(nums);

    // any modification to nums in your function would be known by the caller.
    // using the length returned by your function, it prints the first len elements.
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }
 */


#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = nums.size();
        if (length <= 1) return length;

        int prevNum = nums[0];
        nums.erase(
            remove_if(
                nums.begin()+1, nums.end(),
                [&prevNum](const int& x) {
                    if (x == prevNum) { return true; }
                    else { prevNum = x; return false; }
                }
            ),
            nums.end());
        return nums.size();
    }
};


void printVector(vector<int>& v) {
    for (int x: v)
        cout << x << ' ';
    cout << '\n';
}


int main() {

    Solution sol;

    vector<int> nums1({1,1,2});
    cout << "original: "; printVector(nums1);
    cout << "new length is " << sol.removeDuplicates(nums1) << endl;
    printVector(nums1);

    vector<int> nums2({0,0,1,1,1,2,2,3,3,4});
    cout << "original: "; printVector(nums2);
    cout << "new length is " << sol.removeDuplicates(nums2) << endl;
    printVector(nums2);

    return 0;
}
