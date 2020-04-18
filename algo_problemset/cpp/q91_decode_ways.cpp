#include <set>
#include <string>
#include <vector>

using namespace std;

class Solution {
private:
    set<string> NUMBER_CODES = {
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26"
    };

public:

    int numDecodings(string s) {
        int n = s.length();

        vector<int> hash(n+2, 0);
        hash[n+1] = hash[n] = 1;
        hash[n-1] = (s[n-1] != '0') ? 1 : 0;

        for (int i = n-2; i >= 0; --i) {
            if (NUMBER_CODES.count(s.substr(i, 2)))
                hash[i] += hash[i+2];
            if (s[i] != '0')
                hash[i] += hash[i+1];
        }

        return hash[0];
    }
};
