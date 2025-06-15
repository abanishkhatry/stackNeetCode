from typing import List 

s = "[(])"

def isValid(s: str) -> bool : 
    stack = []
    for i in s: 
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        if i in "[{(":
            stack.append(i)
            if (len(s) == len(stack)): 
               return False 
        elif i in "}])": 
            if len(stack) != 0: 
             current_high = stack.pop()
             if i == "}" and current_high == "{": 
                continue
             elif (i == "]" and current_high == "["): 
                continue
             elif i == ")" and current_high == "(": 
                continue
            else: 
                return False
    return True

print(isValid(s))