class Solution:
    def merge(self, intervals):
        i = 0
        j = 1
        res = []

        while True:
            if j == len(intervals):
                res.append([intervals[i][0], intervals[j-1][-1]])
                break
            # if current and previous intervals are overlapping
            if intervals[j][0] <= intervals[j-1][-1]:
                j += 1
            else:
                res.append([intervals[i][0], intervals[j-1][-1]])
                i = j
                j += 1

        return res
    
print(Solution().merge([[1,4],[4,5]]))