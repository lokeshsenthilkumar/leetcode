class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        d = defaultdict(int)
        
        for i in text:
            if i in 'balloon':
                d[i] += 1
                
        d['l'] //= 2
        d['o'] //= 2
        
        if len(d) == 5:
            return min(i for i in d.values())
        return 0