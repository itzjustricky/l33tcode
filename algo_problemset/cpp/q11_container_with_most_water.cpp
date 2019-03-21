/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <vector>
#include <iostream>

using namespace std;


class Solution {

public:
    int maxArea(vector<int>& height) {
        int maxArea = 0, n = height.size(),
            left = 0, right = n-1;

        auto calcArea = [&height] (int left, int right) {
            return (right-left) * min(height[left], height[right]);
        };

        while (left != right) {
            maxArea = max(calcArea(left, right), maxArea);
            if (height[left] < height[right]) { ++left; }
            else { --right; }
        }

        return maxArea;
    }
};


int main() {

    Solution sol;
    vector<int> heights = {2, 5, 9, 23, 10, 3, 5};
    cout << "Calculated solution is " << sol.maxArea(heights) << endl;

    return 0;
}
