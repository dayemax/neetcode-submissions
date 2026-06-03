#There should be track of two things 
#We know that a rectangle's area is H * W
#If we can c
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
#prefix: [1,1,1,1,1,1]
#postfix:[1,2,4,4,5,6]

#prefix: [7,1,1,1,1,1]
#postfix:[1,1,2,2,2,4]
        n = len(heights)
        prefix = [0] * n
        postfix = [0] * n

        #set the boundaries for the prefix and postfix values
        prefix[0] = -1
        postfix[n-1] = n

        #create the prefix list
        for i in range(1, n):
            pos = i-1
            #While the position doesn't hit the first val and the left side values are greater than the current
            while pos >= 0 and heights[pos] >= heights[i]:
                pos = prefix[pos]
            prefix[i] = pos
        #create the postfix list
        for i in range(n-2,-1,-1):
            pos = i+1
            while pos < n and heights[pos] >= heights[i]:
                pos = postfix[pos]
            postfix[i] = pos
        
        max_area = 0
        for i in range(n):
            width = postfix[i]-prefix[i] - 1
            current_area = heights[i] * width
            max_area = max(max_area, current_area)
        return max_area

        # postfix_area = 0
        # prefix_area = 0
        # width = n
        
        # for i, height in enumerate(prefix):
        #     current_area = height * (i+1)
        #     prefix_area = max(prefix_area, current_area)

        # for i in range(len(postfix)-1,-1,-1):
        #     current_area = postfix[i] * (width-i)
        #     postfix_area = max(postfix_area, current_area)
        
        # return max(prefix_area, postfix_area)

        #heights [7,1,7,2,2,4]

        #prefix [7,1,1,1,1,1]
        #postfix[1,1,2,2,2,4]

        #current_area (prefix) [7,2,3,4,5,6]
        #prefix_area[7,7,7,7,7,7]

        #current_area (post_fix) [6,5,8,6,4,4]
        #postfix(4,4,6,8,8,8)
            