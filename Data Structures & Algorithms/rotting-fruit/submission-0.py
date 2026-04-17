class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0]) # Length of row inside grid[0]
        queue = deque() # Stores all the rotten fruit to process
        fresh = 0 # How many fresh fruit exists#

        # Init queue with rotten fruit and count fresh ones
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 2: # Accesses each cell
                    queue.append((row, col)) # Tuple - storing position

                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Down, Up, right, Left

        # BFS, each loop is one minute
        while queue and fresh > 0: # keep going while rotten fruit to spread and fresh ones still exist
            for _ in range(len(queue)): # Number of items currently in queue
                row, col = queue.popleft() # Take one rotten fruit
                
                for dr, dc in directions: # loop through direction pairs
                                nr, nc = row + dr, col + dc # new row and new column
                                # Moves from curr pos to neighbour

                                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                    # If row / col is inside grid, if its a fresh fruit 
                                    grid[nr][nc] = 2
                                    fresh -= 1
                                    queue.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1