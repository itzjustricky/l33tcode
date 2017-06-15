#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


class Solution {

public:

    vector<int> twoSum(vector<int>& nums, int target) {
        int num = 0, wantedNum = 0;
        int n = nums.size();
        unordered_map<int, int> sumMap;
        sumMap.reserve(n);

        for (int i = 0; i < n; ++i) {
            num = nums[i];
            if (sumMap.find(num) != sumMap.end()) {
                return {sumMap[num], i};
            }
            wantedNum = target - num;
            sumMap.emplace(wantedNum, i);
        }
    }
};


void print_vector(vector<int> vect) {
    for (int x : vect) {
        cout << x << ' ';
    }
    cout << '\n';
}


int main() {
    Solution sol = Solution();

    // test the solution
    vector<int> nums = {1, 6, 7, 18, 20, 23};
    int target = 13;
    print_vector(sol.twoSum(nums, target));

    return 0;
}
