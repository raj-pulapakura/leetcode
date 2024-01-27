class Solution:
    def removeStars(self, s: str) -> str:
        foundStar = False
        i = 0
        n_stars = 0
        while i < len(s):
            if s[i] == "*":
                foundStar = True
                n_stars += 1
                i += 1
            else:
                if foundStar:
                    # remove n_stars*2 previous chars
                    s = s[:i-n_stars*2] + s[i:]
                    i = i-n_stars*2
                    foundStar = False
                    n_stars = 0
                else:
                    i += 1
        if foundStar: s = s[:i-n_stars*2] + s[i:]
        return s

print(Solution().removeStars("erase*****"))