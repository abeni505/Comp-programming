class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checker = { "(" : ')', "{" : '}', "[" : ']'}
        for bracket in s:
            if bracket in ["(","[", "{"]:
                stack.append(bracket)
            else:
                if stack and checker[stack [-1]] == bracket:
                    stack.pop() 
                else:
                    return False


        return stack == []
