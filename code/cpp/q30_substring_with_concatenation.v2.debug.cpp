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
    int _stringSize;

    int _numOfTotalWords;
    int _numOfUniqueWords;

    int _wordLength;

    // map of <word> => <word index>
    unordered_map<string, int> wordToInt;
    // map of <word index> => <number of word>
    unordered_map<int, int> _wordIndexToCount;
    // map of <index on s> => <word index> (as set in 'wordToInt')
    vector<int> _wordStartHash;

    // Initialize the wordToInt with values
    void initWordMaps(vector<string>& words) {
        wordToInt.clear(); _wordIndexToCount.clear();
        auto inWordToIntMap = [this](string word) {
            return wordToInt.find(word) != wordToInt.end();};
        int i = 0;
        for (string word: words) {
            if (inWordToIntMap(word)) {
                ++_wordIndexToCount[wordToInt[word]];
            } else {
                _wordIndexToCount[i] = 1;
                wordToInt[word] = i; ++i;
            }
        }
    }

    int checkForWord(string s) {
        auto got = wordToInt.find(s);
        return (got == wordToInt.end()) ? -1 : got->second;
    }

    void tryToFreeTracker(
            int startPoint, int wordIndex,
            vector<bool>& tracker,
            vector<int>& timesUsedTracker) {
        int tmpWordIndex = 0;
        int totalWordsUsed = accumulate(
            timesUsedTracker.begin(), timesUsedTracker.end(), 0);

        while (totalWordsUsed > 0) {
            tmpWordIndex = _wordStartHash[startPoint];
            --timesUsedTracker[tmpWordIndex];
            tracker[tmpWordIndex] = false;

            // successfully freed wordIndex then just break
            if (tmpWordIndex == wordIndex) break;

            startPoint += _wordLength;
            totalWordsUsed = accumulate(tracker.begin(), tracker.end(), 0);
        }

    }

    void leapSearch(
            int leapStart,
            vector<bool>& doneIndices,
            vector<int>& startIndices) {
        if (doneIndices[leapStart]) return;

        cout << "##################################################" << endl;
        cout << "leap search with leapStart " << leapStart << endl;

        vector<bool> tracker(_numOfUniqueWords, false);
        vector<int> timesUsedTracker(_numOfUniqueWords, 0);

        int indexIter = leapStart,
            wordIndex = _wordStartHash[leapStart],
            startIndex = 0,
            // wordsFilled represents the number of words that is depleted
            wordsFilled = 0,
            totalWordsUsed = 0;

        // a word starts there and it is not repeated
        while (wordIndex != -1) {
            cout << "indexIter: " << indexIter << endl;
            cout << "wordIndex: " << wordIndex << endl;

            doneIndices[indexIter] = true;
            // if trying to use depleted word
            if (tracker[wordIndex]) {
                totalWordsUsed = accumulate(
                    timesUsedTracker.begin(), timesUsedTracker.end(), 0);
                tryToFreeTracker(
                    indexIter - (totalWordsUsed * _wordLength),
                    wordIndex,
                    tracker, timesUsedTracker);
            }

            if (++timesUsedTracker[wordIndex] == _wordIndexToCount[wordIndex])
                tracker[wordIndex] = true;

            wordsFilled = accumulate(tracker.begin(), tracker.end(), 0);
            if (wordsFilled == _numOfUniqueWords) {
                cout << "Found start index " << startIndex << endl;
                startIndex = indexIter - (_numOfTotalWords-1) * _wordLength;
                startIndices.push_back(startIndex);
            }

            indexIter += _wordLength;
            if (indexIter >= _stringSize) break;
            wordIndex = _wordStartHash[indexIter];

        }
        cout << "##################################################" << endl;
    }

    vector<int> findStartIndices() {
        vector<int> startIndices;
        vector<bool> doneIndices(_stringSize, false);
        for (int i = 0; i <= (_stringSize - _wordLength); ++i)
            leapSearch(i, doneIndices, startIndices);

        return startIndices;
    }

public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> startIndices;

        _numOfTotalWords = words.size();
        _stringSize = s.size();
        if ((_stringSize == 0) || (_numOfTotalWords == 0)) return startIndices;

        _wordLength = words[0].size();
        if (_wordLength > _stringSize) return startIndices;

        initWordMaps(words);
        _numOfUniqueWords = wordToInt.size();

        int wordIndex = 0;
        _wordStartHash.resize(_stringSize);
        fill(_wordStartHash.begin(), _wordStartHash.end(), -1);
        for (int i = 0; i <= (_stringSize - _wordLength); ++i) {
            wordIndex = checkForWord(s.substr(i, _wordLength));
            if (wordIndex != -1) {
                cout << "found word " << s.substr(i, _wordLength) << endl;
                cout << "i: " << i << endl;
                cout << "wordIndex: " << wordIndex << endl;
                _wordStartHash[i] = wordIndex;
            }
        }

        startIndices = findStartIndices();
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

    // // Example 2:
    // string s2 = "barfoofoobarthefoobarman";
    // vector<string> words2({"bar","foo","the"});
    // startIndices = sol.findSubstring(s2, words2);
    // cout << "For example 2, found start indices: " << endl;
    // printVector(startIndices);

    // // Example 3:
    // string s3 = "mississippi";
    // vector<string> words3({"mississippis"});
    // startIndices = sol.findSubstring(s3, words3);
    // cout << "For example 3, found start indices: " << endl;
    // printVector(startIndices);

    // // Example 4:
    // string s4 = "wordgoodgoodgoodbestword";
    // vector<string> words4({"word","good","best","good"});
    // startIndices = sol.findSubstring(s4, words4);
    // cout << "For example 4, found start indices: " << endl;
    // printVector(startIndices);

    // // Example 5:
    // string s5 = "a";
    // vector<string> words5({"a"});
    // startIndices = sol.findSubstring(s5, words5);
    // cout << "For example 5, found start indices: " << endl;
    // printVector(startIndices);


    return 0;
}
