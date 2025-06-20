from typing import List

def generateParenthesis(n: int) -> List[str]:
    stack = []
    res = []
    def backtrack(openB, closeB): 
        if (openB == closeB == n): 
            res.append(("").join(stack))
            return 
        
        if openB < n : 
            stack.append("(")
            backtrack(openB + 1, closeB)
            stack.pop()

        if closeB < openB: 
            stack.append(")")
            backtrack(openB, closeB + 1)
            stack.pop()

    backtrack(0,0)        
    return res  