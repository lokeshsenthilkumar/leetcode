class Solution:
    def rob(self, nums: List[int]) -> int:
        
        p2 = 0 ; p1 = 0
        
        for i in range(len(nums)):
            p2 , p1 = p1 , max(p1, p2+nums[i])
        
        return p1
        