class Solution:
    def numIslands(self, grid) -> int:
        cache = []
        m = len(grid)
        n = len(grid[0])

        islands = 0

        def traverse(i, j, prev_stack):

            if (i, j) in cache: return 0
            num = grid[i][j]
            if num == "0":
                if len(prev_stack) != 0: prev_stack.pop()
                cache.append((i, j))
                return 0

            north, south, west, east = (i-1,j), (i+1,j), (i,j-1), (i,j+1)
            
            if i > 0 and north not in prev_stack:
                prev_stack.append((i, j))
                traverse(north[0], north[1], prev_stack)
            if j < n-1 and east not in prev_stack:
                prev_stack.append((i, j))
                traverse(east[0], east[1], prev_stack)
            if i < m-1 and south not in prev_stack:
                prev_stack.append((i, j))
                traverse(south[0], south[1], prev_stack)
            if j > 0 and west not in prev_stack:
                prev_stack.append((i, j))
                traverse(west[0], west[1], prev_stack)

            if len(prev_stack) != 0: prev_stack.pop()

            if (
                (i == 0 or north in cache or north in prev_stack) and 
                (j == n-1 or east in cache or east in prev_stack) and 
                (i == m-1 or south in cache or south in prev_stack) and 
                (j == 0 or west in cache or west in prev_stack)
            ):
                cache.append((i, j))

            if (
                (i == 0 or north in cache) and 
                (j == n-1 or east in cache) and 
                (i == m-1 or south in cache) and 
                (j == 0 or west in cache)
            ):
                return 1
            return 0

        for i in range(m):
            for j in range(n):
                prev_stack = []
                islands += traverse(i, j, prev_stack)

        return islands
    

    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        islands = 0
        visited = []

        for i in range(m):
            for j in range(n):
                queue = [(i, j)]

                while len(queue) != 0:
                    v = queue.pop()
                    if v in visited or grid[v[0]][v[1]] == "0":
                        continue

                    visited.append(v)
                    i, j = v[0], v[1]

                    north, south, west, east = (i-1,j), (i+1,j), (i,j-1), (i,j+1)

                    if i > 0 and north not in visited and north not in queue and grid[north[0]][north[1]] != "0":
                        queue.insert(0, north)
                    if j < n-1 and east not in visited and east not in queue and grid[east[0]][east[1]] != "0":
                        queue.insert(0, east)
                    if i < m-1 and south not in visited and south not in queue and grid[south[0]][south[1]] != "0":
                        queue.insert(0, south)
                    if j > 0 and west not in visited and west not in queue and grid[west[0]][west[1]] != "0":
                        queue.insert(0, west)

                    if len(queue)==0: 
                        islands += 1
                        print(v)

        return islands



print(Solution().numIslands(
    [["1","1","1","1","0"],
     ["1","1","0","1","0"],
     ["1","1","0","0","0"],
     ["0","0","0","0","0"]]
))

# print(Solution().numIslands(
#     [["1","1","0","0","0"],
#      ["1","1","0","0","0"],
#      ["0","0","1","0","0"],
#      ["0","0","0","1","1"]]
    
# ))