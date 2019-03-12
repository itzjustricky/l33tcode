/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <iostream>
#include <vector>

using namespace std;


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

    bool canAdvanceFastPtr(ListNode* fastPtr) {
        return (fastPtr != NULL) && (fastPtr->next != NULL);
    }

    ListNode* getBeforeMidPoint(ListNode* node) {
        ListNode* slowPtr = node;
        ListNode* fastPtr = node;

        while (true) {
            fastPtr = fastPtr->next->next;
            if (!canAdvanceFastPtr(fastPtr)) { break; }
            slowPtr = slowPtr->next;
        }

        return slowPtr;
    }

    TreeNode* splitList(ListNode* node) {
        ListNode* beforeMidNode;
        TreeNode* rootNode;

        if (node == NULL) {
            return NULL;
        } else if (node->next == NULL) {
            rootNode = new TreeNode(node->val);
            return rootNode;
        }

        beforeMidNode = getBeforeMidPoint(node);
        rootNode = new TreeNode(beforeMidNode->next->val);

        rootNode->right = splitList(beforeMidNode->next->next);
        // disconnect the list from the middle
        beforeMidNode->next = NULL;
        rootNode->left = splitList(node);

        return rootNode;
    }

public:

    TreeNode* sortedListToBST(ListNode* head) {
        return splitList(head);
    }
};


ListNode* createList(vector<int> v) {
    ListNode* nodeStart = new ListNode(v[0]);
    ListNode* nodePtr = nodeStart;

    int n = v.size();
    for (int i = 1; i < n; ++i) {
        nodePtr->next = new ListNode(v[i]);
        nodePtr = nodePtr->next;
    }
    return nodeStart;
}

void printInOrder(TreeNode* root) {
    if (root == NULL) { return; }
    printInOrder(root->left);
    cout << root->val << ' ';
    printInOrder(root->right);
}


int main() {

    Solution sol;
    ListNode* list = createList({1, 3, 5, 8, 9, 10, 12, 18});
    TreeNode* root = sol.sortedListToBST(list);

    printInOrder(root);
    cout << endl;

    return 0;
}
