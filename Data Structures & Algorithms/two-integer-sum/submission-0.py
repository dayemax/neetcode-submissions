class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        #Fill the num dict
        #initially I was going to have the aarray value be the key and the index be the value, but that wouldn't work because of duplicate array values.
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        #Now we use the target and subtract the current index to find what number we need
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in num_dict and num_dict[difference] != i:
                return [i, num_dict[difference]]
        return []

        
