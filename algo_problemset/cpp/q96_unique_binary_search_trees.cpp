#include <unordered_map>

using namespace std;

class Solution {

private:
    unordered_map<int, int> countHash;

    bool isEven(int n) {
        return (n % 2) == 0;
    }

    int recursiveNumTrees(int n) {
        if (n <= 1) return 1;
        if (countHash.find(n) != countHash.end()) return countHash[n];

        // small optimization on reflected splits
        int splitStop = n / 2, cnt = 0;
        for (int i = 0; i < splitStop; ++i)
            cnt += recursiveNumTrees(n-i-1) * recursiveNumTrees(i);

        int tmp = 0;
        if (isEven(n)) cnt = 2 * cnt;
        else {
            tmp = recursiveNumTrees(n/2);
            cnt = 2*cnt + tmp*tmp;
        }

        return countHash[n] = cnt;
    }


public:
    int numTrees(int n) {
        countHash.clear(); countHash.reserve(n);
        return recursiveNumTrees(n);
    }
};
