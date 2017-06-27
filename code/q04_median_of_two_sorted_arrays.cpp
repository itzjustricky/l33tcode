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
        int n_mid = n / 2;
        int m_mid = m / 2;
        int num1 = nums1[n_mid], num2 = nums2[m_mid];

        // if n ==
        if (total == 1) {
            return n > m ? nums1[0] : nums2[0];
        }

        if (k == (total / 2)) {
            // something
            // if (
        } else if (k < (total / 2)) {
            if (num1 <= num2) {
                nums2 = subset_vector(0, m/2 - 1, nums2);
            } else {
                nums1 = subset_vector(0, n/2 - 1, nums1);
            }
        } else {  // k > (total / 2)
            // TODO
            if (num1 <= num2) {
                nums2 = subset_vector(0, m/2 - 1, nums2);
            } else {
                nums1 = subset_vector(0, n/2 - 1, nums1);
            }
        }

        return findKthLargest(nums1, nums2, k);
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
