def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0: return 0
    if len(s) == 1: return 1
    max_len = 1
    sub = s[0]
    i = 0
    j = 1
    while i != len(s):
        sub = s[i:j]
        if j == len(s) or s[j] in sub:
            # there is a duplicate
            max_len = max(max_len, len(sub))
            i += 1
        else:
            if j < len(s): 
                j += 1
            else:
                i += 1
    return max_len

lengthOfLongestSubstring("au")