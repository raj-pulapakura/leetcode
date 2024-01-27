class Solution:
    def longestOnes(self, nums, k: int) -> int:
        i = j = 0
        max_count = 0

        while j < len(nums):
            if nums[j] == 0:
                if k != 0:
                    k -= 1
                    j += 1
                else:
                    foundZero = False
                    while not foundZero:
                        if nums[i] == 0:
                            foundZero = True
                        i += 1

                    j += 1
            else:
                j += 1

            max_count = max(max_count, j-i)

        return max_count
        
print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))