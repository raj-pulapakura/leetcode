class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digits = [str(x) for x in range(0, 10)]
        for char in s:
            if char in digits:
                if len(stack)==0 or stack[-1][-1] not in digits:
                    stack.append(char)
                else:
                    stack[-1] = str(stack[-1]) + char
            elif char == "]":
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop() # remove start bracket
                sub = int(stack.pop()) * sub
                stack.append(sub)
            else:
                stack.append(char)
        return "".join(stack)
            

print(Solution().decodeString("100[abc]"))