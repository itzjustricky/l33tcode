/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <utility>
#include <iostream>
#include <unordered_map>

using namespace std;

// TODO fix to return a string instead of length ...
class Solution {
public:

    typedef pair<int, int> int_pair;
    typedef unordered_map<int_pair, int> pair2int_map;

    int calcLongestPalindrome(string s, int_pair& section, pair2int_map& longestTracker) {
        int start = section.first,
            end = section.second;
        if ((start-end) == 1) {
            return 1;
        }

        if (s[start] == s[end]) {
            int_pair newSection = make_pair(start+1, end-1);
            longestTracker[section] = \
                calcLongestPalindrome(s, newSection, longestTracker) \
                + 2;
        } else {
            int_pair newSection1 = make_pair(start+1, end),
                     newSection2 = make_pair(start, end-1);
            longestTracker[section] = max(
                calcLongestPalindrome(s, newSection1, longestTracker),
                calcLongestPalindrome(s, newSection2, longestTracker));
        }

        return longestTracker[section];
    }

    string longestPalindrome(string s) {
        int n = s.length();
        if (n == 0) {
            return 0;
        }
        // longestTracker tracks longest palindrome of substrs of string s
        // mapping of (start index, end index) => length
        pair2int_map longestTracker;
        longestTracker.reserve(n * n);

        int_pair wholeSection = make_pair(0, n);
        int longestLength = calcLongestPalindrome(s, wholeSection, longestTracker);
        return longestLength;
    }

};


int main() {
    string s = "";

    return 0;
}
