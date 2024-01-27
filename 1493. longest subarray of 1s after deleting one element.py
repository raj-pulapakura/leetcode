class Solution:
    def longestSubarray(self, nums) -> int:
        deleted = False
        i = j = curr_count = max_count = 0

        while j < len(nums):
            if nums[j] == 0:
                if deleted:
                    foundZero = False
                    while not foundZero:
                        if nums[i] == 0:
                            foundZero = True
                        else:
                            curr_count -= 1
                        i += 1
                else:
                    deleted = True
            else:
                curr_count += 1
            j += 1
            max_count = max(max_count, curr_count)

        
        return max_count if deleted else max_count - 1

        
print(Solution().longestSubarray([1,1,1]))