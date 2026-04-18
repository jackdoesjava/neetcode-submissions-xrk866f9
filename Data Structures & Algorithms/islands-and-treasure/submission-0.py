class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))

        # Phase 2: The BFS Engine
        dist = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while queue:
            # We process level-by-level (all nodes at distance 'dist')
            for i in range(len(queue)):
                row, col = queue.popleft()
                
                # Update the grid with the current distance
                grid[row][col] = dist
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    # Boundary Check + Wall Check + Visited Check
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] != -1 and 
                        (nr, nc) not in visited):
                        
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            # Increment distance for the next layer of neighbors
            dist += 1