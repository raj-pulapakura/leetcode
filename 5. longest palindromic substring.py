class Solution:
    def expandFromMiddle(self, s:str, left:int, right:int)->int:
        if s is None or len(s) < 1 or left > right: return ""

        while left >= 0 and right < len(s) and s[left]==s[right]:
            left -= 1
            right += 1

        return right - left - 1

    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expandFromMiddle(s, i, i)
            len2 = self.expandFromMiddle(s, i, i+1)
            maxlen = max(len1, len2)
            if maxlen > end-start:
                start = i - int((maxlen-1)/2)
                end = i + int(maxlen/2)

        return s[start:end+1]

sol = Solution()
# print(sol.longestPalindrome("abbcccbbbcaaccbababcbcabca"))
print(sol.longestPalindrome("cbbt"))