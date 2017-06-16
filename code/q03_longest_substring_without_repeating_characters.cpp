/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;


class CharacterTracker {
public:
    unordered_map<char, int> tracker;

    CharacterTracker(int capacity) {
        this->tracker.reserve(capacity);
    }

    void updateMap(string subString) {
        int n = subString.size();
        for (int i = 0; i < n; ++i) {
            this->tracker.erase(subString[i]);
        }
    }

    int& operator[](char key) {
        return this->tracker[key];
    }

    bool contains(char key) {
        return (this->tracker.find(key) != this->tracker.end());
    }

};


class Solution {
public:

    int lengthOfLongestSubstring(string s) {
        int n = s.size();

        CharacterTracker charTracker(26);

        string subString = "";
        int bestLength = 0,                 // to return: length of longest substring
            startToDuplicateLength = 0,     // measures indices b/w substr. start and duplicate
            subStringStart = 0,             // starting index of longest substring
            lengthTmp = 0;                  // to store length of substring when duplicate encountered

        char charIter;
        for (int i = 0; i < n; ++i) {
            charIter = s[i];

            // if duplicate encountered update variables
            if (charTracker.contains(charIter)) {
                lengthTmp = subString.size();
                if (lengthTmp > bestLength) bestLength = lengthTmp;

                startToDuplicateLength = charTracker[charIter] - subStringStart;
                subStringStart = charTracker[charIter] + 1;

                // delete all characters in map from start to duplicate character
                charTracker.updateMap(subString.substr(0, startToDuplicateLength + 1));
                subString = subString.substr(startToDuplicateLength + 1, subString.size());
            }
            subString += charIter;
            charTracker[charIter] = i;
        }

        return bestLength;
    }
};


int main() {

    Solution sol = Solution();

    cout << sol.lengthOfLongestSubstring("abcabcbb") << endl;
    cout << sol.lengthOfLongestSubstring("bbbbb") << endl;
    cout << sol.lengthOfLongestSubstring("pwwkew") << endl;

    return 0;
}
