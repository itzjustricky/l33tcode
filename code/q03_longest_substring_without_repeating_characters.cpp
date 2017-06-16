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
            cout << "deleting " << subString[i] << endl;
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
        cout << "==============================" << endl;

        CharacterTracker charTracker(26);

        int bestLength = 0, lengthTmp;
        int startToDuplicateLength = 0;
        int subStringStart = 0;  // starting index of longest substring
        string subString = "";

        char charIter;
        for (int i = 0; i < n; ++i) {
            charIter = s[i];

            // if character in map update character tracker and substring
            if (charTracker.contains(charIter)) {
                cout << "Encountered duplicate via " << charIter << endl;
                cout << "Currently substring is " << subString << endl << endl;

                lengthTmp = subString.size();
                if (lengthTmp > bestLength) bestLength = lengthTmp;

                startToDuplicateLength = charTracker[charIter] - subStringStart;
                cout << "From start to duplicate length " << startToDuplicateLength << endl;
                cout << "Character location " << charTracker[charIter] << endl;
                subStringStart = charTracker[charIter];
                // delete all characters in map from start to duplicate character
                charTracker.updateMap(subString.substr(0, startToDuplicateLength + 1));
                subString = subString.substr(startToDuplicateLength + 1, subString.size());
                cout << "==============================" << endl;
            }
            subString += charIter;
            charTracker[charIter] = i;
            // longestSubstring += charIter;
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
