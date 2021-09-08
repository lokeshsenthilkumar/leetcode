class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        r = len(board) ; c = len(board[0])
        path = set()
        
        def dfs(i,j,w):
            
            if w == len(word):
                return True
            if i<0 or j<0 or i>=r or j>=c or board[i][j]!=word[w] or (i,j) in path:
                return False
            
            path.add((i,j))
            
            res =  dfs(i-1,j,w+1) or dfs(i+1,j,w+1) or dfs(i,j-1,w+1) or dfs(i,j+1,w+1)
            path.remove((i,j))
            
            return res
        
        
        for i in range(r):
            for j in range(c):
                if dfs(i,j,0):
                    return True
        return False
    
    