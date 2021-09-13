class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            
            if i<0 or j<0 or i==r or j==c or grid[i][j]!=0:
                return 
            
            grid[i][j] = 1
            
            dfs(i-1,j) , dfs(i+1,j) , dfs(i,j-1) , dfs(i,j+1)
        
        r = len(grid) ; c = len(grid[0])
        
        for  i in range(r):
            for j in range(c):
                if i*j==0 or i==r-1 or j==c-1:
                    dfs(i,j)
                
        res = 0        
                
        for  i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i,j)
                
        return res