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


struct int_pair_hash {
    size_t operator() (const pair<int, int>& intPair) const {
        return intPair.first + intPair.second * 1000;
    }
};


// TODO fix to return a string instead of length ...
class Solution {
public:

    typedef pair<int, int> int_pair;
    typedef unordered_map<int_pair, int, int_pair_hash> pair2int_map;

    bool pairInMap(const int_pair& section, pair2int_map& tracker) {
        auto got = tracker.find(section);
        return (got != tracker.end());
    }

    int calcLongestPalindrome(string s, const int_pair& section, pair2int_map& longestTracker) {
        int start = section.first,
            end = section.second;
        // cout << start << "," << end << endl;
        if ((end-start) == 0) {
            return 1;
        } else if ((end-start) == 1) {
            if (s[start] == s[end]) {
                return 2;
            } else {
                return 0;
            }
        }

        if (pairInMap(section, longestTracker)) { return longestTracker[section]; }
        if (s[start] == s[end]) {
            int_pair newSection = make_pair(start+1, end-1);
            longestTracker[section] = \
                calcLongestPalindrome(s, newSection, longestTracker) \
                + 2;
        } else {
            const int_pair& newSection1 = make_pair(start+1, end),
                            newSection2 = make_pair(start, end-1);
            longestTracker[section] = \
                max(calcLongestPalindrome(s, newSection1, longestTracker),
                    calcLongestPalindrome(s, newSection2, longestTracker));
        }

        return longestTracker[section];
    }

    // string longestPalindrome(string s) {
    int longestPalindrome(string s) {
        size_t n = s.length();
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
    Solution sol;
    string s = "abcdefghijka";
    int longestLength = sol.longestPalindrome(s);
    cout << "The longest length is: " << longestLength << endl;

    return 0;
}
