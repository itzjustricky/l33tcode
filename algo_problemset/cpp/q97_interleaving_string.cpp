#include<tuple>
#include<string>
#include <iostream>
#include<unordered_map>

using namespace std;


class Solution {

private:
    typedef tuple<int, int, int> triplet;

    struct triplet_hash : public std::unary_function<triplet, size_t> {
        size_t operator()(const triplet& k) const {
           return get<0>(k) ^ get<1>(k) ^ get<2>(k);
        }
    };

    unordered_map<triplet, bool, triplet_hash> _hash;

    bool recursiveIsInterleave(
            const string& s1,
            const string& s2,
            const string& s3,
            size_t start1,
            size_t start2,
            size_t start3) {

        if (start3 == s3.length()) return true;
        triplet startPoints = make_tuple(start1, start2, start3);
        if (_hash.find(startPoints) != _hash.end()) return _hash[startPoints];

        bool canInterleave =
            ((start1 < s1.length()) && (s3[start3] == s1[start1])
             && recursiveIsInterleave(s1, s2, s3, start1+1, start2, start3+1))
            ||
            ((start2 < s2.length()) && (s3[start3] == s2[start2])
             && recursiveIsInterleave(s1, s2, s3, start1, start2+1, start3+1));

        return _hash[startPoints] = canInterleave;
    }


public:

    bool isInterleave(string s1, string s2, string s3) {
        _hash.clear();
        if ((s1.length() + s2.length()) != s3.length()) return false;
        return recursiveIsInterleave(s1, s2, s3, 0, 0, 0);
    }
};


int main() {

    Solution sol;
    if (sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
        cout << "Is interleaved!" << endl;
    else
        cout << "Is not interleaved!" << endl;

    return 0;
}
