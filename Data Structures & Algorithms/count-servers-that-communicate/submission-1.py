class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1
        
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if row_count[row] > 1 or col_count[col] > 1:
                        ans += 1
        return ans
