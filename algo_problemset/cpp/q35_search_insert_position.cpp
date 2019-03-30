/*
 *
    Given a sorted array and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.

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

        int a = 0, b = nums.size()-1,
            i = 0;
        while ((b - a) > 1) {
            i = (a + b) / 2;
            if (target > nums[i]) a = i;
            else b = i;
        }

        if (target <= nums[a]) return a;
        else if (target <= nums[b]) return b;
        else return b+1;
    }
};


int main() {
    Solution sol;

    vector<int> v({1,3,5,6});
    cout << "1st Solution: " << sol.searchInsert(v, 5) << endl;
    cout << "2nd Solution: " << sol.searchInsert(v, 2) << endl;
    cout << "3rd Solution: " << sol.searchInsert(v, 7) << endl;
    cout << "4th Solution: " << sol.searchInsert(v, 0) << endl;

    return 0;
}
