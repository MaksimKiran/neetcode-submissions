class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string = string + str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        list = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            wordLength = int(s[i:j])
            word = s[j + 1: j + 1 + wordLength]
            list.append(word)
            i = j + 1 + wordLength

        return list

