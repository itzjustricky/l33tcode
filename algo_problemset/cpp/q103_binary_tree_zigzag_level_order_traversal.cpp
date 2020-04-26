#include <deque>
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

    struct push_to_front {};
    struct push_to_back {};

    void extractChildren(
            deque<TreeNode>& nodesPerLevel,
            TreeNode* node,
            const push_to_front) {
        if (node->right != NULL)
            nodesPerLevel.push_front(*node->right);
        if (node->left != NULL)
            nodesPerLevel.push_front(*node->left);
    }

    void extractChildren(
            deque<TreeNode>& nodesPerLevel,
            TreeNode* node,
            const push_to_back) {
        if (node->left != NULL)
            nodesPerLevel.push_back(*node->left);
        if (node->right != NULL)
            nodesPerLevel.push_back(*node->right);
    }

public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        vector<int>* oneLevel;

        bool leftToRight = true;

        if (root == NULL) return levels;

        deque<TreeNode> nodesPerLevel;
        nodesPerLevel.push_back(*root);

        int n = 0;
        TreeNode* nodePtr = NULL;
        while (!nodesPerLevel.empty()) {
            n = nodesPerLevel.size();
            oneLevel = new vector<int>();

            if (leftToRight) for (int i = 0; i < n; ++i) {
                nodePtr = &nodesPerLevel.front();
                oneLevel->push_back(nodePtr->val);
                extractChildren(nodesPerLevel, nodePtr, push_to_back());

                nodesPerLevel.pop_front();
            }
            else for (int i = 0; i < n; ++i) {
                nodePtr = &nodesPerLevel.back();
                oneLevel->push_back(nodePtr->val);
                extractChildren(nodesPerLevel, nodePtr, push_to_front());

                nodesPerLevel.pop_back();
            }

            leftToRight ^= true;
            levels.push_back(*oneLevel);
        }

        return levels;
    }
};
