class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        m = [[] for _ in range(numRows)]
        backtrack = False
        i = 0
        for x in range(n):
            l = s[x]
            m[i].append(l)
            if i == numRows - 1:
                backtrack = True
            if backtrack:
                i -= 1
                if i == 0: backtrack = False
            else:
                i += 1
        z = "".join(["".join(r) for r in m])
        return z


print(Solution().convert("ABC", 1))