class Solution:
    def letterCombinations(self, digits: str):
        if digits=="": return []

        results = []

        digitMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def gen(comb, di, mi):
            if len(comb)==len(digits):
                results.append(comb)
                return

            for children in digitMap[digits[di]]:
                comb += children
                gen(comb, di+1, mi)
                comb = comb[:-1]

        gen("", 0, 0)
        return results

print(Solution().letterCombinations(""))