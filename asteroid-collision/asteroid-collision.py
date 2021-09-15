class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        
        st = []
        
        # if a==[1,-2,-2,-2]:
        #     return [-2,-2,-2]
        
        for i in range(len(a)):
            
            if a[i] > 0:
                st.append(a[i])
            elif a[i] < 0:
                if st==[] or (st[-1]<0 and a[i]<0):
                    st.append(a[i])

                while st!=[] and st[-1] > 0 and a[i] < 0:
                    
                    k = 0
                    if st[-1] < abs(a[i]):
                        k = st[-1]
                        st.pop()
                        
                    elif st[-1] == abs(a[i]):
                        st.pop()
                        break
                    
                    # if st==[]:
                    #     continue
                    
                    if (k != abs(a[i])) and (st==[] or (st[-1]<0 and a[i]<0)):
                        st.append(a[i])
                            
                            
                    if k == 0:
                        break
                        
        return st
        