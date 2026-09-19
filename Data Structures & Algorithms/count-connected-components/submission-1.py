class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #convert to a adjacency list

        def dfs(node):
            stack = []
            stack.append(node)

            while stack:
                n = stack.pop()

                for nei in adj[n]:
                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)

        adj = {}
        visited = set()
        count = 0

        for i in range(n):
            adj[i] = []

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        for node in adj:
            if node not in visited:
                dfs(node)
                count += 1
        
        return count

        


        

        

        