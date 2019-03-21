/*
 * Question 129:

    Given a binary tree containing digits from 0-9 only,
    each root-to-leaf path could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.
    Find the total sum of all root-to-leaf numbers.
    Note: A leaf is a node with no children.

    Example:

    Input: [1,2,3]
        1
       / \
      2   3
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.

    Example 2:

    Input: [4,9,0,5,1]
        4
       / \
      9   0
     / \
    5   1
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.
 *
*/

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

private:
    bool isLeaf(TreeNode* nodePtr) {
        return (nodePtr->left == NULL) &&
               (nodePtr->right == NULL);
    }

    int traverseAndSum(TreeNode* nodePtr, int trackedNum) {
        if (nodePtr == NULL) return 0;

        trackedNum = trackedNum*10 + nodePtr->val;
        if (isLeaf(nodePtr)) return trackedNum;

        return traverseAndSum(nodePtr->left, trackedNum) + \
               traverseAndSum(nodePtr->right, trackedNum);
    }


public:
    int sumNumbers(TreeNode* root) {
        return traverseAndSum(root, 0);
    }
};


int main() {
    Solution sol;

    // Create tree from Example 2:
    //     4
    //    / \
    //   9   0
    //  / \
    // 5   1

    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(9);
    root->left->left = new TreeNode(5);
    root->left->right = new TreeNode(1);
    root->right = new TreeNode(0);

    cout << "The sum is " << sol.sumNumbers(root) << endl;

    return 0;
}
