/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {

public:

    ListNode *detectCycle(ListNode *head) {
        if (head == NULL) { return NULL; }

        ListNode* fastPtr = head;
        ListNode* slowPtr = head;

        while (fastPtr->next != NULL) {
            fastPtr = fastPtr->next->next;
            slowPtr = slowPtr->next;
            if (slowPtr == fastPtr) { break; }
            if (fastPtr == NULL) { return NULL; }
        }

        if (fastPtr->next == NULL) { return NULL; }

        // there is definitely cycle at this point
        ListNode* newPtr = head;
        while (newPtr != slowPtr) {
            slowPtr = slowPtr->next;
            newPtr = newPtr->next;
        }
        return newPtr;
    }

};
