class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        if k == 1: return max(nums)

        moving_avg = 0
        max_avg = -(10**4)-1
        i = 0
        j = k
        while j <= len(nums):
            if i == 0:
                moving_avg = sum(nums[i:j]) / k
                max_avg = max(max_avg, moving_avg)
            else:
                moving_avg = (moving_avg * k - nums[i-1] + nums[j-1]) / k
                max_avg = max(max_avg, moving_avg)
            i += 1
            j += 1
        return max_avg

print(Solution().findMaxAverage([0,1,1,3,3], 4))