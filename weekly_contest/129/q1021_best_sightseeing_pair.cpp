#include <vector>

using namespace std;


class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int N = A.size();

        int maxLowerPair = 0, maxPairScore = 0;
        for (int i = 1; i < N; ++i) {
            maxLowerPair = max(maxLowerPair-1, A[i-1] - 1);
            maxPairScore = max(maxPairScore, A[i] + maxLowerPair);
        }

        return maxPairScore;
    }
};
