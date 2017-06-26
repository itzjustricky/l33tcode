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


class Solution {
public:
    double findKthLargest(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size(), m = nums2.size();
        int total = n + m;
        int n_mid = n / 2;
        int m_mid = m / 2;

        if (k < (total / 2)) {
            // something
        } else {

        }

        // for ()
        if (nums1[n_mid] > nums2[m_mid]) {
            // something
        } else {
            // something
        }

        return 0.0;
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();

        return 0.0;
    }
};


int main() {

    return 0;
}
