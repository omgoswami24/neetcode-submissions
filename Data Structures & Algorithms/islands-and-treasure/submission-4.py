class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        dis = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dis
                
                for dx, dy in directions:
                    nr = dx + row
                    nc = dy + col

                    if nr in range(ROWS) and nc in range(COLS) and ((nr,nc)) not in visited and grid[nr][nc] == 2147483647:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            
            dis += 1







        