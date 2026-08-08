class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        distance = 0
        while q:
            n = len(q)
            for _ in range(n):
                row, col = q.popleft()
                visited.add((row,col))
                grid[row][col] = distance

                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and grid[nr][nc] != -1:
                        q.append((nr,nc))
                        visited.add((nr,nc))


            distance += 1


        