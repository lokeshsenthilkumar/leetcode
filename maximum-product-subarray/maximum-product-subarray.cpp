class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
        int n = nums.size(), prefix = 0, suffix = 0, res = INT_MIN;
        
        for(int i=0;i<nums.size();i++){
            prefix = (prefix==0 ? 1 : prefix) * nums[i];
            suffix = (suffix==0 ? 1 : suffix) * nums[n-i-1];
            res = max({res,prefix,suffix});
        }
        
        return res;

    }
};

