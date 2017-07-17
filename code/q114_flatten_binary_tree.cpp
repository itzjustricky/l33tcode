/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <iostream>
#include <cassert>

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

    bool isLeaf(TreeNode* root) {
        return ((root->left == NULL) &&
                (root->right == NULL));
    }

    void deleteLeftChild(TreeNode* node) {
        node->left = NULL;
    }

    TreeNode* rearrange(TreeNode* node) {
        // assumes leaf nodes not passed in here
        assert(!isLeaf(node));

        TreeNode* leftChild = node->left;
        TreeNode* rightChild = node->right;
        TreeNode* leftTail; TreeNode* rightTail;

        node->left = NULL;
        if ((leftChild != NULL) && (rightChild != NULL)) {
            leftTail = recursiveFlatten(leftChild);
            rightTail = recursiveFlatten(rightChild);
            leftTail->right = rightChild;
            node->right = leftChild;
            deleteLeftChild(leftTail); deleteLeftChild(rightTail);
            deleteLeftChild(leftChild); deleteLeftChild(rightChild);

            return rightTail;

        } else if (leftChild != NULL) {     // only has left child
            leftTail = recursiveFlatten(leftChild);
            node->right = leftChild;
            deleteLeftChild(leftTail); deleteLeftChild(leftChild);

            return leftTail;

        } else {                            // only has right child
            rightTail = recursiveFlatten(rightChild);
            node->right = rightChild;
            deleteLeftChild(rightTail); deleteLeftChild(rightChild);

            return rightTail;
        }
    }


    TreeNode* recursiveFlatten(TreeNode* node) {
        if (node == NULL) {
            return node;
        } else if (isLeaf(node)) {
            return node;
        } else {
            return rearrange(node);
        }
    }

    void flatten(TreeNode* root) {
        recursiveFlatten(root);
    }

};


TreeNode* constructTree() {
    TreeNode* node = new TreeNode(1);

    node->left = new TreeNode(2);
    node->left->left = new TreeNode(3);
    node->left->right = new TreeNode(4);

    node->right = new TreeNode(5);
    node->right->right = new TreeNode(6);

    return node;
}

void printPreOrder(TreeNode* root) {

    if (root != NULL) {
        cout << root->val << " ";
        printPreOrder(root->left);
        printPreOrder(root->right);
    }
}

void printFlattenedTree(TreeNode* root) {
    TreeNode* nodePtr = root;

    while (nodePtr != NULL) {
        cout << nodePtr->val << " ";
        nodePtr = nodePtr->right;
    }
    cout << "\n";
}


int main() {
    TreeNode* testTree = constructTree();
    printPreOrder(testTree);
    cout << "\n";

    Solution sol;
    sol.flatten(testTree);
    printFlattenedTree(testTree);

    return 0;
}
