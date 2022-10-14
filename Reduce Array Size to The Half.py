class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        k = len(arr) / 2
        temp1 = Counter(arr)
        freq = []
        for i in temp1.items():
            freq.append(list(i))
        freq.sort(key=lambda x:-x[1])
        summ = i = count = 0
        while summ < k and i < len(freq):
            summ += freq[i][1]
            count += 1
            i += 1
        return count
