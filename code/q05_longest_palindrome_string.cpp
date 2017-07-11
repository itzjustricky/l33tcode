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
        // since string will be maximum of size 1000
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

    int calcLongestPalindrome(string s, const int_pair& section, int_pair& longestSoFar,
                              pair2int_map& longestTracker, int carry=0) {
        int start = section.first,
            end = section.second;
        int start_to_end = end - start;
        if (start_to_end == 0) {
            longestTracker[section] = carry + 1;
        } else if ((start_to_end == 1) &&
                   (s[start] == s[end])) {
            longestTracker[section] = carry + 2;
        }

        if (pairInMap(section, longestTracker)) { return longestTracker[section]; }
        if (s[start] == s[end]) {
            int_pair newSection = make_pair(start+1, end-1);
            longestTracker[section] = \
                calcLongestPalindrome(s, newSection, longestSoFar, longestTracker, carry+2);
        } else {
            const int_pair& newSection1 = make_pair(start+1, end),
                            newSection2 = make_pair(start, end-1);
            longestTracker[section] = \
                max(calcLongestPalindrome(s, newSection1, longestSoFar, longestTracker),
                    calcLongestPalindrome(s, newSection2, longestSoFar, longestTracker));
        }

        if (longestTracker[section] > longestTracker[longestSoFar]) {
            cout << "The substring " << s.substr(longestSoFar.first, longestSoFar.second+1) \
                 << " is now the longest substring" << endl;

            longestSoFar = section;
        }
        return longestTracker[section];
    }

    string longestPalindrome(string s) {
        size_t n = s.length();
        if (n == 0) {
            return 0;
        }
        // longestTracker tracks longest palindrome of substrs of string s
        // mapping of (start index, end index) => length
        pair2int_map longestTracker;
        longestTracker.reserve(n * n);

        int_pair wholeSection = make_pair(0, n);
        int_pair longestSoFar = make_pair(0, 0);
        calcLongestPalindrome(s, wholeSection, longestSoFar, longestTracker);

        return s.substr(longestSoFar.first, longestSoFar.second+1);
    }

};


int main() {
    Solution sol;
    string s = "afblalbacbdefaaaaaaaabbbbbbaaaaaaaaaa";
    string correctAnswer = "aaaaaaaabbbbbbaaaaaaaa";
    string longestPalindrome = sol.longestPalindrome(s);
    cout << "The longest length is: " << longestPalindrome << endl;
    cout << "The correct answer is: " << correctAnswer << endl;

    return 0;
}
