class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        n_max = 0
        for i in range(len(flowerbed)):
            if (i==0 or flowerbed[i-1]==0) and (i+1==len(flowerbed) or flowerbed[i+1]==0) and flowerbed[i]!=1:
                n_max += 1
                flowerbed[i]=1
        return n <= n_max
    
print(Solution().canPlaceFlowers([1,0,0,0,0,0,1], 2))