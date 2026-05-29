class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        #Get the prefix values 
        for i in range(len(nums)):
            if i==0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i-1]
        print("prefix " + str(prefix))
        #Get the postfix values
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i+1]
        print("postfix: " + str(postfix))
        #Solve it by subtracting the prefix from the postfix

        output = [0] * len(nums)

        for i in range(len(nums)):
            if i==0:
                output[i] = postfix[1]
            elif i==len(nums)-1:
                output[i] = prefix[len(nums)-2]
            else:
                output[i] = prefix[i-1] * postfix[i+1]
        return output