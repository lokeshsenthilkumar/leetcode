class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        return helper(1,n);
    }
    
    vector<TreeNode*> helper(int start, int end){
        
        vector<TreeNode*> v;
        
        if(start > end){
            v.push_back(NULL);
            return v;
        }
        
        if(start == end){
            v.push_back(new TreeNode(start));
            return v;
        }
        
        for(int i=start;i<=end;i++){
            
            vector<TreeNode*> left = helper(start,i-1);
            vector<TreeNode*> right = helper(i+1,end);
            
            for(auto leftNode : left){
                for(auto rightNode : right){
                    TreeNode* t = new TreeNode(i);
                    t -> left = leftNode;
                    t -> right = rightNode;
                    v.push_back(t);
                }
            }
        }
        
        return v;
        
    }
};

                                