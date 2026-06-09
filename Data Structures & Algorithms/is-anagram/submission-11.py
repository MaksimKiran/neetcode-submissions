class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMapS, hashMapT = {}, {}

        for ch in s:
            hashMapS[ch] = hashMapS.get(ch,0) + 1
        for ch in t:
            hashMapT[ch] = hashMapT.get(ch,0) + 1

        return hashMapS == hashMapT



