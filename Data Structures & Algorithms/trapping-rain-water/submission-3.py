class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        postfix = [0] * len(height)
        output = [0] * len(height)
        print("prefix: ")
        for i in range(len(height)):
            if i == 0:
                prefix[0] = height[0]
                print(prefix[i])
                continue
            prefix[i] = max(prefix[i-1], height[i])
            print(prefix[i])
        #prefix[4,4,4,4,4,5]
        print("postfix: ")
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                postfix[i] = height[i]
                print(postfix[i])
                continue
            postfix[i] = max(postfix[i+1], height[i])
            print(postfix[i])
        #postfix[5,5,5,5,5,5]
        print("output: ")
        for i in range(len(height)):
            output[i] = min(prefix[i],postfix[i]) - height[i]
            print(output[i])
        return sum(output)
        #output = [0,2,4,1,2,0]