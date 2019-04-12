/*
 *
    You are given a series of video clips from a sporting event that lasted T seconds.
    These video clips can be overlapping with each other and have varied lengths.

    Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends
    at time clips[i][1].  We can cut these clips into segments freely: for example,
    a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

    Return the minimum number of clips needed so that we can cut the clips into segments
    that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.


    Example 1:
    Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
    Output: 3
    Explanation:
    We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
    Then, we can reconstruct the sporting event as follows:
    We cut [1,9] into segments [1,2] + [2,8] + [8,9].
    Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

    Example 2:
    Input: clips = [[0,1],[1,2]], T = 5
    Output: -1
    Explanation:
    We can't cover [0,5] with only [0,1] and [0,2].

    Example 3:
    Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
    Output: 3
    Explanation:
    We can take clips [0,4], [4,7], and [6,9].

    Example 4:
    Input: clips = [[0,4],[2,8]], T = 5
    Output: 2
    Explanation:
    Notice you can have extra video after the event ends.
 *
 */


// #include <stack>
#include <deque>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

template <typename T>
void print2DVector(const vector<vector<T>>& X);


struct less_than_key {
    inline bool operator() (const vector<int>& c1, const vector<int>& c2) {
        return (c1[0] < c2[0]) ||
               ((c1[0] <= c2[0]) && (c1[1] <= c2[1]));
    }
};


class Solution {

private:
    // Remove clips from the stack that are not needed after newClip is added.
    void cleanStack(deque<vector<int>>& clipDeque, const vector<int>& newClip) {
        auto it1 = clipDeque.rbegin(); auto it2 = it1 + 1;

        while ((it2 != clipDeque.rend()) && ((*it2)[1] >= newClip[0])) {
            ++it1; ++it2;
            clipDeque.pop_back();
        }
    }

public:
    int videoStitching(vector<vector<int>>& clips, int T) {
        if (T == 0) return 0;
        if (clips.size() == 0) return -1;

        // sort the clips, start takes priority over end
        sort(clips.begin(), clips.end(), less_than_key());
        if (clips[0][0] != 0) return -1;

        deque<vector<int>> clipDeque;

        // get longest clip starting at 0
        int i = 0;
        while (clips[i][0] == 0) ++i;
        clipDeque.push_back(clips[i-1]);
        if (clipDeque.back()[1] >= T) return clipDeque.size();

        int currTail = 0;
        for (auto it = clips.begin() + i; it != clips.end(); ++it) {
            currTail = clipDeque.back()[1];
            // if current tail cannot reach the beginning of current clip then task is impossible
            if (currTail < (*it)[0]) return -1;

            if ((*it)[1] >= currTail) {
                cleanStack(clipDeque, *it);
                clipDeque.push_back(*it);

                if (clipDeque.back()[1] >= T) return clipDeque.size();
            }
        }

        return (clipDeque.back()[1] >= T) ? clipDeque.size() : -1;
    }
};


template <typename T>
void print2DVector(const vector<vector<T>>& X) {
    for (auto row : X) {
        for (auto x : row) cout << x << ' ';
        cout << endl;
    }
}


int main() {
    Solution sol;
    vector<vector<int>> clips1 = {
        {0,2}, {4,6}, {8,10},
        {1,9}, {1,5}, {5,9}};
    cout << "The output for Example 1: " << sol.videoStitching(clips1, 10) << endl;

    vector<vector<int>> clips2 = \
        {{5,7},{1,8},{0,0},{2,3},{4,5},{0,6},{5,10},{7,10}};
    cout << "The output for Example 2: " << sol.videoStitching(clips2, 5) << endl;

    return 0;
}
