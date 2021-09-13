class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(r):
            
            if visited[r] == 0:
                
                visited[r] = 1
                
                for k in rooms[r]:
                    dfs(k)
                    
        
        n = len(rooms)
        
        visited = [0]*n
        
        dfs(0)
        
        print(visited)
        return 0 not in visited