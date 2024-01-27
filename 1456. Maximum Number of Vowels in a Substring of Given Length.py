class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = k

        running_vowel_count = 0
        max_vowel_count = 0
        vowels = ["a", "e", "i", "o", "u"]

        while j <= len(s):
            sub = s[i:j]
            if i == 0:
                running_vowel_count = sum([sub.count(vowel) for vowel in vowels])
                max_vowel_count = max(max_vowel_count, running_vowel_count)
            else:
                if s[i-1] in vowels:
                    running_vowel_count -= 1
                if s[j-1] in vowels:
                    running_vowel_count += 1
                max_vowel_count = max(max_vowel_count, running_vowel_count)

            if max_vowel_count == k:
                return k
            i += 1
            j += 1

        return max_vowel_count

print(Solution().maxVowels("weallloveyou", 7))