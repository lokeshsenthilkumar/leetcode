class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 1 ; h = x
        res = 0
        
        while l<=h:
            
            mid = (l+h)//2
            
            if mid*mid == x:
                return mid
            
            elif mid*mid > x:
                h = mid - 1
            
            else:
                l = mid + 1
                res = mid
                
        return res