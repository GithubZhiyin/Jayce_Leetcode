class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        parents = [i for i in range(n)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            rx, ry = find(parents[x]), find(parents[y])
            if rx != ry:
                parents[rx] = ry

        edge_num = len(connections)
        if edge_num < n - 1:
            return -1

        for pair in connections:
            union(pair[0], pair[1])
        
        components = sum(1 for i in range(n) if find(i) == i)
        return components - 1
    
        
        
        
        

                

                
        