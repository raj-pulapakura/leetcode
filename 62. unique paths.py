class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def traverse(i, j, total_paths):
            if i == m-1 and j == n-1:
                return total_paths + 1 

            if (m-i, n-j) in memo:
                return total_paths + memo[(m-i, n-j)]
            
            if (n-j, m-i) in memo:
                return total_paths + memo[(n-j, m-i)]
            
            prev_total_paths = total_paths

            if i < m-1:
                total_paths = traverse(i+1, j, total_paths)

            if j < n-1:
                total_paths = traverse(i, j+1, total_paths)

            memo[(m-i, n-j)] = total_paths - prev_total_paths
            memo[(n-j, m-i)] = total_paths - prev_total_paths

            return total_paths

        return traverse(0, 0, 0)

    
print(Solution().uniquePaths(3, 3))