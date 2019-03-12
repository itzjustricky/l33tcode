/*
 *  Description:
 *      Find longest
 *
 *      Given a string that consists of only uppercase English letters, you can replace
 *      any letter in the string with another letter at most k times. Find the length
 *      of a longest substring containing all repeating letters you can get after
 *      performing the above operations.
 *
 *      Note: Both the string's length and k will not exceed 104.
 *
 */

#include <list>
#include <iostream>
#include <algorithm>
#include <unordered_map>


using namespace std;

class Solution {

private:
    string _alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    unordered_map<char, list<int>> _leftIndexLists;
    unordered_map<char, list<int>> _valueLists;

    unordered_map<char, int> _valueMap;
    unordered_map<char, int> _costMap;

    void initState() {
        int alphabetLen = _alphabet.length();

        _valueMap.reserve(alphabetLen);
        _costMap.reserve(alphabetLen);
        _leftIndexLists.reserve(alphabetLen);
        _valueLists.reserve(alphabetLen);

        for (char c: _alphabet) {
            _leftIndexLists.emplace(c, list<int>());
            _valueLists.emplace(c, list<int>());
            _valueMap[c] = 0;
            _costMap[c] = 0;
        }
    }

    void updateState(char c, int leftIndex, int contigCount, int k) {
        list<int> & leftIndexList = _leftIndexLists[c];
        list<int> & valueList = _valueLists[c];

        int costToAdd = leftIndexList.size() > 0 ?
            (leftIndex - leftIndexList.back() - valueList.back()) : 0;
        int currCost = _costMap[c] + costToAdd,
            currValue = _valueMap[c];

        leftIndexList.push_back(leftIndex); valueList.push_back(contigCount);

        auto indexPtr = leftIndexList.begin();
        auto valuePtr = valueList.begin();
        ++indexPtr;

        int prevIndex = leftIndexList.front(), tmpCost = 0;
        while ((currCost > k) && (indexPtr != leftIndexList.end())) {
            tmpCost =  *indexPtr - (prevIndex + *valuePtr);

            // update cost and value
            currCost -= tmpCost;
            currValue -= (*valuePtr + tmpCost);
            prevIndex = *indexPtr;

            ++indexPtr; ++valuePtr;
            leftIndexList.pop_front(); valueList.pop_front();
        }

        if (costToAdd > k) {
            _costMap[c] = 0;
            _valueMap[c] = contigCount;
        } else {
            _costMap[c] = currCost;
            _valueMap[c] = currValue + contigCount + costToAdd;
        }
    }

public:

    int characterReplacement(string s, int k) {
        initState();

        int maxLength = 0, stringLength = s.length(),
            contigCount = 1, leftIndex = 0;
        // set some dummy variables outside the alphabet
        char c = '?', nextChar = '?';

        int leftSpace = 0, rightSpace = 0, extraSpace = 0;

        for (int i = 0; i < stringLength; ++i) {
            c = s[i];
            nextChar = (i == stringLength) ? '?' : s[i+1];

            if (c == nextChar) {
                contigCount += 1;
            } else {
                updateState(c, leftIndex, contigCount, k);

                if (_costMap[c] < k) {
                    leftSpace = _leftIndexLists[c].front() - 0;
                    rightSpace = stringLength - (_leftIndexLists[c].back() + contigCount);
                    extraSpace = min(k - _costMap[c], leftSpace + rightSpace);
                } else {
                    extraSpace = 0;
                }

                maxLength = max(maxLength, _valueMap[c] + extraSpace);
                leftIndex = i + 1; contigCount = 1;
            }
        }

        return maxLength;
    }
};


int main() {

    Solution sol;
    // expected 4
    // cout << "Answer for s=ABAB & k=2." << endl;
    // cout << sol.characterReplacement("ABAB", 2) << endl;

    // expected 4
    // cout << "Answer for s=AABABBA & k=1." << endl;
    // cout << sol.characterReplacement("AABABBA", 1) << endl;

    // expected 8
    // cout << "Answer for s=ABABABBBBABABABAC & k=2." << endl;
    // cout << sol.characterReplacement("ABABABBBBABABABAC", 2) << endl;

    // expected 14
    // cout << "Answer for s=ABABABBBBABABABAC & k=5." << endl;
    // cout << sol.characterReplacement("ABABABBBBABABABAC", 5) << endl;

    // expected 19
    // cout << "Answer for s=ABABABBBBAAAAAAABAABABA & k=7." << endl;
    // cout << sol.characterReplacement("ABABABBBBAAAAAAABAABABA", 7) << endl;

    // expected 9
    // cout << "Answer for s=ABABABBBB & k=7." << endl;
    // cout << sol.characterReplacement("ABABABBBB", 7) << endl;

    // expected 5
    cout << "Answer for s=BAAAB & k=2." << endl;
    cout << sol.characterReplacement("BAAAB", 2) << endl;

    // expected 7
    cout << "Answer for s=KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF & k=4." << endl;
    cout << sol.characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4) << endl;

    // expected 11
    cout << "Answer for s=EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH & k=7" << endl;
    cout << sol.characterReplacement("EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH", 7) << endl;

    return 0;
}
