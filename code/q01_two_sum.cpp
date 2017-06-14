
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


bool in_map(int key, unordered_map<int, int> hashMap);


class Solution {

public:

    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res = {0, 0};

        int wantedNum;
        int len = nums.size();
        unordered_map<int, int> sumMap;
        sumMap.reserve(len);

        for (int num: nums){
            wantedNum = target - num;
            if (in_map(wantedNum, sumMap) || in_map(num, sumMap)) {
                res[0] = wantedNum; res[1] = num;
                break;
            } else {
                sumMap[wantedNum] = num;
                sumMap[num] = wantedNum;
            }
        }

        return res;
    }
};


bool in_map(int key, unordered_map<int, int> hashMap) {
    auto found = hashMap.find(key);
    return (found != hashMap.end());
}

void print_vector(vector<int> vect) {
    for (int x : vect) {
        cout << x << endl;
    }
}


int main() {
    Solution sol = Solution();

    // test the solution
    vector<int> nums1 = {3, 4, 8, 23, 12};
    int target1 = 15;

    print_vector(sol.twoSum(nums1, target1));

    return 0;
}
