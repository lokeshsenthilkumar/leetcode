class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = [s]
        
        for i in range(len(s)):
            
            c = s[i]
            
            if c.isdigit():
                continue
            
            n = len(res)
            
            for _ in range(n):
                
                
                curr = list(res.pop(0))
                
                curr[i] = curr[i].lower()
                res.append(''.join(curr))
                
                curr[i] = curr[i].upper()
                res.append(''.join(curr))
                
            print(res)
                
        
        return res
                
                
            
        