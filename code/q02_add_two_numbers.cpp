/*
 * Description:
 *
 *
 *
 * @author: Ricky Chang
*/

#include <vector>
#include <iostream>
#include <stdexcept>

using namespace std;


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};


// constructs LinkedList from vector
ListNode* vectorToLinkedList(const vector<int>& vect);
// prints content of LinkedList
void printLinkedList(ListNode* rootNode);


class Solution {
public:
    int addTwoDigits(ListNode* l1, ListNode* l2) {
        int digit1, digit2;

        digit1 = (l1 == nullptr) ? 0 : l1->val;
        digit2 = (l2 == nullptr) ? 0 : l2->val;
        return digit1 + digit2;
    }

    ListNode* moveIterForward(ListNode* nodePtr) {
        if (nodePtr == nullptr) {
            return nodePtr;
        } else {
            return nodePtr->next;
        }
    }

    // assumes list only carries digits (i.e. numbers less than 10)
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* lIter1 = l1; ListNode* lIter2 = l2;
        ListNode* sumNodeRoot = nullptr; ListNode* sumNodePtr = nullptr;
        int carry = 0, digitSum = 0;

        if (l1 == nullptr && l2 == nullptr) return sumNodeRoot;

        while (lIter1 != nullptr || lIter2 != nullptr) {
            digitSum = addTwoDigits(lIter1, lIter2) + carry;
            carry = digitSum / 10;      // always carry <= 1

            if (sumNodeRoot == nullptr) {
                sumNodeRoot = new ListNode(digitSum % 10);
                sumNodePtr = sumNodeRoot;
            } else {
                sumNodePtr->next = new ListNode(digitSum % 10);
                sumNodePtr = sumNodePtr->next;
            }

            lIter1 = moveIterForward(lIter1);
            lIter2 = moveIterForward(lIter2);
        }
        if (carry >= 1) sumNodePtr->next = new ListNode(carry);
        return sumNodeRoot;
    }

};


ListNode* vectorToLinkedList(const vector<int>& vect) {
    int n = vect.size();
    if (n == 0) throw invalid_argument("vector passed is empty");
    ListNode* nodeRoot = new ListNode(vect[0]);
    ListNode* nodePtr = nodeRoot;

    for (int i = 1; i < n; ++i) {
        nodePtr->next = new ListNode(vect[i]);
        nodePtr = nodePtr->next;
    }

    return nodeRoot;
}


void printLinkedList(ListNode* rootNode) {
    ListNode* nodePtr = rootNode;

    while (nodePtr != nullptr) {
        cout << nodePtr->val << ' ';
        nodePtr = nodePtr->next;
    }
    cout << '\n';
}


int main() {

    ListNode* l1 = vectorToLinkedList({5});
    ListNode* l2 = vectorToLinkedList({5});

    Solution sol = Solution();
    ListNode* res = sol.addTwoNumbers(l1, l2);
    printLinkedList(res);

    return 0;
}
