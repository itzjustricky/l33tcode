/*
 * Description:
 *
 *
 * TODO:
 *      switch to using tuple and tie, more elegant
 *
 *
 * @author: Ricky Chang
*/

#include <iostream>

#include <vector>
#include <utility>
// #include <algorithm>

using namespace std;

void printVector(vector<int> v) {
    for (auto x : v) {
        cout << x << " ";
    }
    cout << endl;
}


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:

    int mLargestModeCount = 0;

    void updateStacks(vector<int>& modeStack, vector<int>& countStack) {
        if (countStack.back() < mLargestModeCount) {
            countStack.pop_back();
            modeStack.pop_back();
        } else if (countStack.back() > mLargestModeCount) {
            mLargestModeCount = countStack.back();
            // erase all but last if value on top has highest count
            countStack.erase(countStack.begin(), countStack.end()-1);
            modeStack.erase(modeStack.begin(), modeStack.end()-1);
        }
    }

    void updateMode(int newVal, vector<int>& modeStack, vector<int>& countStack) {

        if (modeStack.empty()) {    // first time updateMode is called
            modeStack.emplace_back(newVal);
            countStack.emplace_back(1);
        } else if (modeStack.back() == newVal) {
            ++countStack.back();
        } else {
            updateStacks(modeStack, countStack);
            modeStack.emplace_back(newVal);
            countStack.emplace_back(1);
        }

    }

    void inorderHelper(TreeNode* node, vector<int>& modeStack, vector<int>& countStack) {
        if (node != NULL) {
            inorderHelper(node->left, modeStack, countStack);
            updateMode(node->val, modeStack, countStack);
            inorderHelper(node->right, modeStack, countStack);
        }
    }

    vector<int> findMode(TreeNode* root) {
        if (root == NULL) {
            return vector<int>();
        }

        mLargestModeCount = 0;
        vector<int> modeStack;
        vector<int> countStack;

        inorderHelper(root, modeStack, countStack);
        // update one last time for most recent insert
        updateStacks(modeStack, countStack);

        return modeStack;
    }
};


TreeNode* constructTree() {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(2);

    return root;
}


int main() {
    TreeNode* tree = constructTree();

    Solution sol;
    vector<int> modes = sol.findMode(tree);

    cout << "The modes are: " << endl;
    printVector(modes);

    return 0;
}
