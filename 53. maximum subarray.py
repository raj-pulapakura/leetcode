class Solution:
    def maxSubArray(self, nums) -> int:
        i = j = curr_sum = max_sum = 0
        sub = []

        while j < len(nums):
            num = nums[j]
            sub.append(num)
            if curr_sum < 0 and len(sub) > 1:
                i = j
                j += 1
                sub = nums[i:j]
                curr_sum = num
            else:
                j += 1
                curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum

print(Solution().maxSubArray([1]))