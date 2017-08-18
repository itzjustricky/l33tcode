/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <vector>
#include <iostream>
#include <stdexcept>

#include <set>
#include <stack>
#include <tuple>
#include <utility>

using namespace std;


void printVector(const vector<string>& v) {
    for (auto x : v) {
        cout << x << " ";
    }
    cout << endl;
}


class Solution {

private:

    stack<tuple<int, int>> m_ExploreStack;


    void clearExploreStack() {
        while (!m_ExploreStack.empty()) {
            m_ExploreStack.pop();
        }
    }

    tuple<int, int> popExploreStack() {
        tuple<int, int> tmpPair = m_ExploreStack.top();
        m_ExploreStack.pop();
        return tmpPair;
    }

    vector<string> parseRegexPattern(string p) {
        vector<string> subPatterns;
        string tmpString;

        int n = p.size();
        for (int i = 0; i < n; ++i) {
            if (p[i] == '*') {
                if (subPatterns.empty()) {
                    throw invalid_argument(
                        "Invalid pattern, no letter passed before '*'");
                } else {
                    tmpString = subPatterns.back() + '*';
                    subPatterns.pop_back();
                    subPatterns.push_back(tmpString);
                }
            } else {
                subPatterns.push_back(string(1, p[i]));
            }
        }
        return collapseStarPatterns(subPatterns);
    }

    bool isStarPattern(string expr) {
        return (expr.size() == 2) && (expr[1] == '*');
    }

    bool patternMatches(char expr, char s) {
        if (expr == '.') {
            return true;
        } else {
            return expr == s;
        }
    }

    /* Reduce the Regex patterns, delete extraneous star patterns
     * while maintaining equivalence in recognized languages.
     */
    vector<string> collapseStarPatterns(const vector<string>& subPatterns) {
        int n = subPatterns.size();
        if (n == 0) { return subPatterns; }

        string prevSubPattern = subPatterns[0], nowSubPattern;
        vector<string> reducedSubPatterns;
        reducedSubPatterns.push_back(subPatterns[0]);

        for (int i = 1; i < n; ++i) {
            nowSubPattern = subPatterns[i];
            if (isStarPattern(nowSubPattern)) {
                if (nowSubPattern != prevSubPattern ) {
                    reducedSubPatterns.push_back(nowSubPattern);
                }
            } else {
                reducedSubPatterns.push_back(nowSubPattern);
            }
            prevSubPattern = nowSubPattern;
        }

        return reducedSubPatterns;
    }

public:

    bool isMatch(string s, string p) {
        clearExploreStack();

        vector<string> subPatterns = parseRegexPattern(p);
        int n1 = s.size(), n2 = subPatterns.size(),
            charPtr = 0, exprPtr = 0;

        string subP; char c;
        while (true) {
            // either only one of char or expr reaches end
            if ((charPtr == n1) != (exprPtr == n2)) {
                if (charPtr == n1) {
                    while (exprPtr != n2) {
                        if (isStarPattern(subPatterns[exprPtr])) { ++exprPtr; }
                        else { break; }
                    }
                    if ((charPtr == n1) && (exprPtr == n2)) { return true; }
                }
                if (m_ExploreStack.empty()) { return false; }
                else { tie(charPtr, exprPtr) = popExploreStack(); }
            }
            if ((charPtr == n1) && (exprPtr == n2)) {
                return true;
            }
            c = s[charPtr];
            subP = subPatterns[exprPtr];

            if (isStarPattern(subP)) {
                if (patternMatches(subP[0], c)) {
                    // add non-deterministic path to stack
                    if (charPtr < (n1-1)) { m_ExploreStack.emplace(charPtr+1, exprPtr); }
                    if (exprPtr < (n2-1)) { m_ExploreStack.emplace(charPtr, exprPtr+1); }
                    // explore continuation of both
                    ++exprPtr; ++charPtr;
                } else {
                    // skip star pattern since character does not match
                    ++exprPtr;
                }
            } else {
                if (patternMatches(subP[0], c)) {
                    ++exprPtr; ++charPtr;
                } else {
                    if (m_ExploreStack.empty()) { return false; }
                    else { tie(charPtr, exprPtr) = popExploreStack(); }
                }
            }

        }   // end of while loop
    }
};


int main() {
    // Time limit exceeded on this one
    string s = "aaaaaaaaaaaaab";
    string p = "a*a*a*a*a*a*a*a*a*a*c";

    // string s = "wxyza";
    // string p = ".*a*a";
    // string s = "a";
    // string p = "ab*";

    Solution sol;
    if (sol.isMatch(s, p)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
