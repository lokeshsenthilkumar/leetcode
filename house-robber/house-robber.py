class Solution:
    def rob(self, nums: List[int]) -> int:
        
        p2 = p1 = 0
        
        for i in range(len(nums)):
            
            t = p1
            p1 = max(p1, nums[i]+p2)
            p2 = t
	        
        return p1
        
       