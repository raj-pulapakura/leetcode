class Solution:
    def reverseWords(self, s: str) -> str:
        i = j = len(s) - 1
        words = []
        onword = False
        while j >= 0:
            if onword:
                if s[j] == " " or j == 0:
                    onword = False
                    if s[j] == " " and j == 0:
                        words.append(s[1:i+1])
                    elif s[j] == " ":
                        words.append(s[j+1:i+1])
                    elif j == 0:
                        words.append(s[j:i+1])
                    j -= 1
                    i = j
                else:
                    j -= 1
            else:
                if s[j] == " ":
                    j -= 1
                    i -= 1
                else:
                    onword = True
                    j -= 1

        if i == 0 and j == -1 and s[i] != " ":
            words.append(s[i])
        return " ".join(words)

print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords("the sky  is blue"))
print(Solution().reverseWords("a good   example"))
print(Solution().reverseWords(" asdasd df f"))