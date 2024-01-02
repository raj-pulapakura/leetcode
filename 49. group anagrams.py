class Solution:
    def getFreqCount(self, string: str):
        d = {}
        for char in string:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        return d

    def groupAnagrams(self, strs):
        freqMaps = []
        words = []

        for string in strs:
            freqCount = self.getFreqCount(string)
            found = False
            for i, freqMap in enumerate(freqMaps):
                if freqMap == freqCount:
                    words[i].append(string)
                    found = True
                    break
            if not found:
                words.append([string])
                freqMaps.append(freqCount)

        return words


print(Solution().groupAnagrams(["a"]))
        