/*
 * Question 30

    You are given a string, s, and a list of words, words, that are all of the same length.
    Find all starting indices of substring(s) in s that is a concatenation of each word in
    words exactly once and without any intervening characters.

    Example 1:

    Input:
      s = "barfoothefoobarman",
      words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
    The output order does not matter, returning [9,0] is fine too.

    Example 2:
    Input:
      s = "wordgoodstudentgoodword",
      words = ["word","student"]
    Output: []

*/

#include <string>
#include <vector>
#include <numeric>
#include <iostream>
#include <unordered_map>

using namespace std;


template <class T>
void printVector(const vector<T>& v);


class Solution {

private:
    typedef vector<bool> bitmap;

    int _stringSize;
    int _numOfWords;
    int _wordLength;

    // map of <index on s> => <word index>
    unordered_map<int, vector<int>> _wordStartHash;
    unordered_map<string, vector<int>> _wordMap;

    bool inVector(int x, vector<int>& vect) {
        for (int val: vect)
            if (x == val) return true;
        return false;
    }

    vector<int> checkForWord(string s) {
        auto got = _wordMap.find(s);
        return (got == _wordMap.end()) ? vector<int>() : got->second;
    }

    bool inWordMap(string s) {
        auto got = _wordMap.find(s);
        return got != _wordMap.end();
    }

    int getWordIndex(int index, vector<bool>& tracker) {
        vector<int> wordIndices(_wordStartHash[index]);
        for (int i: wordIndices)
            if (!tracker[i]) return i;

        return -1;
    }

    void tryToFreeTracker(int startPoint, int wordIndex, vector<bool>& tracker) {
        int wordsUsed = accumulate(tracker.begin(), tracker.end(), 0);

        while (wordsUsed > 0) {
            vector<int> wordIndices = _wordStartHash[startPoint];

            if (inVector(wordIndex, wordIndices)) {
                tracker[wordIndex] = false;
                break;
            } else {
                for (int x: wordIndices) {
                    if (tracker[x]) {
                        // just strip the first word
                        tracker[x] = false;
                        break;
                    }
                }
            }
            startPoint += _wordLength;
            wordsUsed = accumulate(tracker.begin(), tracker.end(), 0);
        }

    }

    void leapSearch(int leapStart, vector<bool>& doneIndices, vector<int>& startIndices) {
        if (doneIndices[leapStart]) return;

        vector<bool> tracker(_numOfWords, false);
        int indexIter = leapStart,
            wordIndex = getWordIndex(leapStart, tracker),
            startIndex = 0, wordsUsed = 0;

        // a word starts there and it is not repeated
        while (wordIndex != -1) {
            tracker[wordIndex] = true;
            doneIndices[indexIter] = true;

            wordsUsed = accumulate(tracker.begin(), tracker.end(), 0);
            if (wordsUsed == _numOfWords) {
                startIndex = indexIter - (_numOfWords-1) * _wordLength;
                startIndices.push_back(startIndex);
            }

            indexIter += _wordLength;
            if (indexIter >= _stringSize) break;
            wordIndex = getWordIndex(indexIter, tracker);
            // if word is unavailable because it is currently used, try to free it
            if ((wordIndex == -1) && (!_wordStartHash[indexIter].empty())) {
                tryToFreeTracker(
                    indexIter - (wordsUsed * _wordLength),
                    _wordStartHash[indexIter][0], tracker);
                wordIndex = getWordIndex(indexIter, tracker);
            }
        }
    }

    vector<int> findCompleteConcatenations() {
        vector<int> startIndices;
        vector<bool> doneIndices(_stringSize, false);
        for (int i = 0; i <= (_stringSize - _wordLength); ++i)
            leapSearch(i, doneIndices, startIndices);

        return startIndices;
    }

public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> startIndices;

        _stringSize = s.size();
        _numOfWords = words.size();
        if ((_stringSize == 0) || (_numOfWords == 0)) return startIndices;

        _wordLength = words[0].size();
        if (_wordLength > _stringSize) return startIndices;

        _wordMap.reserve(_numOfWords);
        _wordStartHash.reserve(s.size());
        for (int i = 0; i < _numOfWords; ++i) {
            if (inWordMap(words[i])) _wordMap[words[i]].push_back(i);
            else _wordMap[words[i]] = vector<int>(1, i);
        }

        // first populate the _hashMap class member
        vector<int> wordIndices;
        for (size_t i = 0; i <= (s.size() - _wordLength); ++i) {
            wordIndices = checkForWord(s.substr(i, _wordLength));
            if (wordIndices.size() > 0) _wordStartHash[i] = wordIndices;
        }

        // then search for the successful concatenations
        startIndices = findCompleteConcatenations();
        return startIndices;
    }
};


template <class T>
void printVector(const vector<T>& v) {
    for (auto x : v) {
        cout << x << " ";
    }
    cout << endl;
}


int main() {

    Solution sol;
    vector<int> startIndices;

    // Example 1:
    string s1 = "barfoothefoobarman";
    vector<string> words1({"foo","bar"});
    startIndices = sol.findSubstring(s1, words1);
    cout << "For example 1, found start indices: " << endl;
    printVector(startIndices);

    // Example 2:
    string s2 = "barfoofoobarthefoobarman";
    vector<string> words2({"bar","foo","the"});
    startIndices = sol.findSubstring(s2, words2);
    cout << "For example 2, found start indices: " << endl;
    printVector(startIndices);

    // Example 3:
    string s3 = "mississippi";
    vector<string> words3({"mississippis"});
    startIndices = sol.findSubstring(s3, words3);
    cout << "For example 3, found start indices: " << endl;
    printVector(startIndices);

    // Example 4:
    string s4 = "wordgoodgoodgoodbestword";
    vector<string> words4({"word","good","best","good"});
    startIndices = sol.findSubstring(s4, words4);
    cout << "For example 4, found start indices: " << endl;
    printVector(startIndices);

    // Example 5:
    string s5 = "a";
    vector<string> words5({"a"});
    startIndices = sol.findSubstring(s5, words5);
    cout << "For example 5, found start indices: " << endl;
    printVector(startIndices);


    return 0;
}
