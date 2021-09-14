class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        r = len(grid1) ; c = len(grid1[0])
        
        def dfs(i,j):
            
            if i<0 or j<0 or i>r-1 or j>c-1 or grid2[i][j]==0:
                return True
            
            grid2[i][j] = 0
            
            res = grid1[i][j]
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                res &= dfs(i + di, j + dj)
            return res
            
        res = 0
        
        for i in range(r):
            for j in range(c):
                if grid2[i][j] == 1:
                    res += dfs(i,j)
                    
        
        return res