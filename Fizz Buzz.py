class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        i = 1
        while i <= n:
            if i % 3 != 0 and i % 5 != 0:
                answer.append(str(i))
            elif i % 3 == 0 and i % 5 != 0:
                answer.append('Fizz')
            elif i % 3 != 0 and i % 5 == 0:
                answer.append('Buzz')
            elif i % 3 == 0 and i % 5 == 0:
                answer.append('FizzBuzz')
            i += 1
        return answer
