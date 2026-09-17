class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # classic BFS problem where you traverse starting at rotten 
        # fruit and you keep going until Q is empty. Then you do a linear
        # search to see if any fresh fruit remain. If not, return the time 
        # elapsed, else return -1.
        from collections import deque

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visited = set()

        time = -1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col))
                    visited.add((row,col))
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            total = len(q)
            for i in range(total):
                row, col = q.popleft()
                grid[row][col] = 2
                for d in direction:
                    dx = d[0] + row
                    dy = d[1] + col

                    if dx in range(ROWS) and dy in range(COLS) and (dx,dy) not in visited and grid[dx][dy] == 1:
                        q.append((dx,dy))
                        visited.add((dx,dy))
            time += 1
            

        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        
        return time if time>0 else 0


                        








        