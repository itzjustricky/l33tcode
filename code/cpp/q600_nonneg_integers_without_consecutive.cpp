/*
 *
 *
 * @author: Ricky Chang
 */

#include <iostream>
#include <stdexcept>

#include <cmath>
#include <bitset>
#include <unordered_map>

using namespace std;


class Solution {

private:

    // The following map bit array size to valid integer count

    // valid arrays for array ending with zero
    unordered_map<int, int> m_ZeroTailCount;
    // valid arrays for array ending with one
    unordered_map<int, int> m_OneTailCount;
    // all valid arrays
    unordered_map<int, int> m_TotalCount;

    bool isInMap(int num, const unordered_map<int, int>& map) {
        return map.find(num) != map.end();
    }

    // void updateZeroTail(int num)
    int findMostSignificantBit(int num) {
        return floor(log2(num));
    }

    /* Find the number of valid bit arrays that have
     * no consecutive ones with array size numOfBits
     */
    void findIntegersForBitArray(int numOfBits) {
        if (numOfBits < 2) { return; }
        if (isInMap(numOfBits, m_TotalCount)) { return; }

        int rightSplit = numOfBits / 2;
        int leftSplit = numOfBits - rightSplit;

        findIntegersForBitArray(leftSplit);
        findIntegersForBitArray(leftSplit-1);
        findIntegersForBitArray(leftSplit-2);
        findIntegersForBitArray(rightSplit);

        // update the maps
        m_TotalCount[numOfBits] = \
            m_ZeroTailCount[leftSplit] * m_OneTailCount[rightSplit] + \
            m_OneTailCount[leftSplit] * m_ZeroTailCount[rightSplit] + \
            m_ZeroTailCount[leftSplit] * m_ZeroTailCount[rightSplit];
        m_ZeroTailCount[numOfBits] = \
            m_ZeroTailCount[leftSplit-1] * m_TotalCount[rightSplit] + \
            m_OneTailCount[leftSplit-1] * m_ZeroTailCount[rightSplit];
        m_OneTailCount[numOfBits] = \
            m_OneTailCount[leftSplit-1] * m_TotalCount[rightSplit] + \
            m_OneTailCount[leftSplit-2] * m_ZeroTailCount[rightSplit];
    }

    int findRemaining(int num) {
        if (num == 0) { return 0; }
        if (num == 1) { return 2; }

        bitset<50> intBitArray(num);
        int mostSignificantBit = findMostSignificantBit(num);

        int nextActiveBit = -1;
        for (int i = mostSignificantBit-1; i >= 0; --i) {
            if (intBitArray[i] == 1) {
                nextActiveBit = i;
                break;
            }
        }

        if (nextActiveBit == -1) {
            return 1;
        } else if (nextActiveBit == (mostSignificantBit-1)) {
            return m_ZeroTailCount[mostSignificantBit];
        } else {
            return findIntegers(num - exp2(mostSignificantBit));
        }
    }


public:

    Solution() {
        // handle some base cases
        m_ZeroTailCount[2] = 2; m_ZeroTailCount[1] = 1;
        m_ZeroTailCount[0] = 0;
        m_OneTailCount[2] = 1; m_OneTailCount[1] = 1;
        m_OneTailCount[0] = 0;
        m_TotalCount[1] = 2; m_TotalCount[0] = 0;
        m_TotalCount[2] = 3;

    }

    int findIntegers(int num) {
        int mostSignificantBit = findMostSignificantBit(num);
        findIntegersForBitArray(mostSignificantBit);

        return m_TotalCount[mostSignificantBit] + findRemaining(num);
    }
};


int main() {

    Solution sol;
    cout << "The computed answer is: " << sol.findIntegers(100000) << endl;

    return 0;
}
