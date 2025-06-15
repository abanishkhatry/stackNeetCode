from typing import List
s = "[(])"
# Solution - Optimal Approach 
# Time Complexity : O(n), where n is the size of input array
# Space Complexity : O(n)
def isValid(s: str) -> bool : 
    # if s is empty or odd in length. 
    if len(s) % 2 != 0 or len(s) == 0:
            return False
    
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for i in s: 
        # if opening brackets then appending them to the stack
        if i in mapping.values:
            stack.append(i)
        # if closing brackets then checking them by poping the latest bracket put into the stack that only holds
        # latest opening brackets.    
        elif i in mapping: 
            if not stack or stack.pop() != mapping[i]:
                return False 

    # for valid string, checking if the stack is empty.         
    if(len(stack) == 0) :       
        return True
    else : 
       return False

print(isValid(s))