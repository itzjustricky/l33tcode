/*
 *
    1022. Sum of Root To Leaf Binary Numbers
    Difficulty: Easy

    Given a binary tree, each node has value 0 or 1.
    Each root-to-leaf path represents a binary number starting with
    the most significant bit.

    For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
    01101 in binary, which is 13.

    For all leaves in the tree, consider the numbers represented by the path from the
    root to that leaf.
    Return the sum of these numbers.

    Example 1:
              1
           /     \
          0       1
         / \     / \
        0   1   0   1
    Input: [1,0,1,0,1,0,1]
    Output: 22
    Explanation: (100) + (101) + (110) + (111)
                 = 4 + 5 + 6 + 7 = 22

    Note:
    The number of nodes in the tree is between 1 and 1000. node.val is 0 or 1.
    The answer will not exceed 2^31 - 1.
 */

#include <cmath>
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
    unsigned int getNumber(const bool bitArray[32], int depth) {
        unsigned int num = 0;
        for (int i = 0; i <= depth; ++i) {
            num += pow(2, bitArray[depth-i]);
        }
        cout << "adding number " << num << endl;
        return num;
    }

    bool isRoot(TreeNode* nodePtr) {
        return (nodePtr->left == NULL) && (nodePtr->right == NULL);
    }

    int iterSum(TreeNode* nodePtr, bool bitArray[32], int depth) {
        if (nodePtr == NULL)
            return 0;
        else if (isRoot(nodePtr)) {
            bitArray[depth] = nodePtr->val;
            return getNumber(bitArray, depth);
        } else {
            bitArray[depth] = nodePtr->val;
            return iterSum(nodePtr->left, bitArray, depth+1) + \
                   iterSum(nodePtr->right, bitArray, depth+1);
        }
    }


public:
    int sumRootToLeaf(TreeNode* root) {
        bool bitArray[32] = {0};
        return iterSum(root, bitArray, 0);
    }
};
