"""
Constraints

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


class Solution:
    def create_s_chunks(self, s: str) -> list[str]:
        """
        Splits s into chunks of characters.
        Chunks are either individual characters, or contiguous sequences of the same character.

        Examples:

        - "pad"           -> ["p", "a", "d"]
        - "paad"          -> ["p", "aa", "d"]
        - "paaad"         -> ["p", "aaa", "d"]
        - "paaaddgbssx"   -> ["p", "aaa", "dd", "g", "b", "ss", "x"]
        """
        s_chunks = []
        win_start = 0
        win_end = 0
        is_cont = False
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                if is_cont:
                    s_chunks.append(s[win_start:win_end+1])
                    is_cont = False
                else:
                    s_chunks.append(s[i])
            else:
                if is_cont:
                    win_end = i+1
                else:
                    is_cont = True
                    win_start = i
                    win_end = i+1

        if is_cont:
            s_chunks.append(s[win_start:win_end+1])
        else:
            s_chunks.append(s[-1])

        return s_chunks
    
    def create_p_chunks(self, p:str) -> list[str]:
        p_chunks = []
        for i in range(len(p)):
            if p[i] == "*":
                p_chunks.pop()
                p_chunks.append(p[i-1]+"*")
            else:
                p_chunks.append(p[i])
        return p_chunks
        
    def isSubMatch(self, s_chunk: str, p_chunk: str) -> bool:
        if s_chunk == p_chunk: return True
        if "*" in p_chunk and ("." in p_chunk or s_chunk in p_chunk): return True
        if p_chunk == "." and len(s_chunk) == 1: return True
        return False
        

    def isMatch(self, s: str, p: str) -> bool:
        p_chunks = self.create_p_chunks(p)
        print()
        si = 0
        for pi, p_chunk in enumerate(p_chunks):
            check = "" if si >= len(s) else s[si]
            if self.isSubMatch(check, p_chunk):
                if "*" in p_chunk:
                    while self.isSubMatch("" if si >= len(s) else s[si], p_chunk):
                        print(f"{p_chunk} matches with {'' if si >= len(s) else s[si]}")
                        si += 1
                        if si >= len(s):
                            break
                else:
                    print(f"{p_chunk} matches with {'' if si >= len(s) else s[si]}")
                    si += 1
            else:
                if pi != len(p_chunks) - 1: continue
                return self.isSubMatch(check, p_chunk) and si < len(s)
        if si < len(s):
            return False
        return True
        




# print(Solution().isMatch("aa", "a"))
# print(Solution().isMatch("aa", "a*"))
# print(Solution().isMatch("aa", ".*"))
# print(Solution().isMatch("pasta", "pasta"))
# print(Solution().isMatch("pa", "p."))
# print(Solution().isMatch("paa", "p."))
# print(Solution().isMatch("paa", "p.*"))
# print(Solution().isMatch("paa", "p*."))
# print(Solution().isMatch("paa", "p*.*"))
# print(Solution().isMatch("paac", "p.*c"))
# print(Solution().isMatch("paa", "p*.*c"))
# print(Solution().isMatch("mississippi", "mis*is*p*."))
# print(Solution().isMatch("pc", "pa*c"))
print(Solution().isMatch("aaa", "aaaa"))
print(Solution().isMatch("aaa", "a*a"))