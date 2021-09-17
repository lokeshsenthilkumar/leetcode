class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        points = [0]*(max(nums)+1)
        
        for i in nums:
            points[i]+=i
            
        prev2 = 0 ; prev1 = 0

        for i in points:
            curr = max(prev2+i,prev1)
            prev2 = prev1
            prev1 = curr
            
        return prev1