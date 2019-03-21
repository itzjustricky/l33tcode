/*
 *
 * Input is guaranteed to be within the range from 1 to 3999.
 *
 * Symbol	I	V	X	L	C	D	M
 * Value	1	5	10	50	100	500	1,000
 *
 * Number	4	9	40	90	400	900
 * Notation	IV	IX	XL	XC	CD	CM
 *
 *
 * @author: Ricky Chang
*/

#include <map>
#include <iostream>

using namespace std;


class Solution {

private:

    string repeatString(int n, string s) {
        string repeatedString = "";
        for (int i = 0; i < n; ++i) {
            repeatedString += s;
        }
        return repeatedString;
    }

public:

    string intToRoman(int num) {
        static map<int, string> romanNumeralMap = {
            {1000, "M"}, {900, "CM"}, {500, "D"},
            {400, "CD"}, {100, "C"}, {90, "XC"},
            {50, "L"}, {40, "XL"}, {10, "X"},
            {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"},
        };

        string romanSymbol, romanString = "";
        int romanNumeral, numTmp = num,
            numOfChar;

        for (auto rit = romanNumeralMap.rbegin();
             rit != romanNumeralMap.rend(); ++rit) {
            romanNumeral = rit->first;
            romanSymbol = rit->second;

            if (numTmp >= romanNumeral) {
                numOfChar = numTmp / romanNumeral;
                romanString += repeatString(numOfChar, romanSymbol);
                numTmp -= romanNumeral * numOfChar;
            }
        }

        return romanString;
    }
};


int main() {

    Solution sol;
    cout << "The computed answer is " << sol.intToRoman(2343) << endl;

    return 0;
}
