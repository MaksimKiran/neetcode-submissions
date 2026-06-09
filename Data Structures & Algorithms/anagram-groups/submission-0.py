class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            charToFreq = [0] * 26
            for c in s:
                charToFreq[ord(c)-ord('a')] += 1
            if tuple(charToFreq) not in hashMap.keys():
                hashMap[tuple(charToFreq)] = [s]
            else:
                hashMap[tuple(charToFreq)].append(s)
        return list(hashMap.values())