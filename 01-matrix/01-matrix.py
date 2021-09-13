#BFS
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
#         r = len(mat) ; c = len(mat[0])
#         q = []
        
#         for i in range(r):
#             for j in range(c):
#                 if mat[i][j] == 0:
#                     q.append((i,j))
#                 else:
#                     mat[i][j] = -1
                    
#         dirs = [(-1,0),(1,0),(0,-1),(0,1)]
                    
#         while q!=[]:
            
#             n = len(q)
            
#             for i in range(n):
#                 curr = q.pop(0)
                
#                 for d in dirs:
                
#                     x = curr[0] + d[0]
#                     y = curr[1] + d[1]
                    
#                     if x<0 or y<0 or x>r-1 or y>c-1 or mat[x][y]!=-1:
#                         continue
                    
#                     mat[x][y] = mat[curr[0]][curr[1]] + 1
#                     q.append((x,y))
            
#         return mat

#DP

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        r = len(mat) ; c = len(mat[0])
        INF = r+c 
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] != 0:
                    top = INF ; left = INF
                    
                    if i-1 >= 0:
                        top = mat[i-1][j]
                    if j-1 >= 0:
                        left = mat[i][j-1]
                    
                    mat[i][j] = min(top+1,left+1)
                    
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if mat[i][j] != 0:
                    bottom = INF ; right = INF
                    
                    if i+1 <= r-1:
                        bottom = mat[i+1][j]
                    if j+1 <= c-1:
                        right = mat[i][j+1]
                    
                    
                    mat[i][j] = min({mat[i][j],bottom+1,right+1})
        
        
        return mat