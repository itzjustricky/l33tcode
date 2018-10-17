/*
 *  Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
 *  You have the following 3 operations permitted on a word:
 *    Insert a character
 *    Delete a character
 *    Replace a character
 */

#include <utility>
#include <vector>
#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;


int getNextSmallestBit(int x) {
    return x ^ (x-1);
}


// delete the bit located at bitIndex (little endian)
int deleteBit(int x, int bitIndex) {
    return x ^ (1 << bitIndex);
}


class Solution {

private:

    typedef vector<int> vi;
    pair<vi, vi> match_letters(string word1, string word2) {
        // these 2 vectors should store integer representations of bit maps
        vector<int> v1, v2;

        char c1('?'), c2('?');
        int wordSize1 = word1.length(), wordSize2 = word2.length(),
            jStartIndex = 0;

        int indexMap1(0), indexMap2(0);
        for (int i = 0; i < wordSize1; ++i) {
            indexMap1 = 0; indexMap2 = 0;

            c1 = word1[i];
            for (int j = jStartIndex; j < wordSize2; ++j) {
                c2 = word2[i];
                if (c1 == c2) {
                    indexMap1 &= (1 << i);
                    indexMap2 &= (1 << j);
                    // v1.push_back(i); v2.push_back(j);
                    // jStartIndex = j + 1;
                    // break;
                }
            }

            if (indexMap1 != 0) {
                v1.push_back(indexMap1); v2.push_back(indexMap2);
            }
        }

        return make_pair(v1, v2);
    }

    // TODO
    int minDistanceForDisjointWords(const string& word1,
                                    const string& word2,
                                    int startIndex1, int endIndex1,
                                    int startIndex2, int endIndex2) {

        int word_size1 = endIndex1 - startIndex1,
            word_size2 = endIndex2 - startIndex2;

        // if word_size1 >
        return 0;
    }

public:
    int minDistance(string word1, string word2) {

    }
};


void print_vector(vector<int> vect) {
    for (int x : vect) {
        cout << x << ' ';
    }
    cout << '\n';
}


int main() {
    Solution sol;
    cout << "Min distance for 'horse', 'ros' "
         << sol.minDistance("horse", "ros") << endl;

    return 0;
}
