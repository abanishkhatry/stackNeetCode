from typing import List 
heights = [7,1,7,2,2,4]

# Solution - Optimal Approach
# Time Complexity - O(n) , where n is the size of input array. 
# Space Complexity - O(n)

def largestRectangleArea( heights: List[int]) -> int:
    stack = []
    max_area = 0

    for index,height in enumerate(heights): 
        start = index
        while stack and height < stack[-1][0]: 
            h, j = stack.pop()
            width = index - j 
            area = h * width
            max_area = max(max_area, area)
            start = j 
        stack.append((height, start)) 

    while stack: 
        h,j = stack.pop()
        w = len(heights) - j
        max_area = max(max_area, h * w)

    return max_area

print(largestRectangleArea(heights))