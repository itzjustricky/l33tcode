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

private:
    bool canAdvanceFastPtr(ListNode* fastPtr) {
        return (fastPtr != NULL) && \
               (fastPtr->next != NULL);
    }

    ListNode* findCycleStart(ListNode* head, ListNode* meetPoint) {
        ListNode* newPtr = head;
        while (newPtr != meetPoint) {
            meetPoint = meetPoint->next;
            newPtr = newPtr->next;
        }
        return newPtr;

    }

public:

    ListNode *detectCycle(ListNode *head) {
        ListNode* fastPtr = head;
        ListNode* slowPtr = head;

        while (true) {
            if (!canAdvanceFastPtr(fastPtr)) { return NULL; }
            fastPtr = fastPtr->next->next;
            slowPtr = slowPtr->next;
            if (slowPtr == fastPtr) { break; }
        }
        // there is definitely cycle at this point
        return findCycleStart(head, slowPtr);
    }

};
