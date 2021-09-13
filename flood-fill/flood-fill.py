class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        if grid[sr][sc] == newColor:
            return grid
        
        def dfs(i,j):
            
            if i<0 or j<0 or i==r or j==c or grid[i][j]!=start:
                return 
            
            grid[i][j] = newColor
            
            dfs(i-1,j) , dfs(i+1,j) , dfs(i,j-1) , dfs(i,j+1)
        
        r = len(grid) ; c = len(grid[0])
        
        start = grid[sr][sc]
        
        res = 0        
                
        dfs(sr,sc)
                
        return grid