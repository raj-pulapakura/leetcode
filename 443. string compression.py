class Solution:
    def compress(self, chars: list):
        if len(chars) == 1: return 1

        original_n = len(chars)
        char = ""
        count = 0

        # get counts
        for i in range(0, original_n):
            count += 1
            char = chars[i]

            if i+1 == original_n or char != chars[i+1]:
                if count == 1:
                    chars.append(char)
                else:
                    chars.append(char)
                    chars.extend(str(count))
                count = 0

        # start from back of appendices, and insert to front
        for _ in range(len(chars), original_n, -1):
            chars.insert(0, chars.pop())

        return len(chars)-original_n
            
            
                        



chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(Solution().compress(chars))

print(chars)
[].remove()