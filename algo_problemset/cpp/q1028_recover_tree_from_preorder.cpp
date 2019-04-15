/*
    1028. Recover a Tree From Preorder Traversal
    Difficulty: Hard

    We run a preorder depth first search on the root of a binary tree.

    At each node in this traversal, we output D dashes (where D is the depth
    of this node), then we output the value of this node. (If the depth of a node is D,
    the depth of its immediate child is D+1.  The depth of the root node is 0.)

    If a node has only one child, that child is guaranteed to be the left child.

    Given the output S of this traversal, recover the tree and return its root.

 */


#include <tuple>
#include <string>
#include <utility>
#include <iostream>


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

    int extractValueLength(const string& S, int startIndex) {
        int N = S.size();
        if (startIndex >= N) return -1;

        for (int i = startIndex; i < N; ++i) {
            if (S[i] == '-')
                return i - startIndex;
        }
        return N - startIndex;
    }

    int extractDepth(const string& S, int startIndex) {
        int N = S.size();
        if (startIndex >= N) return -1;

        for (int i = startIndex; i < N; ++i) {
            if (S[i] != '-')
                return i - startIndex;
        }
        return N - startIndex;
    }

    pair<TreeNode*, int> createTree(string S, int startIndex, int currDepth) {
        int valueLength = extractValueLength(S, startIndex);
        int val = stoi(S.substr(startIndex, valueLength));
        int distMoved = 0, tmpDist = 0;

        int depth = 0;
        TreeNode* root = new TreeNode(val);
        depth = extractDepth(S, startIndex + valueLength);
        distMoved += valueLength;

        // see if there is a left child to populate
        if (depth == currDepth+1) {
            distMoved += depth;
            tie(root->left, tmpDist) = \
                createTree(S, startIndex + distMoved, depth);
            distMoved += tmpDist;

            // see if there is a right child to populate
            depth = extractDepth(S, startIndex + distMoved);
            if (depth == currDepth+1) {
                distMoved += depth;
                tie(root->right, tmpDist) = \
                    createTree(S, startIndex + distMoved, depth);
                distMoved += tmpDist;
            }
        }
        return make_pair(root, distMoved);
    }

public:

    TreeNode* recoverFromPreorder(string S) {
        int dummy = 0;
        TreeNode* root;
        tie(root, dummy) = createTree(S, 0, 0);
        return root;
    }
};


int main() {

    return 0;
}
