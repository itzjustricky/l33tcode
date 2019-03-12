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


class Solution {
public:

    typedef pair<int, int> int_pair;
    typedef unordered_map<int_pair, int, int_pair_hash> pair2int_map;
    typedef unordered_map<int_pair, bool, int_pair_hash> pair2bool_map;

    pair2bool_map m_PalindromeTracker;      // tracks which substrings are palindromes
    pair2int_map m_LongestTracker;          // tracks length of longest palindrome within every substr

    bool pairInMap(const int_pair& section, pair2int_map& tracker) {
        auto got = tracker.find(section);
        return (got != tracker.end());
    }

    void searchLeftAndRightSubstring(string s, const int_pair& section, int_pair& longest) {
        int start = section.first,
            end = section.second;

        m_PalindromeTracker[section] = false;
        const int_pair& rightSection = make_pair(start+1, end),
                        leftSection = make_pair(start, end-1);
        m_LongestTracker[section] = max(
            calcLongestPalindrome(s, rightSection, longest),
            calcLongestPalindrome(s, leftSection, longest));
    }

    void searchInnerSubstring(string s, const int_pair& section, int_pair& longest) {
        int start = section.first,
            end = section.second;

        int_pair innerSection = make_pair(start+1, end-1);
        int innerLongest = calcLongestPalindrome(s, innerSection, longest);

        if (m_PalindromeTracker[innerSection]) {
            m_PalindromeTracker[section] = true;
            m_LongestTracker[section] = innerLongest + 2;
        } else {
            searchLeftAndRightSubstring(s, section, longest);
        }
    }

    int calcLongestPalindrome(string s, const int_pair& section, int_pair& longest) {
        // return cached value
        if (pairInMap(section, m_LongestTracker)) { return m_LongestTracker[section]; }

        int start = section.first, end = section.second;
        int startToEnd = end - start;
        int longestLength;

        // base case if substring length is 2 and composed of same characters
        if ((startToEnd == 1) && (s[start] == s[end])) {
            m_LongestTracker[section] = 2;
            m_PalindromeTracker[section] = true;
        } else {
            if (s[start] == s[end]) {
                searchInnerSubstring(s, section, longest);
            } else {
                searchLeftAndRightSubstring(s, section, longest);
            }
        }

        longestLength = longest.second - longest.first;
        if (m_LongestTracker[section] > m_LongestTracker[longest]) {
            longest = section;
        }

        return m_LongestTracker[section];
    }

    string longestPalindrome(string s) {
        size_t n = s.length();
        if (n == 0) {
            return 0;
        }

        m_LongestTracker.clear(); m_PalindromeTracker.clear();
        m_PalindromeTracker.reserve(n * n); m_LongestTracker.reserve(n * n);
        // start by initializing every character in string into m_LongestTracker
        int_pair pairTmp;
        for (int i = 0; i < int(n); ++i) {
            pairTmp = make_pair(i, i);
            m_LongestTracker[pairTmp] = 1;
            m_PalindromeTracker[pairTmp] = true;
        }
        int_pair wholeSection = make_pair(0, n-1);
        int_pair longest = make_pair(0, 0);
        calcLongestPalindrome(s, wholeSection, longest);

        int substrLength = longest.second - longest.first;
        return s.substr(longest.first, substrLength+1);
    }

};


int main() {
    Solution sol;
    string s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth";
    string longestPalindrome = sol.longestPalindrome(s);
    cout << "The calculated answer is: " << longestPalindrome << endl;

    return 0;
}
