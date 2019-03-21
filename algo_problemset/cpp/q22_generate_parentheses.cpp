/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <vector>
#include <utility>
#include <functional>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <iostream>

using namespace std;


// simple hash for pairs
struct pair_hash {
    template <class T1, class T2>
    size_t operator () (const pair<T1,T2> &p) const {
        auto h1 = hash<T1>{}(p.first);
        auto h2 = hash<T2>{}(p.second);
        return h1 ^ h2;
    }
};


class Solution {

private:
    unordered_map<pair<int, int>, vector<string>, pair_hash> _cacheMap;

    /*
     * n: number of left parenthesis allowed
     * m: number of right parenthesis allowed
     */
    vector<string> generateParenthesis(int n, int m) {
        vector<string> tmpVector;
        vector<string> validParenthesis;

        auto it = _cacheMap.find(make_pair(n, m));
        if (it != _cacheMap.end()) return _cacheMap[make_pair(n, m)];

        if (n == 0)
            return {string(m, ')')};
        if (m == 0) {
            tmpVector = generateParenthesis(n-1, m+1);
            for (string s: tmpVector) {
                validParenthesis.push_back('(' + s);
            }
            return validParenthesis;
        }

        tmpVector = generateParenthesis(n-1, m+1);
        for (string s: tmpVector)
            validParenthesis.push_back('(' + s);

        tmpVector = generateParenthesis(n, m-1);
        for (string s: tmpVector)
            validParenthesis.push_back(')' + s);

        _cacheMap[make_pair(n, m)] = validParenthesis;
        return validParenthesis;
    }


public:
    vector<string> generateParenthesis(int n) {
        return generateParenthesis(n, 0);
    }
};


template<class T>
void print_vector(vector<T> vect) {
    for (T x : vect) {
        cout << x << ' ';
    }
    cout << '\n';
}


int main() {
    Solution sol;

    vector<string> parens = sol.generateParenthesis(3);
    print_vector(parens);

    return 0;
}
