class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "*":
                value1 = stack.pop()
                value2 = stack.pop()
                res = value2 * value1
                stack.append(res)  
            elif token in "-":
                value1 = stack.pop()
                value2 = stack.pop()
                res = value2 - value1
                stack.append(res)
            elif token in "+":
                value1 = stack.pop()
                value2 = stack.pop()
                res = value2 + value1
                stack.append(res)
            elif token in "/":
                value1 = stack.pop()
                value2 = stack.pop()
                res = value2 / value1
                if res > 0:
                    res = res // 1
                else:
                    res = -(-res//1)
                
                stack.append(int(res))
            else:
                token = int(token)
                stack.append(token)
        return stack.pop()
