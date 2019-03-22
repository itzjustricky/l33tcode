#include <vector>
#include <iostream>

using namespace std;



class Solution {
    private:
        vector<vector<int>> initCostMap(const vector<int>& a, int k) {
            int N = a.size();
            vector<vector<int>> costMap(k, vector<int>(0, N));

            return costMap;
        }

    public:
        int calculateCost(vector<int>& a, int k) {
            vector<vector<int>> costMap = initCostMap(a, k);

            int N = a.size();
            // for index i, calculates the min cost that can be incurred
            // for subvector spanning from beginning up to index i
            vector<int> minCost(0, N);

            return minCost[N-1];
        }
};



int main() {

    return 0;
}
