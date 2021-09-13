class Solution:
    def maxDistance(self, mat: List[List[int]]) -> int:
        
        r = len(mat) ; c = len(mat[0])
        q = []
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
                    
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
                    
        while q!=[]:
            
            n = len(q)
            
            for i in range(n):
                curr = q.pop(0)
                
                for d in dirs:
                
                    x = curr[0] + d[0]
                    y = curr[1] + d[1]
                    
                    if x<0 or y<0 or x>r-1 or y>c-1 or mat[x][y]!=-1:
                        continue
                    
                    mat[x][y] = mat[curr[0]][curr[1]] + 1
                    q.append((x,y))
                    
        res =  max(max(i) for i in mat)
        
        
        if res==1 or res==-1:
            return -1
            
        return res-1