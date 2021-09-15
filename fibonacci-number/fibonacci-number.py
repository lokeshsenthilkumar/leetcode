class Solution:
    def fib(self, n: int) -> int:
        
        a = 0 ; b = 1
        
        for i in range(n):
            p = a
            a = a + b
            b = p
            
        return a
            
        
        