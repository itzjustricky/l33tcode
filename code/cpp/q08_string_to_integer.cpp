/*
 *
 *
 * @author: Ricky Chang
 */

#include <climits>
#include <iostream>
#include <unordered_map>

using namespace std;


class Solution {
public:

    int findFirstNonWhiteSpace(string str) {
        int i = 0;
        while (str[i] == ' ') { ++i; }
        return i;
    }

    int processChar(char c) {
        static unordered_map<char, int> ctoiMap(
            {{'0', 0}, {'1', 1}, {'2', 2},
             {'3', 3}, {'4', 4}, {'5', 5},
             {'6', 6}, {'7', 7}, {'8', 8}, {'9', 9}});

        auto it = ctoiMap.find(c);
        if (it != ctoiMap.end()) { return ctoiMap[c]; }
        else { return -1; }
    }

    int myAtoi(string str) {
        size_t i = findFirstNonWhiteSpace(str),
               res = 0;

        // keep track of sign
        bool isNegative = false;
        if (str[i] == '+') { isNegative = false; ++i; }
        else if (str[i] == '-') { isNegative = true; ++i; }

        int intRepr = processChar(str[i]);
        while (intRepr != -1) {
            res = res * 10 + intRepr;
            ++i; intRepr = processChar(str[i]);

            if (res > INT_MAX) {
                return isNegative ? INT_MIN : INT_MAX;
            }
        }

        return res * (isNegative ? -1 : 1);
    }
};


int main() {
    Solution sol = Solution();

    string str = "   +999a999";
    cout << "Result is " << sol.myAtoi(str) << endl;



    return 0;
}
