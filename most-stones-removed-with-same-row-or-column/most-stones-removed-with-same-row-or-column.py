class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        n = len(stones)
        visited = set()
        islands = 0
        
        def dfs(i):
            
            if i not in visited:
                visited.add(i)

                for j in range(n):

                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                        nonlocal islands
                        dfs(j)
        
        for i in range(n):
            if i not in visited:
                islands += 1
                dfs(i)
                
        print(islands)
        return n - islands