class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        P = Counter(p)
        temp_dic = Counter(s[:len(p)-1])
        for indx,char in enumerate(s[len(p)-1:]):
            temp_dic[char] += 1
            if temp_dic == P:
                res.append(indx)
            temp_dic[s[indx]] -= 1
            if not temp_dic[s[indx]]:  #for dictionary if its value is zero, it is counted as it doesnt exist
                del temp_dic[s[indx]]
        return res
        
       
