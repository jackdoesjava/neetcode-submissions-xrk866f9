class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(rows):
            for col in range(cols):
                # Found a new island
                if grid[row][col] == 1 and (row, col) not in visited:
                    curr_area = 0
                    queue = deque([(row, col)]) # Fix 1: Tuple in list
                    visited.add((row, col))

                    while queue:
                        curr_r, curr_c = queue.popleft()
                        curr_area += 1

                        for dr, dc in directions: # Fix 2: Spelling
                            nr, nc = curr_r + dr, curr_c + dc

                            if (0 <= nr < rows and 
                                0 <= nc < cols and 
                                grid[nr][nc] == 1 and 
                                (nr, nc) not in visited):
                                
                                queue.append((nr, nc))
                                visited.add((nr, nc))
                    
                    # Fix 3: Indentation (Update after BFS finishes)
                    max_area = max(max_area, curr_area)
                        
        return max_area