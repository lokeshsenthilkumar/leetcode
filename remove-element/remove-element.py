class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        nk = 0
        
        for i in range(len(nums)):
            
            if nums[i] != val:
                nums[nk] = nums[i]
                nk += 1
        
        return nk
        