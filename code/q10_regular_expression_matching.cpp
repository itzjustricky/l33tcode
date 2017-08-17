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

#include <stack>
#include <tuple>
// #include <unordered_map>

using namespace std;

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
        vector<string> subExpressions;
        string tmpString;

        int n = p.size();
        for (int i = 0; i < n; ++i) {
            if (p[i] == '*') {
                if (subExpressions.empty()) {
                    throw invalid_argument(
                        "Invalid pattern, no letter passed before '*'");
                } else {
                    tmpString = subExpressions.back() + '*';
                    subExpressions.pop_back();
                    subExpressions.push_back(tmpString);
                }
            } else {
                subExpressions.push_back(string(1, p[i]));
            }
        }
        return subExpressions;
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

public:

    bool isMatch(string s, string p) {
        clearExploreStack();

        vector<string> subExpressions = parseRegexPattern(p);
        int n1 = s.size(), n2 = subExpressions.size(),
            charPtr = 0, exprPtr = 0;

        string subExpr; char c;
        while (true) {
            // either only one of char or expr reaches end
            if ((charPtr == n1) != (exprPtr == n2)) {
                // TODO: this needs to be thought about ...
                // to take care of cases like ab, ab.*
                if ((charPtr == n1) && (exprPtr == n2-1)) {
                    return isStarPattern(subExpressions[exprPtr]);
                }

                if (m_ExploreStack.empty()) { return false; }
                else { tie(charPtr, exprPtr) = popExploreStack(); }
            }
            if ((charPtr == n1) && (exprPtr == n2)) {
                return true;
            }
            c = s[charPtr];
            subExpr = subExpressions[exprPtr];

            if (isStarPattern(subExpr)) {
                if (patternMatches(subExpr[0], c)) {
                    // add non-deterministic path to stack
                    if (charPtr < n1) { m_ExploreStack.emplace(charPtr+1, exprPtr); }
                    // explore continuation of both
                    ++exprPtr; ++charPtr;
                } else {
                    // skip star pattern since character does not match
                    ++exprPtr;
                }
            } else {
                if (patternMatches(subExpr[0], c)) {
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
    // "bbbba"
    // ".*a*a"

    string s = "a";
    string p = "ab*";

    Solution sol;
    if (sol.isMatch(s, p)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
