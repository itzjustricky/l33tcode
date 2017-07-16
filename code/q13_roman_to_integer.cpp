/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <cassert>
#include <iostream>

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:

    int accumulate(const vector<int> values) {
        int sum = 0;
        for (auto val: values) {
            sum += val;
        }
        return sum;
    }

    int symbolToInt(char c) {
        static unordered_map<char, int> roman2intMap = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}
        };

        return roman2intMap[c];
    }

    void accumSubtractiveNotation(vector<int>& values) {
        size_t n = values.size();
        for (size_t i = 1; i < n; ++i) {
            if (values[i-1] < values[i]) {
                values[i] -= values[i-1];
                values[i-1] = 0;
            }
        }
    }

    int romanToInt(string s) {
        size_t n = s.length();

        vector<int> values(n);

        for (size_t i = 0; i < n; ++i) {
            values[i] = symbolToInt(s[i]);
        }
        accumSubtractiveNotation(values);
        return accumulate(values);
    }
};


int main() {

    Solution sol;
    cout << "The calculated answer is " << sol.romanToInt("DCXXI") << endl;

    return 0;
}
