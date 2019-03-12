/*
 * Question 56:

    Given a collection of intervals, merge all overlapping intervals.

    Example 1:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Example 2:
    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
*/


#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


// Definition for an interval.
struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};


// Functor for less than operation between Intervals
struct Interval_less_than {
    inline bool operator()(const Interval& int1, const Interval& int2) {
        if (int1.start < int2.start) {
            return true;
        } else if (int1.start == int2.start) {
            return int1.end < int2.end;
        } else {
            return false;
        }
    }
};


class Solution {
private:
    // Assumes that int1 <= int2
    bool canMerge(const Interval& int1, const Interval& int2) {
        return (int1.end >= int2.start);
    }

    // Assumes that int1 <= int2
    Interval mergeIntervals(const Interval& int1, const Interval& int2) {
        return Interval(int1.start, max(int1.end, int2.end));
    }

public:
    vector<Interval> merge(vector<Interval>& intervals) {
        // first sort the interval O(nlogn)
        sort(intervals.begin(), intervals.end(), Interval_less_than());
        vector<Interval> mergedIntervals;
        int numOfIntervals = intervals.size();

        if (numOfIntervals == 0) return mergedIntervals;

        Interval tmpInterval = intervals[0];
        // O(n) merging operation
        for (int i = 1; i < numOfIntervals; ++i) {
            if (canMerge(tmpInterval, intervals[i])) {
                tmpInterval = mergeIntervals(tmpInterval, intervals[i]);
            } else {
                mergedIntervals.push_back(tmpInterval);
                tmpInterval = intervals[i];
            }
        }
        mergedIntervals.push_back(tmpInterval);
        return mergedIntervals;
    }
};


void printVectorOfIntervals(const vector<Interval>& v) {
    for (Interval x: v)
        cout << "[" << x.start << "," << x.end << "] ";

    cout << endl;
}


int main() {
    Solution sol;

    // Example 1:
    // Input: [[1,3],[2,6],[8,10],[15,18]]
    // Output: [[1,6],[8,10],[15,18]]
    // Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    vector<Interval> intervals1({
        Interval(1, 3), Interval(2, 6),
        Interval(8, 10), Interval(15, 18)
    });

    cout << "For input: " << endl;
    printVectorOfIntervals(intervals1);
    vector<Interval> mergedIntervals1 = sol.merge(intervals1);
    printVectorOfIntervals(mergedIntervals1);

    return 0;
}
