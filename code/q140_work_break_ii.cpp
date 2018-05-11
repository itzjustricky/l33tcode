/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <tuple>
#include <stack>
#include <vector>
#include <iostream>
#include <unordered_map>
// #include <unordered_map>

using namespace std;

class Solution {


private:
    // typedef vector<vector<string>> vvs;

    // map from the start index (on 's') to vector of valid sentences
    // starting from string 's' at start index
    unordered_map<int, vector<string>> wordHash;

    bool isInHash(int index) {
        return (wordHash.find(index) != wordHash.end());
    }

public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        return wordBreak(s, wordDict, 0);
    }

    vector<string> wordBreak(string s, vector<string>& wordDict, int start) {

        if (isInHash(start))  return wordHash[start];
        if (start == int(s.size())) return vector<string>();

        vector<string> validSentences, storedSentences;
        // vector<string> storedSentences;

        string word = "";
        stack<pair<int, int>> trackerStack;
        // populate the stack, where first letter of word matches letter in
        // 's' at position 'start'
        for (size_t i = 0; i < wordDict.size(); ++i) {
            word = wordDict[i];
            if (word[0] == s[start]) {
                cout << "Inserting word " << word << " into stack." << endl;
                trackerStack.emplace(make_pair(i, 0));
            }
        }

        cout << "Stack has size of " << trackerStack.size() << "." << endl << endl;
        int stringIter = start + 1;
        int wordIndex = 0, letterIndex = 0;
        while (!trackerStack.empty()) {
            tie(wordIndex, letterIndex) = trackerStack.top();
            trackerStack.pop();
            ++letterIndex;

            word = wordDict[wordIndex];

            cout << "Trying to match word " << word << " at position "
                 << letterIndex << " to string " << s << " at position "
                 << stringIter << "." << endl;
            // if word is completely matched
            if (letterIndex == int(word.length())) {
                cout << "Word completed." << endl;
                storedSentences = wordBreak(s, wordDict, letterIndex);
                for (string sentence: storedSentences) {
                    validSentences.emplace_back(word + " " + sentence);
                }
            // or word is still being matched
            } else if (word[letterIndex] == s[stringIter]) {
                cout << "Next letter '" << word[letterIndex] << "' matched." << endl;
                trackerStack.push(make_pair(wordIndex, letterIndex));
            // else word has failed matching so do nothing
            } else {
                cout << "Word did not match." << endl;
            }

            cout << "========================================" << endl;
            ++stringIter;
        }

        wordHash[start] = validSentences;
        return validSentences;
    }

};



int main() {
    Solution sol;

	string s = "catsanddog";
	vector<string> wordDict = {"cat", "cats", "and", "sand", "dog"};
    cout << "The word 's' is '" << s << "'." << endl;
    cout << "The dictionary is [";
    for (string word : wordDict) {
        cout << word << ", ";
    }
    cout << "]." << endl;

    vector<string> validSentences = sol.wordBreak(s, wordDict);

    for (string sentence: validSentences) {
        cout << sentence << endl;
    }

    return 0;
}
