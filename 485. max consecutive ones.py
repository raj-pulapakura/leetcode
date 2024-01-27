class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_cons = 0

        i = 0
        j = 0
        while j <= len(nums):
            if j != len(nums) and nums[j] == 1:
                j += 1
            else:
                max_cons = max(max_cons, j-i)
                j += 1
                i = j
        return max_cons
    
print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]))