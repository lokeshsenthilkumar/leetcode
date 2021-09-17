class Solution:
    def climbStairs(self, n: int) -> int:
        
        p2 = 1 ; p1 = 1
        
        for i in range(2,n+1):
            
            p2, p1 = p1 , p1+p2
            
        return p1
        