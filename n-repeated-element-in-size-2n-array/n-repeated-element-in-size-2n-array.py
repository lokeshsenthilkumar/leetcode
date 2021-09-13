class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        while 1:
            r = random.sample(nums,2)
            if r[0]==r[1]:
                return r[0]
        