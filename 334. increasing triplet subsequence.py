class Solution:
    def increasingTriplet(self, nums):
        curr_min = 2 ** 31 - 1
        curr_max = - (2 ** 31)
        cache = [[] for _ in range(len(nums))]
        for i in range(len(nums)):
            cache[i].append(curr_min)
            curr_min = min(curr_min, nums[i])
        for i in range(len(nums)-1, -1, -1):
            cache[i].append(curr_max)
            curr_max = max(curr_max, nums[i])

        for i in range(len(nums)):
            if cache[i][0] < nums[i] < cache[i][1]:
                return True
            
        return False
    
print(Solution().increasingTriplet([20,100,10,12,5,13]))
