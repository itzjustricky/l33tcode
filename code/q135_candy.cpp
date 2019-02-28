/*
 *
 *
   There are N children standing in a line. Each child is assigned a rating value.

   You are giving candies to these children subjected to the following requirements:

   Each child must have at least one candy.
   Children with a higher rating get more candies than their neighbors.
   What is the minimum candies you must give?

   Example 1:

   Input: [1,0,2]
   Output: 5
   Explanation:
        You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
   Example 2:

   Input: [1,2,2]
   Output: 4
   Explanation:
        You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
        The third child gets 1 candy because it satisfies the above two conditions.
 *
 *
 */


#include <iostream>

#include <vector>
#include <unordered_map>

using namespace std;


enum Condition {
    lte,    // less than or equal to, or is at a boundary (0 or N)
            // <= and boundary are treated the same
    gt,     // greater than
};


constexpr unsigned int condition_pair(
        Condition left,
        Condition right) {
    return (left << 16) + right;
}


class Solution {

private:

    unordered_map<int, int> _candyHash;

    Condition decideCondition(vector<int>& ratings, int i, int j) {
        int N = ratings.size();
        if ((j >= N) || (j < 0)) {
            return lte;
        } else if (ratings[i] <= ratings[j]) {
            return lte;
        } else {    // ratings[i] > ratings[j]
            return gt;
        }
    }

    int recursiveDecideCandy(vector<int>& ratings, int i) {
        auto got = _candyHash.find(i);
        if (got != _candyHash.end()) return got->second;

        Condition leftCon = decideCondition(ratings, i, i-1),
                  rightCon = decideCondition(ratings, i, i+1);

        switch(condition_pair(leftCon, rightCon)) {
            case condition_pair(lte, lte):
                return _candyHash[i] = 1;
            case condition_pair(gt, lte):
                return _candyHash[i] = 1 + recursiveDecideCandy(ratings, i-1);
            case condition_pair(lte, gt):
                return _candyHash[i] = 1 + recursiveDecideCandy(ratings, i+1);
            case condition_pair(gt, gt):
                return _candyHash[i] = 1 + max(
                    recursiveDecideCandy(ratings, i-1),
                    recursiveDecideCandy(ratings, i+1));
        }
        // it will never reach here
        return 0;
    }

public:
    int candy(vector<int>& ratings) {
        int N = ratings.size(), totalCandy = 0;
        _candyHash.clear(); _candyHash.reserve(N);

        for (int i = 0; i < N; ++i) {
            totalCandy += recursiveDecideCandy(ratings, i);
        }
        return totalCandy;
    }
};


int main() {

    Solution sol;

    // Example 1:
    vector<int> ranking1({1,0,2});
    cout << "Computed answer " << sol.candy(ranking1) << " for example 1." << endl;

    // Example 2:
    vector<int> ranking2({1,2,2});
    cout << "Computed answer " << sol.candy(ranking2) << " for example 2." << endl;

    // Example 3:
    vector<int> ranking3({2,3,6,4,3,2,1,8,3,10});
    // expected answer is 23
    cout << "Computed answer " << sol.candy(ranking3) << " for example 3." << endl;

    return 0;
}
