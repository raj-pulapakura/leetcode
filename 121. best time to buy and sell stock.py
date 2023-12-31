class Solution:
    def maxProfit(self, prices) -> int:

        ### O(n^2) solution
        #
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         maxProfit = max(maxProfit, prices[j]-prices[i])
        # return maxProfit

        # O(n) solution
        maxProfit = 0
        i, j = 0, 1

        while j < len(prices):
            maxProfit = max(maxProfit, prices[j]-prices[i])
            if prices[i] >= prices[j]:
                i = j
            j += 1

        return maxProfit

print(Solution().maxProfit([7, 1, 5, 3, 6, 4])) # max profit is between 5 (between 1 and 6)
print(Solution().maxProfit([7, 6, 4, 3, 1])) # max profit is 0