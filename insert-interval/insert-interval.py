class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval);
        intervals.sort(key=lambda x:x[0])
        
        res = 0
                
        for i in range(1,len(intervals)):
            
            if intervals[res][1] >= intervals[i][0]:
                intervals[res][0] = min(intervals[res][0],intervals[i][0])
                intervals[res][1] = max(intervals[res][1],intervals[i][1])
            else:
                res += 1
                intervals[res] = intervals[i]
                
        return intervals[:res+1]
        