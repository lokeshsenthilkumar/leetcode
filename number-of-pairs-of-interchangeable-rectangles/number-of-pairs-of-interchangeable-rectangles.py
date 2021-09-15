class Solution:
    def interchangeableRectangles(self, r: List[List[int]]) -> int:
        
        res = 0 
        
        d = defaultdict(int)
        
#         for i in range(len(r)):
#             d[r[i][0]/r[i][1]] += 1
        
#         for i in d.values():
#             res += (i*(i-1))//2

        for i in range(len(r)):
            res += d[r[i][0]/r[i][1]] 
            d[r[i][0]/r[i][1]] += 1
            
        
    
        return res
    
        