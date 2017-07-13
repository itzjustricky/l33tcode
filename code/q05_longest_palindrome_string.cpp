/*
 * Description:
 *
 * TODO:
 *      - algorithm is not calculating all the substring combinations
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


class Solution {
public:

    typedef pair<int, int> int_pair;
    typedef unordered_map<int_pair, int, int_pair_hash> pair2int_map;
    typedef unordered_map<int_pair, bool, int_pair_hash> pair2bool_map;

    bool pairInMap(const int_pair& section, pair2int_map& tracker) {
        auto got = tracker.find(section);
        return (got != tracker.end());
    }

    int calcLongestPalindrome(string s, const int_pair& section, int_pair& longestSoFar,
                              pair2int_map& longestTracker, pair2bool_map& palindromeTracker) {
        // return cached value
        if (pairInMap(section, longestTracker)) { return longestTracker[section]; }

        int start = section.first,
            end = section.second;
        int startToEnd = end - start;
        int longestSoFarLength;

        if ((startToEnd == 1) && (s[start] == s[end])) {
            longestTracker[section] = 2;
            palindromeTracker[section] = true;
        } else {

            if (s[start] == s[end]) {
                int_pair newSection = make_pair(start+1, end-1);
                longestTracker[section] = \
                    calcLongestPalindrome(s, newSection, longestSoFar, longestTracker, palindromeTracker);

                if (palindromeTracker[newSection]) {
                    longestTracker[section] += 2;
                    palindromeTracker[section] = true;
                } else {
                    palindromeTracker[section] = false;

                    const int_pair& newSection1 = make_pair(start+1, end),
                                    newSection2 = make_pair(start, end-1);
                    longestTracker[section] = max(
                        calcLongestPalindrome(s, newSection1, longestSoFar, longestTracker, palindromeTracker),
                        calcLongestPalindrome(s, newSection2, longestSoFar, longestTracker, palindromeTracker));

                }

                // the section below could hit cache ... which then may lead it to falsely
                // believe all the ones below are also palindromes
                // longestTracker[section] += isPalindrome * 2;
            } else {
                palindromeTracker[section] = false;

                const int_pair& newSection1 = make_pair(start+1, end),
                                newSection2 = make_pair(start, end-1);
                longestTracker[section] = max(
                    calcLongestPalindrome(s, newSection1, longestSoFar, longestTracker, palindromeTracker),
                    calcLongestPalindrome(s, newSection2, longestSoFar, longestTracker, palindromeTracker));
            }
        }

        longestSoFarLength = longestSoFar.second - longestSoFar.first;

        if (longestTracker[section] > longestTracker[longestSoFar]) {
            longestSoFar = section;
        }

        return longestTracker[section];
    }

    string longestPalindrome(string s) {
        size_t n = s.length();
        if (n == 0) {
            return 0;
        }
        // mapping of (start index, end index) => length
        // tracks longest palindrome of substrs of string s
        pair2int_map longestTracker;
        // tracks which substrings are actually palindromes
        pair2bool_map palindromeTracker;

        // start by initializing every character in string into longestTracker
        for (int i = 0; i < int(n); ++i) {
            longestTracker[make_pair(i, i)] = 1;
        }

        palindromeTracker.reserve(n * n);
        longestTracker.reserve(n * n);

        int_pair wholeSection = make_pair(0, n-1);
        int_pair longestSoFar = make_pair(0, 0);
        // longestTracker
        calcLongestPalindrome(s, wholeSection, longestSoFar, longestTracker, palindromeTracker);

        int substrLength = longestSoFar.second - longestSoFar.first;
        return s.substr(longestSoFar.first, substrLength+1);
    }

};


int main() {
    Solution sol;
    string s = "afblalbacbdefaaabbbbaaaaa";
    string correctAnswer = "aaabbbbaaa";
    // string s = "bcxbaaabyz";
    // string correctAnswer = "baaab";

    string longestPalindrome = sol.longestPalindrome(s);
    cout << "The calculated answer is: " << longestPalindrome << endl;
    cout << "The correct answer is: " << correctAnswer << endl;

    return 0;
}
