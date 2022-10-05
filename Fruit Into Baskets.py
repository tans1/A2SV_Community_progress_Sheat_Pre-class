class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first =last= 0
        temp_dic = {}
        max_len = 0
        while last < len(fruits):
            temp_dic[fruits[last]] = last
            if len(temp_dic) >= 3:
                head_slide = min(temp_dic.values())
                del temp_dic[fruits[head_slide]]
                first = head_slide + 1
            max_len = max(max_len,last-first+1)
            last += 1
        return max_len
