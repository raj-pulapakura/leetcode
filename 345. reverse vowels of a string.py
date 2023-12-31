class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        vowels = ["a", "e", "i", "o", "u"]
        s = list(s)
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                # swap
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
        return "".join(s)
    
print(Solution().reverseVowels("hello"))