class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        r = len(board) ; c = len(board[0])
        
        def dfs(i,j):
            if i<0 or j<0 or i==r or j==c or board[i][j]!='O':
                return
            
            board[i][j] = 'B'
            
            dfs(i-1,j) , dfs(i+1,j) , dfs(i,j-1) , dfs(i,j+1)
                
        
        for i in range(r):
            for j in range(c):
                if i*j == 0 or i == r-1 or j == c-1:
                    dfs(i,j)
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                
        