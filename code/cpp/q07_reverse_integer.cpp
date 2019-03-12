/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <cmath>
#include <climits>
#include <iostream>

using namespace std;

class Solution {
public:

    int reverse(int x) {
        size_t reversed_x = 0;

        // determine sign and adjust x to be positive
        int sign = 1;
        if (x >= 0) { sign = 1; }
        else { sign = -1; }
        x *= sign;

        int numOfDecimals = log10(x);
        for (int i = 0; i <= numOfDecimals; ++i) {
            reversed_x = (10 * reversed_x) + (x % 10);
            if (reversed_x > INT_MAX) { return 0; }
            x /= 10;
        }

        return reversed_x * sign;
    }
};


int main() {
    Solution sol;

    cout << sol.reverse(123) << endl;
    cout << sol.reverse(-123) << endl;

    return 0;
}
