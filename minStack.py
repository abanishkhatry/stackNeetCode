from typing import List, Dict

# Solution - Optimal Approach 
# Time Complexity - O (1) , for each function 
# Space Complexity - 0 (n), where n is the total number of elements pushed. 
class MinStack : 

    # like a constructor , initializes the stack object.
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.curr_min = 0

    # stacking the input value.      
    def push(self, val:int) -> None :
        self.stack.append(val) 
        if not self.min_stack or (self.curr_min > val): 
           self.curr_min = val
        self.min_stack.append(self.curr_min)       

    # removes the element from the top of the stack. 
    def pop(self) -> None :
       if not self.stack: 
          print("Stack is empty, can't pop")
       else : 
          # deleting the last element from each
          del self.stack[-1]
          del self.min_stack[-1]  
          # updating curr_min if the min_stack is not empty. 
          if self.min_stack: 
             self.curr_min = self.min_stack[-1]
          else: 
             self.curr_min = None 
                
    # gives the top element from the stack.
    def top(self) -> int : 
     return self.stack[-1]

    # returns the minimum valued element from the stack.
    def getMin(self) -> int: 
       return self.min_stack[-1]


