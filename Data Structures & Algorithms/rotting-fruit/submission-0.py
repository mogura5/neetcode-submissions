class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        moves = [[1,0], [0,1], [-1,0], [0,-1]]
        output = 0
        freshCount = 0
        queue = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshCount += 1

        while queue and freshCount > 0:

            for _ in range(len(queue)):

                poprow, popcol = queue.pop(0)

                for (dr, dc) in moves:
                    drow = poprow + dr
                    dcol = popcol + dc

                    if 0 <= drow < rows and 0 <= dcol < cols and grid[drow][dcol] == 1:
                        grid[drow][dcol] = 2
                        freshCount -= 1
                        queue.append((drow, dcol))
            output += 1

        if freshCount != 0:
            return -1
        else:
            return output
        