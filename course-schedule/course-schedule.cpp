class Solution {
public:
    
    bool canFinish(int n, vector<vector<int>>& pre) {
        
        vector<int> adj[n];
        
        for(auto edge : pre)
            adj[edge[0]].push_back(edge[1]);
        
        vector<int> vis(n,0);
        
        for(int i=0;i<n;i++){
            if(iscycle(adj,vis,i))
                return false;
        }
        return true;
    }
    
    bool iscycle(vector<int> adj[],vector<int> &vis,int id){
        
        if(vis[id]==1)
            return true;

        if(vis[id]==0){
            vis[id]=1;
            for(auto edge : adj[id]){
                if(vis[edge]!=2 && iscycle(adj,vis,edge))
                    return true;
            }
        }

        vis[id] = 2;
        return false;
    }
};