class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        for ch in s:
            if ch not in hashMapS:
                hashMapS[ch] = 1
            else:
                hashMapS[ch] += 1

        hashMapT = {}
        for ch in t:
            if ch not in hashMapT:
                hashMapT[ch] = 1
            else:
                hashMapT[ch] += 1
                
        if hashMapS.keys() != hashMapT.keys():
            return False

        for key in hashMapS.keys():
            if hashMapS.get(key) != hashMapT.get(key):
                return False
        return True



