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


void printVector(const vector<int>& v) {
    for (auto x : v) {
        cout << x << " ";
    }
    cout << endl;
}


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
    typedef pair<int, vector<int>> mode_pair;

    bool isLeaf(TreeNode* node) {
        return ((node->left == NULL) && (node->right == NULL));
    }

    bool isInVector(int x, const vector<int>& v) {
        return find(v.begin(), v.end(), x) != v.end();
    }

    void updateMode(int rootVal, mode_pair& leftSubTree) {
        if (isInVector(rootVal, leftSubTree.second)) {
            leftSubTree.first += 1;
            leftSubTree.second = vector<int>(1, rootVal);
        } else if (leftSubTree.first == 0) {
            leftSubTree.first = 1;
            leftSubTree.second = vector<int>(1, rootVal);
        } else if (leftSubTree.first == 1) {
            leftSubTree.second.push_back(rootVal);
        }
    }

    vector<int> combineVectors(const vector<int>& v1, const vector<int>& v2) {
        vector<int> newVector;
        newVector.insert(newVector.end(), v1.begin(), v1.end());
        newVector.insert(newVector.end(), v2.begin(), v2.end());
        return newVector;
    }

    mode_pair intersectModes(const mode_pair& left_modes, const mode_pair& right_modes) {
        vector<int> modeIntersect;
        for (auto x : left_modes.second) {
            if (isInVector(x, right_modes.second)) {
                modeIntersect.push_back(x);
            }
        }

        if (modeIntersect.size() > 0) {
            return make_pair(left_modes.first + right_modes.first, modeIntersect);
        } else {
            return make_pair(0, modeIntersect);
        }
    }

    mode_pair recursiveFindMode(TreeNode* root) {
        if (root == NULL) {
            return make_pair(0, vector<int>());
        }
        if (isLeaf(root)) {
            return make_pair(1, vector<int>(1, root->val));
        }

        vector<int> mergedModes;

        mode_pair leftSubTree = recursiveFindMode(root->left);
        mode_pair rightSubTree = recursiveFindMode(root->right);
        // here I count the root as part of the left sub-tree
        updateMode(root->val, leftSubTree);

        mode_pair subTreeIntersect = intersectModes(leftSubTree, rightSubTree);
        if (subTreeIntersect.first > 0) {
            return subTreeIntersect;

        } else {
            if (leftSubTree.first > rightSubTree.first) {
                return leftSubTree;
            } else if (leftSubTree.first < rightSubTree.first) {
                return rightSubTree;
            } else {    // mode count of left and right are the same
                mergedModes = combineVectors(leftSubTree.second, rightSubTree.second);
                return make_pair(leftSubTree.first, mergedModes);
            }
        }

    }

    vector<int> findMode(TreeNode* root) {
        mode_pair treeModes = recursiveFindMode(root);
        return treeModes.second;
    }
};


TreeNode* constructTree() {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    // root->right->left = new TreeNode(2);

    return root;
}


int main() {
    TreeNode* tree = constructTree();

    Solution sol;
    vector<int> modes = sol.findMode(tree);

    cout << "The modes are: " << endl;
    printVector(modes);

    return 0;
}
