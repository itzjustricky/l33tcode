/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <tuple>
#include <vector>
#include <iostream>
#include <stdexcept>
#include <unordered_map>

using namespace std;


class Solution {

private:

    vector<int> createRange(int start, int end) {
        vector<int> newVector(end-start);
        for (int vi = 0, i = start; i < end; ++i, ++vi) {
            newVector[vi] = i;
        }
        return newVector;
    }

    int argMax(vector<int>& v, int startIndex, int afterIndex=-1) {
        int maxIndex = 0;

        maxIndex = startIndex;
        for (int i = startIndex-1; i > afterIndex; --i) {
            if (v[maxIndex] <= v[i]) maxIndex = i;
        }
        return maxIndex;
    }

    int decideNextInteger(int i1, int i2, vector<int>& v1, vector<int>& v2) {
        int l1 = v1.size(), l2 = v2.size();

        if (v1.size() == 0) return 1;
        else if (v2.size() == 0) return 0;
        else {
            while (v1[i1] == v2[i2]) { ++i1; ++i2; }
            if (i1 == l1) {
                return 1;
            } else if (i2 == l2) {
                return 0;
            } else {
                return (v1[i1] > v2[i2]) ? 0 : 1;
            }
        }
    }

    vector<int> mergeMaxVectors(vector<int>& maxV1, vector<int>& maxV2) {
        int mergeIndex = 0, nextInteger = 0;
        vector<int> mergedVector(maxV1.size() + maxV2.size());

        int i1 = 0, i2 = 0,
            l1 = maxV1.size(), l2 = maxV2.size();
        while (i1 < l1 || i2 < l2) {
            if (i1 == l1) {
                mergedVector[mergeIndex++] = maxV2[i2++];
            } else if (i2 == l2) {
                mergedVector[mergeIndex++] = maxV1[i1++];
            } else {
                nextInteger = decideNextInteger(i1, i2, maxV1, maxV2);
                if (nextInteger == 0) {
                    mergedVector[mergeIndex++] = maxV1[i1++];
                } else {
                    mergedVector[mergeIndex++] = maxV2[i2++];
                }
            }
        }
        return mergedVector;

    }

    bool vectorGreaterThan(vector<int>& v1, vector<int>& v2) {
        if (v1.size() != v2.size())
            throw invalid_argument("The passed vectors 'v1' and 'v2' should be the same size.");
        for (int i = 0; i < int(v1.size()); ++i) {
            if (v1[i] > v2[i]) {
                return true;
            } else if (v1[i] < v2[i]) {
                return false;
            }
        }
        return false;
    }

    vector<int> maxNumberForOneVector(vector<int>& v, int k) {
        int vectorLength = v.size();

        if (k == 0) return {};
        if (vectorLength == k) return v;

        // store the indices of the max numbers
        vector<int> argMaxNumber(createRange(vectorLength-k, vectorLength));
        for (int i = 0; i < k; ++i) {
            if (i == 0) {
                argMaxNumber[i] = argMax(v, argMaxNumber[i]);
            } else {
                argMaxNumber[i] = argMax(v, argMaxNumber[i], argMaxNumber[i-1]);
            }
        }

        int argMaxIter = 0;
        vector<int> maxNumber(k);
        // now convert the indices to values
        for (int i: argMaxNumber) {
            maxNumber[argMaxIter++] = v[i];
        }
        return maxNumber;
    }

public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {

        vector<int> maxV1{}, maxV2{};
        vector<int> maxNumber(k), candidateMax(k);

        int i = 0, j = 0,
            l1 = nums1.size(), l2 = nums2.size();

        j = min(k, l2);
        i = k - j;
        int stopIndex = min(l1, k);

        while (i <= stopIndex) {
            maxV1 = maxNumberForOneVector(nums1, i);
            maxV2 = maxNumberForOneVector(nums2, j);
            candidateMax = mergeMaxVectors(maxV1, maxV2);

            if (vectorGreaterThan(candidateMax, maxNumber)) {
                maxNumber = candidateMax;
            }
            ++i; --j;
        }

        return maxNumber;
    }
};



int main() {

    Solution sol;

    // Example 1:
    // vector<int> nums1 = {3, 4, 6, 5};
    // vector<int> nums2 = {9, 1, 2, 5, 8, 3};
    // int k = 5;
    // should return [9, 8, 6, 5, 3]

    // Example 2:
    // vector<int> nums1 = {6, 7};
    // vector<int> nums2 = {6, 0, 4};
    // int k = 5;
    // should return [6, 7, 6, 0, 4]

    // Example 3:
    // vector<int> nums1 = {3, 9};
    // vector<int> nums2 = {8, 9};
    // int k = 3;
    // should return [9, 8, 9]

    // Example 4:
    // vector<int> nums1 = {3, 4, 6, 5};
    // vector<int> nums2 = {9, 1, 2, 5, 8, 3};
    // int k = 5;

    // Example 5:
    // vector<int> nums1 = {2,5,6,4,4,0};
    // vector<int> nums2 = {7,3,8,0,6,5,7,6,2};
    // int k = 15;
    // should return [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]

    // Example 6:
    vector<int> nums1 = {4,1,2,5,8,5,7,3,7,3,0,5,8,9,5,7,3,3,4,4,0};
    vector<int> nums2 = {7,8,4,8,9,5,0,4,0,8,2};
    int k = 32;
    // should return [7,8,4,8,9,5,4,1,2,5,8,5,7,3,7,3,0,5,8,9,5,7,3,3,4,4,0,4,0,8,2,0]

    vector<int> maxNumber = sol.maxNumber(nums1, nums2, k);
    for (int num: maxNumber) {
        cout << num << ',';
    }
    cout << endl;

    return 0;
}
