class Solution:
    def numIslands(self, grid) -> int:
        cache = []
        m = len(grid)
        n = len(grid[0])

        islands = 0

        def traverse(i, j, prev=None):
            if (i, j) in cache: return
            num = grid[i][j]
            if num == 0:
                cache.append((i, j))
                return

            north, south, west, east = (i-1,j), (i+1,j), (i,j-1), (i,j+1)
            
            if i > 0 and prev != north:
                traverse(north[0], north[1], prev=(i, j))
            if j < n-1 and prev != east:
                traverse(east[0], east[1], prev=(i, j))
            if i < m-1 and prev != south:
                traverse(south[0], south[1], prev=(i, j))
            if j > 0 and prev != west:
                traverse(west[0], west[1], prev=(i, j))

            if (i > 0 or north in cache or prev==north) and (j < n-1 or east in cache or prev==east) and (i < m-1)

            cache.append((i, j))
            return 1


        for i in range(m):
            for j in range(n):
                islands += traverse(i, j)

        return islands

print(Solution().numIslands(
    [["1","1","1","1","0"],
     ["1","1","0","1","0"],
     ["1","1","0","0","0"],
     ["0","0","0","0","0"]]
))