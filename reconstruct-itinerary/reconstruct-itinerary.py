class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = {}
        res = []
        
        for s,d in tickets:
            if s not in graph:
                graph[s] = [d]
            else:
                graph[s].append(d)
                
        for s,adj in graph.items():
            adj.sort(reverse = True)
            
        stack = ['JFK']
        
        while stack!=[]:
            
            top = stack[-1]
            
            if top in graph and graph[top] != []:
                stack.append(graph[top].pop())
            else:
                res.append(stack.pop())
        
        print(res)
        return res[::-1]