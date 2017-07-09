/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <iostream>
#include <vector>

using namespace std;


vector<int> subset_vector(int start_index, int end_index, vector<int>& vect) {
    auto start = vect.begin() + start_index;
    auto end = vect.begin() + end_index;

    vector<int> subvector(start, end);
    return subvector;
}


class Solution {
public:
    double findKthLargest(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size(), m = nums2.size();
        int total = n + m;

        // return findKthLargest(nums1, nums2, k);
        return 0.0;
    }


    // handle base case when the smaller vector is of length 1
    vector<int> handleBaseCase(vector<int>& nums1, vector<int>& nums2) {

    }


    // utility used for update vector
    // not sure if this should be function signature
    vector<int> updateVector(vector<int>& nums, bool midIsLarger, int k) {
        int n = nums.size();
        int midIndex = getMidElement(nums);
    }


    // The middle element is n/2 when vector is even
    //                       n/2+1 when vector is odd
    // where n is the size of the vector
    int getMidElement(vector<int>& nums) {
        int n = nums.size();
        return ((n%2) == 0) ?  n/2 : n/2+1;
    }


    // order the vectors so that the smaller one is first
    void orderVectors() {

    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        int total = n + m;
        if ((total % 2) == 0) {
            return (findKthLargest(nums1, nums2, total/2) +
                    findKthLargest(nums1, nums2, total/2 + 1)) / 2.0;
        } else {
            return findKthLargest(nums1, nums2, total/2);
        }
    }
};


int main() {
    vector<int> nums1 = {1, 2};
    vector<int> nums2 = {3, 4};

    Solution sol = Solution();
    cout << sol.findMedianSortedArrays(nums1, nums2) << endl;

    return 0;
}
