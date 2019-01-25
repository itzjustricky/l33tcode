/*
 *  Single Number

    Given a non-empty array of integers, every element appears twice except for one. Find that single one.

    Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,1]
    Output: 1
    Example 2:

    Input: [4,1,2,1,2]
    Output: 4
 *
*/


#include <vector>
#include <iostream>


using namespace std;


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int singleNum = 0;
        for (int num: nums)
            singleNum ^= num;
        return singleNum;
    }
};


int main() {
    Solution sol;

    vector<int> nums1{2,2,1};
    vector<int> nums2{4,1,2,1,2};

    cout << "single number for nums1 is " << sol.singleNumber(nums1) << endl;
    cout << "single number for nums2 is " << sol.singleNumber(nums2) << endl;

    return 0;
}
