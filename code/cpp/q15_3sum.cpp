/*
 *  Description:
 * Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
 * Find all unique triplets in the array which gives the sum of zero.
 *
 * Note: The solution set must not contain duplicate triplets.
 *
 *
 */

#include <iostream>

#include <vector>
#include <unordered_map>

using namespace std;


class Solution {

private:
    unordered_map<int, int> sumMap;

    bool inSumMap(int i) {
        auto it = sumMap.find(i);
        return (it != sumMap.end());
    }

    vector<vector<int>> twoSum(vector<int>& nums, int target, int start_index) {
        int numsLength = nums.size(), val = 0;
        vector<vector<int>> validPairs;

        sumMap.clear(); sumMap.reserve(numsLength-start_index);
        for (int i = start_index; i < numsLength; ++i) {
            val = nums[i];
            if (inSumMap(val))
                validPairs.push_back(vector<int>({sumMap[val], val}));
            sumMap[target-val] = val;
        }
        return validPairs;
    }

public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int val = 0;
        vector<vector<int>> validTriplets, numsSubset,
                            twoSumVector, tmpVector;

        for (size_t i = 0; i < nums.size(); ++i) {
            val = nums[i];

            twoSumVector = twoSum(nums, 0-val, i+1);
            for (vector<int> v: twoSumVector) {
                v.insert(v.begin(), val);
                validTriplets.push_back(v);
            }
        }

        return validTriplets;
    }
};


template<class T>
void print_vector(vector<T> vect) {
    for (T x: vect) {
        cout << x << ' ';
    }
    cout << '\n';
}


template<class T>
void print2DVector(vector<vector<T>> vect) {
    for (vector<T> row: vect) {
        cout << '[';
        for (T x: row) cout << x << ' ';
        cout << "]\n";
    }
    cout << '\n';
}


int main() {

    Solution sol;
    vector<int> nums({-1, 0, 1, 2, -1, -4});

    cout << "For nums:" << endl; print_vector(nums);
    cout << "Solution is:" << endl;
    vector<vector<int>> answer(sol.threeSum(nums));

    print2DVector(answer);

    return 0;
}
