class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] !=0 or grid[-1][-1]!=0:
            return -1
        
        n = len(grid)
        d = 1
        q = [(0,0,1)]
        
        while q!=[]:
            
            x,y,d = q.pop(0)
            
            if x==n-1 and y==n-1:
                return d
            
            for i,j in ((x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1) ):
                
                if 0<=i<=n-1 and 0<=j<=n-1 and grid[i][j]==0:
                    grid[i][j] = 1
                    
                    q.append((i,j,d+1))
                    
        return -1
                    
        
        
        
        
        