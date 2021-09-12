class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        
        def dfs(node,time):
            
            nonlocal ans
            
            ans = max(ans, time)
            
            for child in graph[node]:
                dfs(child,time + informTime[node])
            
        
        
        graph = defaultdict(list)
        
        for e,m in enumerate(manager):
            graph[m].append(e)
        
        ans = 0
            
        dfs(headID,0)
        
        return ans