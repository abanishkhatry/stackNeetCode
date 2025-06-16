from typing import List
nums = [ '1', '2', '+', '3', "*", '4','-']

# Solution - Optimal Approach
# Time Complexity - O(n), where n is the size of input array. 
# Space Complexity - O(n)

def evalRPN(tokens: List[str]) -> int:
    operators = ["+", "-" , "/", "*"]
    stack = []
    for j in tokens: 
        if j in operators: 
            second = int(stack.pop())
            first = int(stack.pop())
            if j == "+": 
                new_val = first + second
            if j == "-":  
                new_val = first - second
            if j == "*":  
                new_val = first * second
            if j == "/": 
                new_val = first / second
            stack.append(int(new_val)) 
        else : 
            stack.append(int(j))    
    return(stack[0])
