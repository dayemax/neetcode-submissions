class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #My professional thought process is yelling at me saying to solve this with
        #binary search, but I do not remember how to do that with more than 1 index.
        #When thinking about it, if there is an area of the array that has a value greater than the target,
        #there is no need to go there because we cannot add any of those numbers
        #We want to section off that side of the array 
        #Since the target can also be a negative, we'll need to keep that in mind
        #for now, lets think about the general solution. 
        mid = (len(numbers) // 2) + 1
        # i1_min = 1
        # i1_max = mid -1
        # i2_min = mid
        # i2_max = len(numbers)-1
        i_1 = 0
        i_2  = len(numbers)-1
        while (numbers[i_1] + numbers[i_2]) != target:
            sum = numbers[i_1] + numbers[i_2]
            if sum > target:
                i_2 -=1
            elif sum < target:
                i_1 +=1
        return [i_1+1, i_2+1]
