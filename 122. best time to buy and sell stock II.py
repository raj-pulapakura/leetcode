class Solution:
    def maxProfit(self, prices) -> int:
        totalProfit = 0
        i, j = 0, 1

        while j < len(prices):
            buy = prices[i]
            sell = prices[j]
            profit = sell - buy
            if profit < 0:
                i = j
            else:
                totalProfit += profit
                i += 1
            j += 1

        return totalProfit

print(Solution().maxProfit([7, 6, 4, 3, 1]))