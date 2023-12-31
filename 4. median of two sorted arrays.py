import math

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    t = m + n
    if t % 2 == 1:
        endpos = math.floor(t/2)
    else:
        startpos = math.floor(t/2) - 1
        endpos = math.floor(t/2)

    if m == 0:
        if t % 2 == 1:
            return nums2[endpos]
        else:
            return (nums2[startpos]+nums2[endpos]) / 2
    if n == 0:
        if t % 2 == 1:
            return nums1[endpos]
        else:
            return (nums1[startpos]+nums1[endpos]) / 2

    i, j, nums = 0, 0, []
    
    while len(nums)-1 < endpos:
        if i == m:
            nums.append(nums2[j])
            j += 1
        elif j == n:
            nums.append(nums1[i])
            i += 1
        elif nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            nums.append(nums2[j])
            j += 1
        else:
            nums.append(nums1[i])
            nums.append(nums2[j])
            i += 1
            j += 1
    
    if t % 2 == 1:
        return nums[endpos]
    else:
        return (nums[startpos] + nums[endpos]) / 2

print(findMedianSortedArrays([1], [2, 3, 4]))