/*
 *
 *
 * @author: Ricky Chang
 */

#include <limits>
#include <iostream>

#include <vector>
#include <unordered_map>

using namespace std;


struct vector_hash {
    static const hash<vector<bool>> hasher;

    size_t operator() (const vector<int>& v) const {
        static vector<bool> boolVector(1000, false);
        fill(boolVector.begin(), boolVector.end(), false);  // reset all to false
        for (int x : v) {
            boolVector[x] = true;
        }
        return hasher(boolVector);
    }
};

class Solution {

private:

    typedef unordered_map<vector<int>, int, vector_hash> chain2int_map;
    static const int INT_INF = numeric_limits<int>::infinity();

    int m_TotalPairCount;
    chain2int_map m_ChainHash;
    vector<vector<int>>* m_Pairs;

    vector<int> replacePairs(int start, int end, int replacementPair, const vector<int>& pairChain) {
        vector<int> newChain = pairChain;
        newChain.erase(newChain.begin() + start, newChain.begin() + end);
        newChain.insert(newChain.begin() + start, replacementPair);
        return newChain;
    }

    int findLargestSmallerPair(const vector<int>& pair, const vector<int>& pairChain, int startIndex=0) {
        int n = pairChain.size(), i = startIndex;
        vector<int> pairIter = {-INT_INF, -INT_INF};
        if (i != 0) { pairIter = (*m_Pairs)[pairChain[i]]; }

        // assumes all pairs before startIndex are smaller
        while (pair[0] > pairIter[1]) {
            ++i; if (i == n) { break; }
            pairIter = (*m_Pairs)[pairChain[i]];
        }
        return i-1;
    }


    int findSmallestLargerPair(const vector<int>& pair, const vector<int>& pairChain, int startIndex=0) {
        int n = pairChain.size(), i = startIndex;
        vector<int> pairIter = {-INT_INF, -INT_INF};
        if (i != 0) { pairIter = (*m_Pairs)[pairChain[i]]; }

        // assumes all pairs before startIndex are smaller
        while (pair[1] < pairIter[0]) {
            ++i; if (i == n) { break; }
            pairIter = (*m_Pairs)[pairChain[i]];
        }
        return i-1;
    }

    bool canInsert(int insertIndex, const vector<int>& pair, const vector<int>& pairChain) {
        static vector<int> frontPair, backPair;
        frontPair = (*m_Pairs)[pairChain[insertIndex]];
        backPair = (*m_Pairs)[pairChain[insertIndex+1]];
        return ((pair[0] > frontPair[1]) && (pair[1] < backPair[0]));
    }

    int _findLongestChain(int startIndex, vector<int> pairChain) {
        vector<int> pairIter, newChain;
        int longestChain = 0,
            largestSmallerPair = 0,
            smallestLargerPair = 0;

        for (int i = startIndex; i < m_TotalPairCount; ++i) {
            pairIter = (*m_Pairs)[i];
            largestSmallerPair = findLargestSmallerPair(pairIter, pairChain);

            if (canInsert(largestSmallerPair, pairIter, pairChain)) {
                ++longestChain;
                pairChain.insert(pairChain.begin() + largestSmallerPair, i);
            } else {
                smallestLargerPair = findSmallestLargerPair(pairIter, pairChain, largestSmallerPair);
                newChain = replacePairs(largestSmallerPair, smallestLargerPair, i, pairChain);
                // explore two different chain options
                longestChain += max(_findLongestChain(i+1, pairChain),
                                    _findLongestChain(i+1, newChain));
            }
        }

        return longestChain;
    }


public:

    int findLongestChain(vector<vector<int>>& pairs) {
        m_Pairs = &pairs;
        m_TotalPairCount = pairs.size();

        vector<int> pairChain(m_TotalPairCount);
        return _findLongestChain(0, pairChain);
    }
};


int main() {

    vector<vector<int>> pairs = {
        {1, 2}, {4, 5}, {8, 9},
        {-1, 0}, {10, 12}, {3, 10},
    };

    Solution sol;
    cout << "The longest chain is " << sol.findLongestChain(pairs) << endl;


    return 0;
}
