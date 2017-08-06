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
    bool hasCycle(ListNode *head) {
        if (head == NULL) { return false; }

        ListNode* fastPtr = head;
        ListNode* slowPtr = head;

        while (fastPtr->next != NULL) {
            fastPtr = fastPtr->next->next;
            slowPtr = slowPtr->next;
            if (slowPtr == fastPtr) { return true; }
            if (fastPtr == NULL) { break; }
        }

        return false;
    }
};
