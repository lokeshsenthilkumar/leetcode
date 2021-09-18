class Solution:
    def findOriginalArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        if n%2:
            return []
        
        nums.sort()
        
        res = []
        
        d = Counter(nums)
        
        for i in nums:
            if d[i] != 0 and d[i*2]!=0:
                res.append(i)
                d[i] -= 1
                d[i*2] -= 1
                
            elif d[i]!=0:
                return []
            
        return res
                
        
        
        