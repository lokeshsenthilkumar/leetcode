class Solution:
    def simplifyPath(self, path: str) -> str:
        
        l = path.split('/')
        L = []
        
        for i in l:
            if i=='' or i=='.':
                continue
            L.append(i.strip('/'))
              
        st = [] 
        
        for i in L:
            if st==[] and i=='..':
                continue
            elif i == '..':
                st.pop()
            else:
                st.append(i)
        
        return ('/'+'/'.join(st))
        