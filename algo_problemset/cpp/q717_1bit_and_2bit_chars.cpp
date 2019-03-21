/*
 * Question 717:

    We have two special characters. The first character can be represented by one bit 0.
    The second character can be represented by two bits (10 or 11).
    Now given a string represented by several bits. Return whether the last character
    must be a one-bit character or not. The given string will always end with a zero.

    Example 1:
        Input:
        bits = [1, 0, 0]
        Output: True
        Explanation:
        The only way to decode it is two-bit character and one-bit character.
        So the last character is one-bit character.

    Example 2:
        Input:
        bits = [1, 1, 1, 0]
        Output: False
        Explanation:
        The only way to decode it is two-bit character and two-bit character.
        So the last character is NOT one-bit character.

    Note:
    1. 1 <= len(bits) <= 1000.
    2. bits[i] is always 0 or 1.
 *
*/

#include <vector>
#include <iostream>

using namespace std;

template <class T>
void printVector(vector<T> v);


class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int i = 0, n = bits.size();
        // represent last character used, {1: 1-bit char, 0: 2-bit char}
        bool prevChar(0);

        while (i < n) {
            // if starts with 0, must use 1-bit character
            if (bits[i] == 0) {
                i += 1; prevChar = 1;
                // if starts with 1, must use 2-bit character
            } else {    // i == 1
                i += 2; prevChar = 0;
            }
        }
        return prevChar;
    }
};


template <class T>
void printVector(vector<T> v) {
    for (auto x: v) {
        cout << x << ' ';
    }
    cout << endl;
}

string convertBool(bool x) {
    return x ? "true" : "false";
}


int main() {

    Solution sol;
    vector<int> bits1({1, 0, 0});
    vector<int> bits2({1, 1, 1, 0});

    cout << "For bits: "; printVector(bits1);
    cout << "answer is: " << convertBool(sol.isOneBitCharacter(bits1)) << endl;

    cout << "For bits: "; printVector(bits2);
    cout << "answer is: " << convertBool(sol.isOneBitCharacter(bits2)) << endl;

    return 0;
}
