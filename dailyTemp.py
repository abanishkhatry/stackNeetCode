from typing import List 

temp = [30,36,32,33,34,40,30]


# Solution - Optimal Approach 
# Time Complexity - O(n), where n is the size of the input
# Space Complexity - O(n)

"""
This is an important question as it uses the monotonic stack. Here the stack 
that we are using to build up the answer keeps storing the tuples in decreasing order of 
temperature. 

Eventhough we are using a while loop inside a for loop , the time complexity is still o(n), 
because we not visiting the same item twice, we are just removing the items that satisfy the 
condition from the stack to our answer array. Overall, we are just appending and poping the 
each element at most one time. 
"""
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    temps = temperatures
    n = len(temps)
    ans = n * [0]
    stack = []
    # here i is the index, and t is the temp. Increments both simultaneously after each loop
    for i, t in enumerate(temps): 
        # if the stack is not empty and the current t of temps is larger that top placed temp in stack
        while stack and stack[-1][0] < t: 
            item_idx = stack.pop()
            days_diff = i - item_idx[1]
            ans[item_idx[1]] = days_diff

        stack.append((t,i)) 
    return(ans)

print(dailyTemperatures(temp))
