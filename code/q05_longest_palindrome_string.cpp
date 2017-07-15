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


class Solution {
public:

    // calculate the Palindrome length with s as the center
    string findPalindrome(string s, int startIndex, int rightOffset=0) {
        int n = s.length();
        int leftIter = startIndex,
            rightIter = startIndex + rightOffset,
            length = 0;

        while ((leftIter >= 0) || (rightIter < n)) {
            if (s[leftIter] != s[rightIter]) {
                break;
            }
            --leftIter; ++rightIter;
        }
        // reverse since iters will always overstep by 1
        length = (--rightIter) - (++leftIter) + 1;
        return s.substr(leftIter, length);
    }

    string updateLongest(string s, string candidate) {
        if (candidate.length() > s.length()) {
            return candidate;
        } else {
            return s;
        }
    }

    string longestPalindrome(string s) {
        int n = s.length();
        string longest = "",
               tmpPalindrome = "";

        // find palindromes with i as center
        for (int i = 0; i < n; ++i) {
            // look for odd length palindrome
            tmpPalindrome = findPalindrome(s, i, 0);
            longest = updateLongest(longest, tmpPalindrome);
            // look for even length palindrome
            tmpPalindrome = findPalindrome(s, i, 1);
            longest = updateLongest(longest, tmpPalindrome);
        }

        return longest;
    }

};


int main() {
    Solution sol;
    string s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth";
    string longestPalindrome = sol.longestPalindrome(s);
    cout << "The calculated answer is: " << longestPalindrome << endl;

    return 0;
}
