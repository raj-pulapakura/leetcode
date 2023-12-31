class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left_prods = [1]
        cum_left_prod = 1
        for i in range(n-1):
            cum_left_prod *= nums[i]
            left_prods.append(cum_left_prod)
        right_prods = [1]
        cum_right_prod = 1
        for i in range(n-1, 0, -1):
            cum_right_prod *= nums[i]
            right_prods.append(cum_right_prod)
        prods = []
        for i in range(n):
            prods.append(left_prods[i]*right_prods[n-1-i])
        return prods


print(Solution().productExceptSelf([1,2,3,4]))