/*
 *
   Given an array, rotate the array to the right by k steps, where k is non-negative.

   Example 1:

   Input: [1,2,3,4,5,6,7] and k = 3
   Output: [5,6,7,1,2,3,4]
   Explanation:
   rotate 1 steps to the right: [7,1,2,3,4,5,6]
   rotate 2 steps to the right: [6,7,1,2,3,4,5]
   rotate 3 steps to the right: [5,6,7,1,2,3,4]
   Example 2:

   Input: [-1,-100,3,99] and k = 2
   Output: [3,99,-1,-100]
   Explanation:
   rotate 1 steps to the right: [99,-1,-100,3]
   rotate 2 steps to the right: [3,99,-1,-100]
   Note:

   Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
   Could you do it in-place with O(1) extra space?
 *
*/

#include <vector>
#include <iostream>

using namespace std;

void printVector(vector<int>& v);


class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int length = nums.size();
        if (length <= 1) return;

        k = k % length;
        for (int i = 0; i < k; ++i) {
            nums.insert(nums.begin(), nums[length-1]);
            nums.erase(nums.end()-1, nums.end());
        }
    }
};


void printVector(vector<int>& v) {
    for (int x: v)
        cout << x << ' ';
    cout << '\n';
}


int main() {
    Solution sol;

    vector<int> nums1({1,2,3,4,5,6,7});
    vector<int> nums2({-1,-100,3,99});

    cout << "original: "; printVector(nums1);
    sol.rotate(nums1, 3);
    cout << "new: "; printVector(nums1);

    cout << "original: "; printVector(nums2);
    sol.rotate(nums2, 2);
    cout << "new: "; printVector(nums2);

    return 0;
}
