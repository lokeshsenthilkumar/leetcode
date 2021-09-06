class Solution:
    def findNthDigit(self, n: int) -> int:
        
        base = 9 ; digits = 1
        
        while n - (base * digits) > 0:
            
            n -= base * digits
             
            base *= 10
            
            digits += 1
            
        
        print(n,digits)
        
        index = n % digits
        
        if n % digits == 0:
            index = digits 
            
        print(index)
        
        start = 10**(digits-1)   
        
        print(start)
        
        start += (n // digits) - 1 if index==digits else (n // digits)
        
        print(start)
        
        print(n % digits)
        
        return int(str(start)[(n % digits) - 1])
        