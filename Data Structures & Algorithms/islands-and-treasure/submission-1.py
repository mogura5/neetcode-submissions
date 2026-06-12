class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # loop through
        rows = len(grid)
        cols = len(grid[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2147483647

        queue = []
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c)) 

        distance = 0
        # call bfs to look around node and find the closest treasure
        # only going through if theres other land
        while queue:
            # process every cell at the current distance level
            for _ in range(len(queue)):
                poprow, popcol = queue.pop(0)
                grid[poprow][popcol] = distance

                for drow, dcol in moves:
                    neighborRow = drow + poprow
                    neighborCol = dcol + popcol

                    if neighborRow < 0 or neighborRow >= rows or neighborCol < 0 or neighborCol >= cols:
                        continue
                    if (neighborRow, neighborCol) in visited:
                        continue
                    if grid[neighborRow][neighborCol] == -1:
                        continue
                    queue.append((neighborRow, neighborCol))
                    visited.add((neighborRow, neighborCol))

            distance += 1