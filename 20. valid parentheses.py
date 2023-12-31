class Solution:
    def isValid(self, s: str) -> bool:
        openP, closedP, openC, closedC, openS, closedS = 0, 0, 0, 0, 0, 0

        matchStack = []

        for i in range(len(s)):
            x = s[i]
            if x == "(": 
                openP += 1
                matchStack.append("(")
            if x == "{": 
                openC += 1
                matchStack.append("{")
            if x == "[": 
                openS += 1
                matchStack.append("[")
            if x == ")":
                if i == 0 or openP <= closedP or matchStack[-1] != "(": return False
                if s[i-1] == "(" or s[i-1] in [")", "}", "]"]:
                    closedP += 1
                    matchStack.pop()
                else: return False
            if x == "}":
                if i == 0 or openC <= closedC or matchStack[-1] != "{": return False
                if s[i-1] == "{" or s[i-1] in [")", "}", "]"]:
                    closedC += 1
                    matchStack.pop()
                else: return False
            if x == "]":
                if i == 0 or openS <= closedS or matchStack[-1] != "[": return False
                if s[i-1] == "[" or s[i-1] in [")", "}", "]"]:
                    closedS += 1
                    matchStack.pop()
                else: return False
        return openP == closedP and openC == closedC and openS == closedS
    
print(Solution().isValid("[([]])"))