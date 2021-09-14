class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        email_to_name = {}
        parent = {}
        
        def find(x):
            return x if parent[x]==x else find(parent[x])
        
        def union(i,j):
            parent[find(j)] = find(i)
        
        parent = {}
        
        for account in accounts:
            
            username = account[0]
            
            for email in account[1:]:
                
                if email not in parent:
                    parent[email] = email
                
                email_to_name[email] = username
                
                union(account[1],email)
                
        
        forest = defaultdict(list)
        
        for i in parent.keys():
            forest[find(i)].append(i)
            
        print(forest)
        
        res = []
        
        for i in forest:
            k = [email_to_name[i]]
            
            for j in sorted(forest[i]):
                k.append(j)
            
            res.append(k)
    
        return res