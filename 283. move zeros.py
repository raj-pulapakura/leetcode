class Solution:
    def moveZeroes(self, nums:int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZerosFound = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                numZerosFound += 1
            if len(nums) == 0 or i >= len(nums): break
            if nums[i] != 0: i += 1
        for _ in range(numZerosFound):
            nums.append(0)
        

nums = [1, 0]
Solution().moveZeroes(nums)
print(nums)