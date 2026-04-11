class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: # If matrix is empty, do nothing
            return

        rows = len(matrix) 
        cols = len(matrix[0]) # Assumes matrix is not empty thats why we check before

        # Create a 2D grid filles with 0s
        # = Make one row of 0s then repeat that row (row + 10 ) times
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Build prefix sum matrix
        for r in range(rows):
            for c in range(cols):
                # Current cell = 
                # value at matrix[r][c]
                # + sum above
                # + sum to the left
                # - overlap (because it was added twice)
                self.prefix[r+1][c+1] = (
                    matrix[r][c]
                    + self.prefix[r][c+1] # top
                    + self.prefix[r+1][c] # left
                    - self.prefix[r][c] # overlap
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Take the big rectangle up to (row2, col2),
        # then remove the parts we don't want:
        # - everything above row1
        # - everything left of col1
        # + add back the top-left overlap (we removed it twice)
        return (
            self.prefix[row2+1][col2+1]
            - self.prefix[row1][col2+1]
            - self.prefix[row2+1][col1]
            + self.prefix[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)