class Solution:
    def findNthDigit(self, n: int) -> int:
        
        base = 9 ; digits = 1
        
        while n - (base * digits) > 0:
            
            n -= base * digits
            base *= 10
            digits += 1
            
        
        index = (n-1) % digits
        
        offset = (n-1) // digits
            
        start = 10**(digits-1)   
        
        start += offset
        
        print(start,offset,index)
        
        return int(str(start)[index])
        