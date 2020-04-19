#include <vector>

using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {

private:
    vector<int> recursiveInOrderTraversal(TreeNode* root, vector<int>& inOrder) {
        if (root == NULL) return inOrder;

        if (root->left != NULL)
            recursiveInOrderTraversal(root->left, inOrder);
        inOrder.push_back(root->val);
        if (root->right != NULL)
            recursiveInOrderTraversal(root->right, inOrder);

        return inOrder;
    }

public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inOrder;
        return recursiveInOrderTraversal(root, inOrder);
    }
};
