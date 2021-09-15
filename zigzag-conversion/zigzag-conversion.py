class Solution:
    def convert(self, s: str, n: int) -> str:
        
        if n == 1: return s
        
        res = ''
        inc = (n-1)*2 
        
        for i in range(n):
            
            for j in range(i, len(s), inc):
                res += s[j]
                
                if i>0 and i<n-1 and j + inc - 2 * i < len(s):
                    res += s[j + inc - 2 * i]
            
        return res                
                
