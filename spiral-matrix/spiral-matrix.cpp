class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        int rs = 0, cs = 0, re = matrix.size()-1, ce = matrix[0].size()-1;
        vector<int> res;
        
        while(rs<=re && cs<=ce){
            
            for(int i=cs;i<=ce;i++){
                res.push_back(matrix[rs][i]);
            }
            
            // res.push_back(-1);
            
            rs++;
            
            for(int i=rs;i<=re;i++){
                res.push_back(matrix[i][ce]);
            }
            
            // res.push_back(-1);
            
            ce--;
            
            if(rs <= re){
                for(int i=ce;i>=cs;i--){
                    res.push_back(matrix[re][i]);
                }
                
            }
            
            re--;
            // res.push_back(-1);
            
            
            if(cs<=ce){
                for(int i=re;i>=rs;i--){
                    res.push_back(matrix[i][cs]);
                }
            }
            
            // res.push_back(-1);
            cs++;
            
        }
        
        return res;
            
    }
};