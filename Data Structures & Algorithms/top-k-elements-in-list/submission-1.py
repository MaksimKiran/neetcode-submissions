class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        pairs = []
        for key in hashMap:
            pair = [key, hashMap[key]]
            pairs.append(pair)
        pairs.sort(key=lambda x: x[1], reverse=True)
        outputList = []
        for i in range(0, k):
            outputList.append(pairs[i][0])
        return outputList