class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}   #get the frequency of the words
        for word in words:
            if word in freq: freq[word] += 1
            else: freq[word] = 1
        #using anonymus lambda function it is easier to sort dictionary by its value
        temp1 = sorted(freq,key =lambda word:(-freq[word], word)) #the negative is to sort in descending order and if two wrods have same frequency we sort them by lexicography
        res = []
        for i in range(k):
            res.append(temp1[i])
        return res
        
