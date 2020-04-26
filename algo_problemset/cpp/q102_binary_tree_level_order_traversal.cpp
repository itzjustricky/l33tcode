#include <queue>
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
    void extractChildren(queue<TreeNode>& nodesPerLevel, TreeNode* node) {
        if (node->left != NULL)
            nodesPerLevel.push(*node->left);
        if (node->right != NULL)
            nodesPerLevel.push(*node->right);
    }


public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        vector<int>* oneLevel;

        if (root == NULL) return levels;

        queue<TreeNode> nodesPerLevel;
        nodesPerLevel.push(*root);

        int n = 0;
        TreeNode* nodePtr = NULL;
        while (!nodesPerLevel.empty()) {
            n = nodesPerLevel.size();
            oneLevel = new vector<int>();

            for (int i = 0; i < n; ++i) {
                nodePtr = &nodesPerLevel.front();
                oneLevel->push_back(nodePtr->val);
                extractChildren(nodesPerLevel, nodePtr);

                nodesPerLevel.pop();
            }

            levels.push_back(*oneLevel);
        }

        return levels;
    }
};
