class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i, item in enumerate(temperatures):
            if i == 0 :
                stack.append((item,i))
            
            while stack and item > stack[-1][0]:
                temp = stack.pop()
                answer[temp[1]] = i - temp[1]
            stack.append((item,i))
        return answer


            
