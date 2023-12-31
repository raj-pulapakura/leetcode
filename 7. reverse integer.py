class Solution:
    def reverse(self, x: int) -> int:
        positive = x >= 0
        x = int("".join(reversed(str(abs(x)))))
        if positive:
            if x > (2**31)-1:
                return 0
            else:
                return x
        else:
            if -x < -(2**31):
                return 0
            else:
                return -x
            
print(Solution().reverse(-2147483648))