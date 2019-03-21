/*
 *
 *
 * @author: Ricky Chang
 */

#include <climits>
#include <iostream>
#include <unordered_map>

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
    bool isFlipped(TreeNode* left, TreeNode* right) {
        if ((left == NULL) && (right == NULL)) {
            return true;
        } else if ((left == NULL) || (right == NULL)) {
            return false;
        }

        if ((left->val == right->val) &&
            isFlipped(left->left, right->right) &&
            isFlipped(left->right, right->left)) {
            return true;
        } else {
            return false;
        }

    }

    bool isSymmetric(TreeNode* root) {
        if (root == NULL) {
            return true;
        }

        return isFlipped(root->left, root->right);
    }
};
