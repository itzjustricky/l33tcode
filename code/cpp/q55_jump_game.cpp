/*
 *
 *
 *
 *  Given an array of non-negative integers, you are initially positioned at the first index of the array.
 *  Each element in the array represents your maximum jump length at that position.
 *  Determine if you are able to reach the last index.
 *
 *  Example 1:
 *  Input: [2,3,1,1,4]
 *  Output: true
 *  Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
 *
 *  Example 2:
 *  Input: [3,2,1,0,4]
 *  Output: false
 *  Explanation: You will always arrive at index 3 no matter what. Its maximum
 *               jump length is 0, which makes it impossible to reach the last index.
*/

#include <cmath>
#include <iostream>

#include <vector>
#include <unordered_map>

using namespace std;

void printVector(vector<int> vect);


class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size(), jumpCount = 0;
        vector<int> jumpTracker(n, 0);
        // index '0' is the starting point
        jumpTracker[0] = 1;

        for (int i = 0; i < n; ++i) {
            if (jumpTracker[i] == 0) continue;

            jumpCount = nums[i];
            for (int j = i+1; j <= min(i + jumpCount, n-1); ++j)
                ++jumpTracker[j];
        }
        return jumpTracker[n-1] > 0;
    }
};


void printVector(vector<int> vect) {
    for (int x : vect) {
        cout << x << ' ';
    }
    cout << '\n';
}


int main() {
    Solution sol;

    // first test vector
    vector<int> nums({2, 3, 1, 1, 4});
    cout << "For array: "; printVector(nums);
    if (sol.canJump(nums)) cout << "can jump" << endl;
    else cout << "cannot jump" << endl;

    // second test vector
    vector<int> nums2({3, 2, 1, 0, 4});
    cout << "For array: "; printVector(nums2);
    if (sol.canJump(nums2)) cout << "can jump" << endl;
    else cout << "cannot jump" << endl;

    // second test vector
    vector<int> nums3({0,2,3});
    cout << "For array: "; printVector(nums3);
    if (sol.canJump(nums3)) cout << "can jump" << endl;
    else cout << "cannot jump" << endl;

    return 0;
}
