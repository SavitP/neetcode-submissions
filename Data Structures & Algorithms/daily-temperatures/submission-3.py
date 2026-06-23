class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        toReturn = [0] * len(temperatures)
        tempNum = 0
        for temp in temperatures:
            if len(stack) == 0:
                stack.append([tempNum, temp])
                tempNum += 1
                continue
            elif temp > stack[len(stack) - 1][1]:
                for i in range(len(stack)):
                    if (temp > stack[len(stack) - 1][1]):
                        item = stack.pop()
                        toReturn[item[0]] = tempNum - item[0]
                    else:
                        break
            stack.append([tempNum, temp])
            tempNum += 1
        return toReturn

