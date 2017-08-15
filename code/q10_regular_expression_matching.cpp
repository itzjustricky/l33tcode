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

class Solution {

private:

    stack<tuple<int, int>> m_ExploreStack;
    // make use of this
    // maps out where pair (charPtr, exprPtr) have failed
    // set<pair<int, int>> m_FailedMatches;

    void clearExploreStack() {
        while (!m_ExploreStack.empty()) {
            m_ExploreStack.pop();
        }
    }

    // bool hasFailed(int charPtr, int exprPtr) {
    //     if (pa)
    // }

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
        // TODO empty m_ExploreStack and m_FailedMatches here
        clearExploreStack();

        vector<string> subExpressions = parseRegexPattern(p);

        int n1 = s.size(), n2 = subExpressions.size(),
            charPtr = 0, exprPtr = 0;

        string subExpr; char c;
        while (true) {
            if ((charPtr == n1) && (exprPtr == n2)) {
                cout << "entered and branch" << endl;
                return true;
            } else if ((charPtr == n1) || (exprPtr == n2)) {
                cout << "entered or branch" << endl;
                if (m_ExploreStack.empty()) {
                    return false;
                } else {
                    tie(charPtr, exprPtr) = m_ExploreStack.top();
                    m_ExploreStack.pop();
                }
            }

            subExpr = subExpressions[exprPtr];
            c = s[charPtr];
            cout << "Sub expression " << subExpr << endl;
            cout << "Character expression " << c << endl;

            if (isStarPattern(subExpr)) {
                // add non-deterministic path to stack
                cout << subExpr << " is a start pattern" << endl;
                if (patternMatches(subExpr[0], c)) {
                    m_ExploreStack.emplace(charPtr+1, exprPtr);
                    ++charPtr; ++exprPtr;
                } else {    // char for star pattern does not match
                    // must skip star pattern
                    ++exprPtr;
                }
            } else {
                if (patternMatches(subExpr[0], c)) {
                    ++exprPtr; ++charPtr;
                } else {
                    if (m_ExploreStack.empty()) {
                        return false;
                    } else {
                        tie(charPtr, exprPtr) = m_ExploreStack.top();
                        m_ExploreStack.pop();
                    }
                }
            }

        }   // end of while loop
    }
};


int main() {

    string s = "aa";
    string p = ".*";

    Solution sol;
    if (sol.isMatch(s, p)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
