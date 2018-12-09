/*
 *
 *  Given two words (beginWord and endWord), and a dictionary's word list,
 *  find the length of shortest transformation sequence from beginWord to endWord,
 *  such that:
 *      Only one letter can be changed at a time.
 *      Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
 *
 *  Note:
 *      Return 0 if there is no such transformation sequence.
 *      All words have the same length.
 *      All words contain only lowercase alphabetic characters.
 *      You may assume no duplicates in the word list.
 *      You may assume beginWord and endWord are non-empty and are not the same.
 *
 *  Example 1:
 *  Input:
 *  beginWord = "hit",
 *  endWord = "cog",
 *  wordList = ["hot","dot","dog","lot","log","cog"]
 *  Output: 5
 *  Explanation: As one shortest transformation is
 *      "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 *  return its length 5.
 *
 *  Example 2:
 *  Input:
 *  beginWord = "hit"
 *  endWord = "cog"
 *  wordList = ["hot","dot","dog","lot","log"]
 *  Output: 0
 *  Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 *
 *
 * @author: Ricky Chang
 */

#include <queue>
#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;


class Solution {
private:
    int _wordLength = 0;
    int _numOfWords = 0;

    bool isNeighbor(string w1, string w2) {
        int numOfCommonChars = 0;
        for (int i = 0; i < _wordLength; ++i) {
            if (w1[i] == w2[i]) ++numOfCommonChars;
        }
        if (numOfCommonChars == (_wordLength - 1)) {
            cout << "words " << w1 << " and " << w2
                 << " are neighbors " << endl;
        }
        return numOfCommonChars == (_wordLength - 1);
    }

    bool hasTrueValues(vector<bool>& boolMap) {
        int sum = 0;
        for (bool x: boolMap) {
            sum += x;
        }
        return sum > 0;
    }

    bool wordInList(string targetWord, vector<string>& wordList) {
        for (string word: wordList) {
            if (word == targetWord) return true;
        }
        return false;
    }

    // This will manipulate the passed neighborBoolMap
    // it will populate true values into indices corresponding to a neighbor
    void findNeighbors(
            string targetWord,
            vector<bool>& neighborBoolMap,
            vector<string>& wordList,
            vector<bool>& visitedWords) {

        for (int i = 0 ; i < _numOfWords; ++i) {
            // if not visited then check if is neighbor
            if ((!visitedWords[i]) &&
                (!neighborBoolMap[i]) &&
                (isNeighbor(targetWord, wordList[i]))) {
                neighborBoolMap[i] = true;
            }
        }
    }

    // will return a boolean map of neighbors for the passed target-word
    vector<bool> findNeighbors(
            vector<bool>& targetWords,
            vector<string>& wordList,
            vector<bool>& visitedWords) {
        vector<bool> neighborBoolMap(_numOfWords, false);

        for (int i = 0; i < _numOfWords; ++i) {
            if (targetWords[i]) {
                findNeighbors(
                    wordList[i], neighborBoolMap,
                    wordList, visitedWords);
            }
        }
        cout << "//////////////////////////////////////////////////" << endl;
        cout << "For target words: " << endl;
        for (int i = 0; i < _numOfWords; ++i) {
            if (targetWords[i]) cout << wordList[i] << ", ";
        }
        cout << endl;

        cout << "Found neighbors: " << endl;
        for (int i = 0; i < _numOfWords; ++i) {
            if (neighborBoolMap[i]) cout << wordList[i] << ", ";
        }
        cout << endl;
        cout << "//////////////////////////////////////////////////" << endl;

        return neighborBoolMap;
    }


public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // set the class member _numOfWords first
        _wordLength = beginWord.size();
        _numOfWords = wordList.size();

        vector<bool> visitedWords(_numOfWords, false);
        vector<bool> neighborBoolMap(_numOfWords, false);
        findNeighbors(beginWord, neighborBoolMap, wordList, visitedWords);

        // first check if endWord is even in the wordList
        if (!wordInList(endWord, wordList)) return 0;

        int length(1);

        while (hasTrueValues(neighborBoolMap)) {
            ++length;
            cout << "Entered while loop." << endl;

            for (int i = 0; i < _numOfWords; ++i) {
                if (neighborBoolMap[i]) {
                    cout << "visiting word " << wordList[i] << endl;
                    visitedWords[i] = true;

                    if (endWord == wordList[i]) {
                        cout << "returning the length found" << endl;
                        return length;
                    }
                }
            }

            neighborBoolMap = findNeighbors(
                neighborBoolMap, wordList, visitedWords);
        }

        cout << "no path was found" << endl;
        return 0;
    }
};

void printVector(const vector<string>& v) {
    for (auto x : v) {
        cout << x << " ";
    }
    cout << endl;
}

int main() {
    Solution sol = Solution();

    vector<string> wordList1({"hot","dot","dog","lot","log","cog"});
    cout << "For ('hit' => 'cog') and word list:" << endl;
    printVector(wordList1);
    cout << "The ladder length is " << sol.ladderLength("hit", "cog", wordList1) << endl;

    return 0;
}
