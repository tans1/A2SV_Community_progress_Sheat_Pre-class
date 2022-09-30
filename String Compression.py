class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        while fast < len(chars):
            chars[slow] = chars[fast]
            count = 1
            
            while fast + 1 < len(chars) and chars[fast] == chars[fast+1]:
                fast += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[slow+1] = c
                    slow += 1

            fast += 1
            slow += 1
        return slow
        
########## the following code works in IDLE , but not leetcode , I dont know why it didn't work on leetcode
        ind = [0]
        tempdic = {}
        for i in ind:
            counter = 0
            tempdic[chars[i]] = 1
            for j in range(i+1,len(chars)):
                if chars[j] == chars[i]:
                    tempdic[chars[i]] += 1
                elif counter < 1:
                    counter +=1
                    ind.append(j)
        output = []
        for char in tempdic:
            output.append(char)
            if tempdic[char] > 1:
                i = 0
                tempstr = str(tempdic[char])
                while i < len(tempstr):
                    output.append(tempstr[i])
                    i +=1
        return len(output)
