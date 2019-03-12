/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <iostream>
#include <cstdlib>

using namespace std;


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

float randfloat() {
    return (float) rand() / (RAND_MAX);
}

class Solution {
public:

    ListNode* mHead;

    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        mHead = head;
    }

    /** Returns a random node's value. */
    int getRandom() {
        ListNode* nodePtr = mHead;
        int randValue = 0, cnt = 0;

        while (nodePtr != NULL) {
            if (randfloat() < (1.0 / (1+cnt))) {
                randValue = nodePtr->val;
            }
            ++cnt; nodePtr = nodePtr->next;
        }
        return randValue;
    }
};


int main() {
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);

    // Your Solution object will be instantiated and called as such:
    Solution sol(head);
    cout << sol.getRandom() << endl;
    cout << sol.getRandom() << endl;
    cout << sol.getRandom() << endl;
    cout << sol.getRandom() << endl;
    cout << sol.getRandom() << endl;
    cout << sol.getRandom() << endl;
    cout << sol.getRandom() << endl;

    return 0;
}
