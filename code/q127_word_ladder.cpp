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
 *  Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
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

#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;


class Solution {
private:
    // vector<vector<bool>> transitionMatrix;
    // vector<vector<int>> vec(m, vector<int> (n, 0));

    // void buildMatrixGraph(wordList) {
    // }
    int _wordLength = 0;

    bool isNeighbor(string w1, string w2) {
        int numOfCommonChars = 0;
        for (int i = 0; i < _wordLength; ++i) {
            if (w1[i] == w2[i]) ++numOfCommonChars;
        }
        return numOfCommonChars == (_wordLength - 1);
    }

    bool wordInList(string targetWord, vector<string>& wordList) {
        for (string word: wordList) {
            if (word == targetWord) return true;
        }
        return false;
    }

    // will return a boolean map of neighbors
    vector<bool> findNeighbors(string targetWord, vector<string>& wordList) {
        vector<bool> neighborBoolMap(_wordLength, false);
        for (size_t i = 0 ; i < wordList.size(); ++i) {
            // if (excludeIndex == i) continue;
            if (isNeighbor(targetWord, wordList[i]))
                neighborBoolMap[i] = true;
        }
        return neighborBoolMap;
    }


public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // set the class member _wordLength first
        _wordLength = beginWord.size();

        string currentWord(beginWord);
        vector<bool> visitedWords(_wordLength, false);
        vector<bool> neighborBoolMap(_wordLength, false);

        // first check if endWord is even in the wordList
        if (!wordInList(endWord, wordList)) return 0;

        while (true) {
            neighborBoolMap = findNeighbors(currentWord, wordList);
            for (int i = 0; i < _wordLength; ++i) {
                if (neighborBoolMap[i]) {
                    visitedWords

                }
            }
        }
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
    cout << "For word list:" << endl;
    printVector(wordList1);
    cout << "The ladder length is " << sol.ladderLength("hit", "cog", wordList1) << endl;

    return 0;
}
