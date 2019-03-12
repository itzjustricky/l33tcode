/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <algorithm>
#include <iostream>

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

    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) {
            return root;
        }

        swap(root->left, root->right);
        if (root->left != NULL) {
            invertTree(root->left);
        }
        if (root->right != NULL) {
            invertTree(root->right);
        }

        return root;
    }
};

TreeNode* constructTree() {
    TreeNode* node = new TreeNode(4);

    node->left = new TreeNode(2);
    node->left->left = new TreeNode(1);
    node->left->right = new TreeNode(3);

    node->right = new TreeNode(7);
    node->right->left = new TreeNode(6);
    node->right->right = new TreeNode(9);

    return node;
}

void printPreOrder(TreeNode* root) {

    if (root != NULL) {
        cout << root->val << " ";
        printPreOrder(root->left);
        printPreOrder(root->right);
    }
}


int main() {
    TreeNode* root = constructTree();
    printPreOrder(root);
    cout << endl;

    Solution sol;
    sol.invertTree(root);

    printPreOrder(root);
    cout << endl;

    return 0;
}
