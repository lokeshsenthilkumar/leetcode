class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        d = {keysPressed[0]:releaseTimes[0]}
        
        
        for i in range(1,len(keysPressed)):
            
            if keysPressed[i] in d:
                d[keysPressed[i]] = max(d[keysPressed[i]] , releaseTimes[i] - releaseTimes[i-1])
            else:
                d[keysPressed[i]] = releaseTimes[i] - releaseTimes[i-1]
            
            
        d = sorted(d.items() , key = lambda x : x[0],reverse = 1)
        d = sorted(d , key = lambda x : -x[1])
        
        
        return d[0][0]