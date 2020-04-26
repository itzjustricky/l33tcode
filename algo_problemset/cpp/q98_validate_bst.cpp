#include <limits>
#include <iostream>
#include <algorithm>


using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {

private:
    bool recursiveIsValidBST(TreeNode* root, long ltVal, long gtVal) {
        if (root == NULL) return true;

        int rootVal = root->val;
        if ((rootVal >= ltVal) || (rootVal <= gtVal)) return false;

        return
            recursiveIsValidBST(root->left, rootVal, gtVal)
            && recursiveIsValidBST(root->right, ltVal, rootVal);
}


public:
    bool isValidBST(TreeNode* root) {
        return recursiveIsValidBST(
            root, numeric_limits<long>::max(), numeric_limits<long>::min());
    }
};


int main() {
    Solution sol;

    TreeNode * tree = new TreeNode(2147483647);
    if (sol.isValidBST(tree))
        cout << "is valid" << endl;
    else
        cout << "is valid" << endl;

    return 0;
}
