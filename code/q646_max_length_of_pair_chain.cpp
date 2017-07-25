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


class Solution {

private:

    hash<vector<bool>> vectorHash;
    vector<vector<int>>* m_Pairs;

    vector<int> findReplacePairs(int pairIndex, const vector<int>& pairChain) {
        vector<int> replacePairs;
        vector<int> pair = (*m_Pairs)[pairIndex], pairTmp;

        for (auto pairIter: pairChain) {
            pairTmp = (*m_Pairs)[pairIter];
            if (pairTmp[1] < pair[1]) {

            }

            // (*m_Pairs)[pairIter]
            // replacePairs.append();
        }

    }


public:

    static const int INT_INF = numeric_limits<int>::infinity();

    int findInsertionPoint(int pairIndex, const vector<int>& pairChain) {
        int i = 0, n = pairChain.size();
        vector<int> frontPair = {-INT_INF, -INT_INF},
                    backPair = (*m_Pairs)[0];
        vector<int> pair = (*m_Pairs)[pairIndex];
        do {
            if ((frontPair[1] < pair[0]) && (pair[1] < backPair[0])) {
                return i;
            }
            ++i;
            frontPair = (*m_Pairs)[pairChain[i-1]];
            backPair = (*m_Pairs)[pairChain[i]];
        } while (i < n);

        return (backPair[1] < pair[0]) ? n : -1;
    }


    int _findLongestChain(int start, vector<int> pairChain) {

    }


    int findLongestChain(vector<vector<int>>& pairs) {
        m_Pairs = &pairs;

        vector<int> pairChain;
        // pairChainKey will be used as key to hash map
        // since each pair can only be used once
        vector<bool> pairChainKey(1000, false);
        // unordered_map<int, vector<int>> chainHash;
        // chainHash.reserve(pairs.size());

        for (auto pair: pairs) {

        }

    }
};


int main() {


    return 0;
}
