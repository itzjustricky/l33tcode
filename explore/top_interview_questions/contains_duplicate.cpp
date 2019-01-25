/*
 * Contains Duplicate

    Given an array of integers, find if the array contains any duplicates.

    Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

    Example 1:

    Input: [1,2,3,1]
    Output: true
    Example 2:

    Input: [1,2,3,4]
    Output: false
    Example 3:

    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true
 *
*/


#include <vector>
#include <iostream>
#include <unordered_map>
#include <unordered_set>


using namespace std;


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        auto inMap = [](int num, unordered_set<int>& numSet) {
            return numSet.find(num) != numSet.end();
        };
        unordered_set<int> tracker;
        tracker.reserve(nums.size());

        for (int num: nums) {
            if (inMap(num, tracker)) return true;
            else tracker.insert(num);
        }
        return false;
    }
};


int main() {
    Solution sol;

    vector<int> nums1({1,2,3,1});
    vector<int> nums2({1,2,3,4});
    vector<int> nums3({1,1,1,3,3,4,3,2,4,2});

    cout << "nums1 contains "
         << (sol.containsDuplicate(nums1) ? "duplicates" : "no duplicates") << endl;
    cout << "nums2 contains "
         << (sol.containsDuplicate(nums2) ? "duplicates" : "no duplicates") << endl;
    cout << "nums3 contains "
         << (sol.containsDuplicate(nums3) ? "duplicates" : "no duplicates") << endl;

    return 0;
}
