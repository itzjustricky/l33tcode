/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:

    int getMinStringLength(const vector<string>& strs) {
        size_t n = strs.size();
        size_t minLength = strs[0].length();

        for (size_t i = 1; i < n; ++i) {
            minLength = min(minLength, strs[i].length());
        }

        return minLength;
    }

    bool checkCharacterOnAllStrings(int checkIndex, const vector<string>& strs) {
        size_t n = strs.size();
        char c = strs[0][checkIndex];
        for (size_t i = 0; i < n; ++i) {
            if (strs[i][checkIndex] != c) {
                return false;
            }
        }
        return true;
    }

    string longestCommonPrefix(vector<string>& strs) {
        bool allMatch = true;
        size_t n = strs.size();
        if (n == 0) {
            return "";
        }

        int prefixLength = -1,
            minLength = getMinStringLength(strs);
        while (prefixLength < minLength) {
            allMatch = checkCharacterOnAllStrings(prefixLength+1, strs);
            if (!allMatch) { break; }
            ++prefixLength;
        }
        return strs[0].substr(0, prefixLength+1);
    }

};


int main() {
    Solution sol;

    vector<string> strs = {
        "abcdefgh",
        "abc",
        "ab",
        "abcd",
        "abcde",
    };

    string prefix = sol.longestCommonPrefix(strs);
    cout << "The longest common prefix is " << prefix << endl;

    return 0;
}
