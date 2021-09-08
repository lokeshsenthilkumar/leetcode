class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        curr = self
        
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
                
        curr.isEnd = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        res, visit = set(), set()
        
        root = TrieNode()
        
        for w in words:
            root.addWord(w)
            
        r = len(board) ; c = len(board[0])
        
        def dfs(i,j,node,word):
            
            if i<0 or j<0 or i==r or j==c or (i,j) in visit or board[i][j] not in node.children:
                return
            
            visit.add((i,j))
            
            word += board[i][j]
            
            node = node.children[board[i][j]]
            
            if node.isEnd:
                res.add(word)
                
            dfs(i-1,j,node,word)
            dfs(i+1,j,node,word)
            dfs(i,j-1,node,word)
            dfs(i,j+1,node,word)
            
            visit.remove((i,j))
            
            
        for i in range(r):
            for j in range(c):
                dfs(i,j,root,'')
                
        return res