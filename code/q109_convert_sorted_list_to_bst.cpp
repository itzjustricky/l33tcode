/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <iostream>


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {

private:

    ListNode* getMidPoint(ListNode* node) {
        if (node == NULL) { return NULL; }

        ListNode* slowPtr = node;
        ListNode* fastPtr = node;

        while (fastPtr->next != NULL) {
            slowPtr = slowPtr->next;
            fastPtr = fastPtr->next->next;
        }
        return slowPtr;
    }

    TreeNode* splitList(ListNode* node) {
        ListNode* midNode = getMidPoint(node);

        if (midNode == NULL) { return NULL; }

        TreeNode* rootNode = new TreeNode(midNode->val);
        rootNode->right = splitList(midNode->next);
        // disconnect the list from the middle
        midNode->next = NULL;
        rootNode->left = splitList(node);

        return rootNode;
    }

public:

    TreeNode* sortedListToBST(ListNode* head) {
        return splitList(head);
    }
};
