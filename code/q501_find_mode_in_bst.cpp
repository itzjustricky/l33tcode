/*
 * Description:
 *
 *
 * TODO:
 *      switch to using tuple and tie, more elegant
 *
 *
 * @author: Ricky Chang
*/

#include <iostream>

#include <vector>
#include <utility>
#include <algorithm>

using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:

    // first stores count, second stores numbers with that count
    typedef pair<int, vector<int>> mode_count;

    bool isLeaf(TreeNode* node) {
        return ((node->left == NULL) && (node->right == NULL));
    }

    bool isInVector(int x, const vector<int>& v) {
        return find(v.begin(), v.end(), x) != v.end();
    }

    void updateModeWithValue(int rootVal, mode_count& leftSubTree) {
        if (leftSubTree.first == 1) {
            leftSubTree.second.emplace_back(rootVal);
        } else if (isInVector(rootVal, leftSubTree.second)) {
            leftSubTree.first += 1;
            leftSubTree.second = vector<int>(rootVal);
        }

    }

    vector<int> combineVectors(const vector<int>& v1, const vector<int>& v2) {
        vector<int> newVector(v1.size() + v2.size());
        newVector.insert(newVector.end(), v1.begin(), v1.end());
        newVector.insert(newVector.end(), v2.begin(), v2.end());
        return newVector;
    }

    vector<int> accumulateModes(const vector<int>& left_modes, const vector<int>& right_modes) {
        vector<int> accmModes;

        for (auto x : left_modes) {
            if (isInVector(x, right_modes)) {
                accmModes.push_back(x);
            }
        }
        return accmModes;
    }

    mode_count recursiveFindMode(TreeNode* root) {
        if (isLeaf(root)) {
            return make_pair(1, vector<int>(1, root->val));
        }

        mode_count leftSubTree = recursiveFindMode(root->left);
        mode_count rightSubTree = recursiveFindMode(root->right);
        vector<int> accmModes = accumulateModes(leftSubTree.second, rightSubTree.second);

        if (accmModes.size() > 0) {
            if (isInVector(root->val, accmModes)) {
                return make_pair(leftSubTree.first + rightSubTree.first + 1,
                                 vector<int>(1, root->val));
            } else {
                return make_pair(leftSubTree.first + rightSubTree.first,
                                 accmModes);
            }
        } else {
            // TODO: need to handle the root value too
            updateModeWithValue(root->val, leftSubTree);

            if (leftSubTree.first > rightSubTree.first) {
                return leftSubTree;
            } else if (leftSubTree.first < rightSubTree.first) {
                return rightSubTree;
            } else {
                return make_pair(leftSubTree.first,
                                 combineVectors(leftSubTree.second, rightSubTree.second));
            }
        }

    }

    vector<int> findMode(TreeNode* root) {
        mode_count treeModes = recursiveFindMode(root);

        return treeModes.second;
    }
};

int main() {


    return 0;
}
