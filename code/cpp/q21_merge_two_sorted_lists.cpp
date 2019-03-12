/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:

    ListNode* deleteDummyHead(ListNode* head) {
        ListNode* dummyHead = head;
        head = head->next;
        delete dummyHead;
        return head;
    }

    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if ((l1 == NULL) && (l2 == NULL)) {
            return l1;
        }
        // create a dummy head to be dropped later
        ListNode* newHead = new ListNode(0);
        ListNode* newIter = newHead;

        while ((l1 != NULL) && (l2 != NULL)) {
            if (l1->val < l2->val) {
                newIter->next = l1;
                l1 = l1->next;
            } else {
                newIter->next = l2;
                l2 = l2->next;
            }
            newIter = newIter->next;
        }

        // set rest to list that didn't end
        if (l1 == NULL) {
            newIter->next = l2;
        } else {
            newIter->next = l1;
        }
        return deleteDummyHead(newHead);
    }
};


ListNode* listFromVector(vector<int> values) {
    size_t n = values.size();
    ListNode* nodeHead = new ListNode(values[0]);
    ListNode* nodePtr = nodeHead;
    for (size_t i = 1; i < n; ++i) {
        nodePtr->next = new ListNode(values[i]);
        nodePtr = nodePtr->next;
    }
    return nodeHead;
}

void printLinkedList(ListNode* node) {
    while (node != NULL) {
        cout << node->val << " ";
        node = node->next;
    }
}


int main() {
    ListNode* node1 = listFromVector({1, 2, 6, 9, 12});
    ListNode* node2 = listFromVector({3, 8, 15, 18, 20});
    printLinkedList(node1);
    cout << endl;
    printLinkedList(node2);
    cout << endl;

    Solution sol;
    ListNode* mergedNode = sol.mergeTwoLists(node1, node2);
    printLinkedList(mergedNode);
    cout << endl;

    return 0;
}
