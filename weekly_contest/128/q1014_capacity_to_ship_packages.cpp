/*
 *
    1014. Capacity To Ship Packages Within D DaysMy SubmissionsBack to Contest
    A conveyor belt has packages that must be shipped from one port to another within D days.

    The i-th package on the conveyor belt has a weight of weights[i].
    Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
    We may not load more weight than the maximum weight capacity of the ship.

    Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.


    Example 1:
    Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
    Output: 15
    Explanation:
    A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
    1st day: 1, 2, 3, 4, 5
    2nd day: 6, 7
    3rd day: 8
    4th day: 9
    5th day: 10

    Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

    Example 2:
    Input: weights = [3,2,2,4,1,4], D = 3
    Output: 6
    Explanation:
    A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
    1st day: 3, 2
    2nd day: 2, 4
    3rd day: 1, 4

    Example 3:
    Input: weights = [1,2,3,1,1], D = 4
    Output: 3
    Explanation:
    1st day: 1
    2nd day: 2
    3rd day: 3
    4th day: 1, 1


    Note:
    1 <= D <= weights.length <= 50000
    1 <= weights[i] <= 500
 */

#include <vector>
#include <iostream>


using namespace std;


class Solution {

private:

    bool canShip(int weight, vector<int>& weights, int D) {
        int daysUsed = 0, weightTracker = 0;

        for (int w: weights) {
            weightTracker += w;
            if (weightTracker >= weight) {
                if ((++daysUsed) > D) return false;

                if (weightTracker == weight) weightTracker = 0;
                else weightTracker = w;
            }
        }

        daysUsed += (weightTracker > 0) ? 1 : 0;
        return daysUsed <= D;
    }

    int binarySearchMinWeight(
            vector<int>& weights,
            int D,
            int lBound,
            int uBound) {
        int minWeight = 0;

        while ((uBound - lBound) > 1) {
            minWeight = (lBound + uBound) / 2;
            if (canShip(minWeight, weights, D))
                uBound = minWeight;
            else
                lBound = minWeight;
        }
        return canShip(lBound, weights, D) ?  lBound : uBound;
    }

public:
    int shipWithinDays(vector<int>& weights, int D) {
        int lBound = 0, uBound = 0;
        for (int w: weights) {
            lBound = max(w, lBound); uBound += w;
        }
        return binarySearchMinWeight(weights, D, lBound, uBound);
    }
};


int main() {

    Solution sol;

    vector<int> weights1({1,2,3,4,5,6,7,8,9,10});
    cout << "The capacity for the 1st example is: "
         << sol.shipWithinDays(weights1, 5) << endl;

    cout << "################################################################################" << endl;

    vector<int> weights2({3,2,2,4,1,4});
    cout << "The capacity for the 2nd example is: "
         << sol.shipWithinDays(weights2, 3) << endl;

    cout << "################################################################################" << endl;

    vector<int> weights3({1,2,3,1,1});
    cout << "The capacity for the 3rd example is: "
         << sol.shipWithinDays(weights3, 4) << endl;

    return 0;
}
