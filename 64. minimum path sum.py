class Solution:
    def minPathSum(self, grid) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        row = [0] * n_cols

        for r in range(n_rows-1, -1, -1):
            for c in range(n_cols-1, -1, -1):
                if c == n_cols-1 and r == n_rows-1:
                    row[c] = grid[r][c] + row[c]
                elif r == n_rows-1:
                    row[c] = grid[r][c] + row[c+1]
                elif c == n_cols-1:
                    row[c] = grid[r][c] + row[c]
                else:
                    row[c] = min(grid[r][c]+row[c], grid[r][c]+row[c+1])
            print(row)
        return row[0]

print(Solution().minPathSum([[1,2,3],[4,5,6]]))