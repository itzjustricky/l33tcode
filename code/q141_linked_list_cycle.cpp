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

public:
    bool hasCycle(ListNode *head) {
        if (head == NULL) { return false; }

        ListNode* fastPtr = head;
        ListNode* slowPtr = head;

        while (true) {
            if (!canAdvanceFastPtr(fastPtr)) { break; }
            fastPtr = fastPtr->next->next;
            slowPtr = slowPtr->next;
            if (slowPtr == fastPtr) { return true; }
        }

        return false;
    }
};
