class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        moves = [[1, 0], [-1, 0], [0,1], [0,-1]]
        
        def bfs(row, col):

            # base case
            grid[row][col] = 0
            queue = []
            queue.append((row, col))
            maxArea = 1

            while queue:
                poprow, popcol = queue.pop()

                for (drow, dcol) in moves:
                    r = drow + poprow
                    c = dcol + popcol

                    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                        continue
                    grid[r][c] = 0
                    queue.append((r, c))
                    maxArea += 1
            
            return maxArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea