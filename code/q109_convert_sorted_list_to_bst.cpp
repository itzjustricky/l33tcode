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

    ListNode* getMidPoint(ListNode* node) {
        if (node == NULL) { return NULL; }

        ListNode* slowPtr = node;
        ListNode* fastPtr = node;

        while (fastPtr->next != NULL) {
            slowPtr = slowPtr->next;
            fastPtr = fastPtr->next->next;
            if (fastPtr == NULL) { break; }
        }

        cout << "passed node is " << node->val << endl;
        cout << "mid-point is " << slowPtr->val << endl;
        return slowPtr;
    }

    TreeNode* splitList(ListNode* node) {
        if (node == NULL) { return NULL; }
        ListNode* midNode = getMidPoint(node);

        TreeNode* rootNode = new TreeNode(midNode->val);
        if (midNode == node) { return rootNode; }

        cout << "setting right child" << endl;
        rootNode->right = splitList(midNode->next);
        // disconnect the list from the middle
        cout << "setting left child" << endl;
        midNode->next = NULL;
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


int main() {

    Solution sol;
    ListNode* list = createList({1, 3, 5, 8, 9, 10, 12, 18});
    sol.sortedListToBST(list);

    return 0;
}
