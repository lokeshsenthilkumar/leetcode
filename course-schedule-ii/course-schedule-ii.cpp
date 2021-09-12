class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int>>& pre) {
           
        vector<int> adj[n];
        vector<int> output;
        
        for(auto edge : pre)
            adj[edge[0]].push_back(edge[1]);
        
        vector<int> vis(n,0);
        
        for(int i=0;i<n;i++){
            if(iscycle(adj,vis,i,output))
                return {};
        }
        
        return output;
    }
    
    bool iscycle(vector<int> adj[],vector<int> &vis,int id,vector<int> &output){
        
        if(vis[id]==1)  // processing (present in current recursion stack)
            return true;
        
        if(vis[id] == 2) // this check is not mandatory
            return false;

        if(vis[id] == 0){
            vis[id] = 1;
            for(auto edge : adj[id]){
                if(vis[edge]!=2 && iscycle(adj,vis,edge,output))
                    return true;
            }
        }

        output.push_back(id);
        
        vis[id] = 2;  // processed (popping out of current recursion stack)
        return false;
    }
};