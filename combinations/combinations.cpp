class Solution {
private:
    vector<vector<int>> ans;
    vector<int> sub;
    
public:
    vector<vector<int>> combine(int n, int k) {
        
        explore(1,n,k);
        return ans;
        
    }
    
    void explore(int start, int n, int k){
        
        if(sub.size() == k){
            ans.push_back(sub);
            return;
        }
        
        for(int i=start;i<=n;i++){
            sub.push_back(i);
            explore(i+1,n,k);
            sub.pop_back();
        }
        
    }
};