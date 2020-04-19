#include <stack>
#include <queue>
#include <vector>
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inOrder;
        if (root == NULL) return inOrder;

        queue<TreeNode> nodeQueue; nodeQueue.push(*root);
        stack<TreeNode> reserveNodeStack;

        TreeNode* nodePtr = NULL;
        TreeNode* extraNodePtr = NULL;
        while (!nodeQueue.empty() || !reserveNodeStack.empty()) {

            if (!nodeQueue.empty()) {
                nodePtr = &nodeQueue.front();
                reserveNodeStack.push(*nodePtr);
                // nodeQueue.pop() may lead to memory leak
                extraNodePtr = nodePtr->left;

                nodeQueue.pop();

                if (extraNodePtr != NULL) nodeQueue.push(*extraNodePtr);
            } else {
                nodePtr = &reserveNodeStack.top();
                inOrder.push_back(nodePtr->val);
                extraNodePtr = nodePtr->right;

                reserveNodeStack.pop();
                if (extraNodePtr != NULL) nodeQueue.push(*extraNodePtr);
            }
        }

        return inOrder;
    }
};
