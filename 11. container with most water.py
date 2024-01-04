class Solution:
    def maxArea(self, height: int) -> int:
        if len(height)==2: return min(height)

        i = 0
        j = len(height)-1
        area = 0

        while j - i > 0:
            area = max(area, (j-i)*min(height[i], height[j]))



            left_min = min(height[i], height[i+1], height[j])
            right_min = min(height[i], height[j-1], height[j])
            if left_min > right_min:
                i += 1
            elif left_min < right_min:
                j -= 1
            else:
                if height[i] >= height[j]:
                    j -= 1
                else:
                    i += 1

        return area
    
print(Solution().maxArea([1,3,2,5,25,24,5]))