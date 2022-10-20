class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "/":
                result =int(eval("(1/" + stack.pop() + ")*" + stack.pop()))
                stack.append(str(result))
            elif tokens[i] == "-":
                result =eval("-" + stack.pop() + "+" + stack.pop())
                stack.append(str(result))
            elif tokens[i] in "+*":
                result = eval(stack.pop() + tokens[i] + stack.pop())
                stack.append(str(result))
            else:
                stack.append(tokens[i])
        return stack.pop()
