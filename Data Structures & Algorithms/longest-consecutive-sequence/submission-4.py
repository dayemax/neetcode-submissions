from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # #Now that its created, iterate through the original list and check if the current num's +- val is in the set
        # #If it is, then we add it to the set.
        # output_set = set()
        # for num in nums:
        #     if (num+1) in num_set:
        #         output_set.add(num)
        # if not output_set and not nums:
        #     return 0
        # elif not output_set and nums:
        #     return 1
        # return len(output_set)
        # #Once we get all the values in the set, we return the set length
        if not nums:
            return 0
        num_set = set(nums)
        #My idea is we create a set called num_set that takes in all the numbers within the list
        #We make a start set that determines the start of a sequence:
        start_set = set()
        
        for num in nums:
            if num-1 not in num_set:
                start_set.add(num)
        
        max_num = 1

        while start_set:

            start_num = start_set.pop()
            current_streak = 1

            while start_num + 1 in num_set:
                current_streak += 1
                start_num +=1
            max_num = max(current_streak,max_num)
        return max_num
            

        