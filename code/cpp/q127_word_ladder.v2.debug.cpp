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

template <class T>
void printVector(const vector<T>& v);

class Solution {
private:
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
            if (word == targetWord)
                return true;
        }
        return false;
    }

    // This will manipulate the passed neighbors;
    // it will populate the words into neighbors
    void findNeighbors(
            string targetWord,
            vector<string>& neighbors,
            vector<string>& wordList) {

        cout << "##################################################" << endl;
        cout << "finding neighbors for word: " << targetWord << endl;
        vector<int> eraseTargets;
        for (size_t i = 0; i < wordList.size(); ++i) {
            if (isNeighbor(targetWord, wordList[i])) {
                neighbors.push_back(wordList[i]);
                eraseTargets.push_back(i);
                cout << "adding " << wordList[i] << endl;
            }
        }
        cout << "##################################################" << endl;

        for (vector<int>::reverse_iterator i = eraseTargets.rbegin();
             i != eraseTargets.rend(); ++i) {
            wordList.erase(wordList.begin()+*i);
        }
    }

    // will return a boolean map of neighbors for the passed target-word
    vector<string> findNeighbors(
            vector<string>& targetWords,
            vector<string>& wordList) {
        vector<string> neighbors;

        for (string word: targetWords) {
            findNeighbors(word, neighbors, wordList);
        }

        cout << "//////////////////////////////////////////////////" << endl;
        cout << "For target words: " << endl;
        printVector(targetWords);
        cout << "Found neighbors: " << endl;
        printVector(neighbors);
        cout << "//////////////////////////////////////////////////" << endl;

        return neighbors;
    }


public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        _wordLength = beginWord.size();
        vector<string> neighbors;

        // first check if endWord is even in the wordList
        if (!wordInList(endWord, wordList)) return 0;

        findNeighbors(beginWord, neighbors, wordList);

        int length(1);
        while (!neighbors.empty()) {
            cout << "entering while loop" << endl;
            ++length;
            if (wordInList(endWord, neighbors)) {
                cout << "found path to endword" << endl;
                return length;
            }
            neighbors = findNeighbors(neighbors, wordList);
        }
        cout << "no path to endword" << endl;
        return 0;
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
    Solution sol = Solution();

    // vector<string> wordList1({"hot","dot","dog","lot","log","cog"});
    // cout << "For ('hit' => 'cog') and word list:" << endl;
    // printVector(wordList1);
    // cout << "The ladder length is " << sol.ladderLength("hit", "cog", wordList1) << endl;

    vector<string> wordList2({"a","b","c"});
    cout << "For ('a' => 'c') and word list:" << endl;
    printVector(wordList2);
    cout << "The ladder length is "
         << sol.ladderLength("a", "c", wordList2) << endl;


    return 0;
}
