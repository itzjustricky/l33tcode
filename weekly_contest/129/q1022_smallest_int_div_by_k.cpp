/*
 *
 *
    1022. Smallest Integer Divisible by K
    Medium

    Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.
    Return the length of N.  If there is no such N, return -1.

    Example 1:
    Input: 1
    Output: 1
    Explanation: The smallest answer is N = 1, which has length 1.

    Example 2:
    Input: 2
    Output: -1
    Explanation: There is no such positive integer N divisible by 2.

    Example 3:
    Input: 3
    Output: 3
    Explanation: The smallest answer is N = 111, which has length 3.

    Note:
    1 <= K <= 10^5
*/

#include <math.h>
#include <iostream>

using namespace std;


class Solution {
public:
    int smallestRepunitDivByK(int K) {

        if ((K % 2) == 0 || (K % 5) == 0) return -1;

        int remTracker = 0, tenModK = 10 % K;
        int tenRemTracker = 1;
        for (int i = 0; i <= K; ++i) {
            tenRemTracker = (tenRemTracker * tenModK) % K;
            remTracker = ((tenRemTracker % K) + remTracker) % K;
            if (remTracker == 0) return i + 1;
        }

        return -1;
    }
};


int main() {

    Solution sol;
    cout << "Answer for K=1 " << sol.smallestRepunitDivByK(1) << endl;
    cout << "Answer for K=2 " << sol.smallestRepunitDivByK(2) << endl;
    cout << "Answer for K=3 " << sol.smallestRepunitDivByK(3) << endl;

    cout << "Answer for K=17 " << sol.smallestRepunitDivByK(17) << endl;
    cout << "Answer for K=99999 " << sol.smallestRepunitDivByK(99999) << endl;
}
