class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        l = s.split()
        res = []
        
        for i in range(len(max(l,key=len))):
            k = ''
            for j in range(len(l)):
                try:
                    k += l[j][i]
                except:
                    k += ' '
            res.append(k.rstrip())
        
        return res