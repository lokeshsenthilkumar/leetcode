/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        
        if(!root1 && !root2)
            return NULL;
        
        int r1v = root1 ? root1->val : 0;
        int r2v = root2 ? root2->val : 0;
        
        TreeNode* res = new TreeNode(r1v + r2v);
        
        res->left = mergeTrees(root1 ? root1->left : NULL ,root2 ? root2->left : NULL);
        res->right = mergeTrees(root1 ? root1->right : NULL, root2 ? root2->right : NULL);
        
        return res;
        
    }
};

       // 1            1
       //             /
       //            2
       //           /
       //          3