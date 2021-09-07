class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x:x[1])
        
        end = points[0][1]
        
        c = 1
        
        for i in range(1,len(points)):
            if points[i][0] > end:
                c += 1 
                end = points[i][1]
            
        return c
        