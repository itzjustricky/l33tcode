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

        _valueMap.clear(); _costMap.clear();
        _leftIndexLists.clear(); _valueLists.clear();

        _valueMap.reserve(alphabetLen);
        _costMap.reserve(alphabetLen);
        _leftIndexLists.reserve(alphabetLen);
        _valueLists.reserve(alphabetLen);

        for (char c: _alphabet) {
            _leftIndexLists.emplace(c, list<int>(1, 0));
            _valueLists.emplace(c, list<int>(1, 0));
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

        cout << "updating state for character " << c << endl;
        cout << "with leftIndexList size: " << leftIndexList.size() << endl;
        cout << "with leftIndexList back: " << leftIndexList.back() << endl;
        cout << "with costToAdd: " << costToAdd << endl;
        cout << "with leftIndex: " << leftIndex << endl;
        cout << "with contigCount: " << contigCount << endl;

        auto indexPtr = leftIndexList.begin();
        auto valuePtr = valueList.begin();
        ++indexPtr; ++valuePtr;

        int prevIndex = leftIndexList.front(),
            tmpCost = 0;
        while ((currCost > k) && (indexPtr != leftIndexList.end())) {
            tmpCost =  *indexPtr - (prevIndex + *valuePtr);

            cout << "currCost " << currCost << " is higher than k (" << k << ")" << endl;
            cout << "prevIndex: " << prevIndex << endl;
            cout << "value: " << *valuePtr << endl;
            // cout << "index: " << indexPtr << endl;

            // update cost and value
            currCost -= tmpCost;
            currValue -= (*valuePtr + tmpCost);

            prevIndex = *indexPtr;

            ++indexPtr; ++valuePtr;
            leftIndexList.pop_front(); valueList.pop_front();
        }
        leftIndexList.push_back(leftIndex);
        valueList.push_back(contigCount);

        // if after removing all previous contiguous values and cost is
        // still higher than 'k' then ...
        if (currCost > k) {
            _costMap[c] = 0;
            _valueMap[c] = contigCount;
        // can connect to previous contiguous values
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

        for (int i = 0; i < stringLength; ++i) {
            c = s[i];
            nextChar = (i == stringLength) ? '?' : s[i+1];

            cout << "Running for character: " << c << endl;

            if (c == nextChar) {
                contigCount += 1;
            } else {
                updateState(c, leftIndex, contigCount, k);
                maxLength = max(maxLength, _valueMap[c]);

                cout << "maxLength is now " << maxLength << endl;

                leftIndex = i + 1; contigCount = 1;
            }
            cout << "##############################" << endl;
        }

        cout << "Checking right tail." << endl;

        // check for cases where the cost is not exhausted for some letters
        // and we can add additional letters to right tail
        int availableToAdd = 0;
        for (char c: _alphabet) {
            // the distance b/w the right tail of letter and end of string
            availableToAdd = \
                 stringLength - (_leftIndexLists[c].back() + _valueLists[c].back());

            cout << "c: " << c << endl;
            cout << "cost: " << _costMap[c] << endl;
            cout << "value: " << _valueMap[c] << endl;
            if (_costMap[c] < k) {
                maxLength = max(
                    maxLength,
                    _valueMap[c] + min(k - _costMap[c], availableToAdd));
                cout << "maxLength is now " << maxLength << endl;
            }
            cout << "##############################" << endl;
        }

        return maxLength;
    }
};


int main() {

    Solution sol;
    // cout << "Answer for s=ABAB & k=2." << endl;
    // cout << sol.characterReplacement("ABAB", 2) << endl;

    // cout << "Answer for s=AABABBA & k=1." << endl;
    // cout << sol.characterReplacement("AABABBA", 1) << endl;

    // cout << "Answer for s=ABABABBBBABABABAC & k=2." << endl;
    // cout << sol.characterReplacement("ABABABBBBABABABAC", 2) << endl;

    // cout << "Answer for s=ABABABBBBABABABAC & k=5." << endl;
    // cout << sol.characterReplacement("ABABABBBBABABABAC", 5) << endl;

    // cout << "Answer for s=ABABABBBBAAAAAAABAABABA & k=7." << endl;
    // cout << sol.characterReplacement("ABABABBBBAAAAAAABAABABA", 7) << endl;

    // cout << "Answer for s=ABABABBBB & k=7." << endl;
    // cout << sol.characterReplacement("ABABABBBB", 7) << endl;

    // cout << "Answer for s=BAAAB & k=2." << endl;
    // cout << sol.characterReplacement("BAAAB", 2) << endl;

    cout << "Answer for s=KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF & k=4." << endl;
    cout << sol.characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4) << endl;

    return 0;
}
