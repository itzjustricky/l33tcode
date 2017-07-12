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
                              pair2int_map& longestTracker, bool& successFlag) {
        // return cached value
        if (pairInMap(section, longestTracker)) { return longestTracker[section]; }

        int start = section.first,
            end = section.second;
        int start_to_end = end - start;
        int tmpLongest1 = 0, tmpLongest2 = 0;

        if (start_to_end == 0) {
            longestTracker[section] = 1;
        } else if ((start_to_end == 1) &&
                   (s[start] == s[end])) {
            longestTracker[section] = 2;
        } else {
            if (s[start] == s[end]) {
                successFlag = true;
                int_pair newSection = make_pair(start+1, end-1);
                longestTracker[section] = \
                    calcLongestPalindrome(s, newSection, longestSoFar, longestTracker, successFlag);
                longestTracker[section] += successFlag * 2;
                /*
                if ((start_to_end+1) < longestTracker[section]) {
                    cout << "length is violated here: " << endl;
                    cout << "carry: " << carry << endl;
                    cout << "ind: " << start << "-" << end << endl;
                    cout << "substring: " << s.substr(start, start_to_end+1) << endl;
                    cout << "------------------------------" << endl;
                }
                */

            } else {
                successFlag = false;

                const int_pair& newSection1 = make_pair(start+1, end),
                                newSection2 = make_pair(start, end-1);
                tmpLongest1 = calcLongestPalindrome(s, newSection1, longestSoFar, longestTracker, successFlag);
                tmpLongest2 = calcLongestPalindrome(s, newSection2, longestSoFar, longestTracker, successFlag);
                longestTracker[section] = max(tmpLongest1, tmpLongest2);
            }
        }

        if ((start == 20) && (end == 27)) {
            cout << "******************************" << endl;
            cout << "The length for 20-27 is " << longestTracker[section] << endl;
            cout << "THe current longest so far is " << longestTracker[longestSoFar] << endl;
            cout << "******************************" << endl;
        }
        if ((start == 21) && (end == 26)) {
            cout << "******************************" << endl;
            cout << "The length for 21-26 is " << longestTracker[section] << endl;
            cout << "THe current longest so far is " << longestTracker[longestSoFar] << endl;
            cout << "******************************" << endl;
        }

        if (longestTracker[section] > longestTracker[longestSoFar]) {
            longestSoFar = section;

            cout << "------------------------------" << endl;
            cout << "with indices " << longestSoFar.first << "-" << longestSoFar.second << endl;
            cout << "The substring " << s.substr(longestSoFar.first, start_to_end+1) \
                 << " is now the longest substring with length " << longestTracker[section] << endl;
            cout << "Substring actually has length " \
                 << s.substr(longestSoFar.first, start_to_end+1).length() << endl;
            cout << "success flag is " << successFlag << endl;
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
        bool successFlag = false;
        pair2int_map longestTracker;
        longestTracker.reserve(n * n);

        int_pair wholeSection = make_pair(0, n-1);
        int_pair longestSoFar = make_pair(0, -1);
        longestTracker[longestSoFar] = 0;
        // longestTracker
        calcLongestPalindrome(s, wholeSection, longestSoFar, longestTracker, successFlag);

        int substrLength = longestSoFar.second - longestSoFar.first;
        return s.substr(longestSoFar.first, substrLength+1);
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
