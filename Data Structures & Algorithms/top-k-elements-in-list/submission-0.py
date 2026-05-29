class Solution:
   #For this problem, the solution that is screaming out to me is to make a hasmap/dict that takes count of all the values in the array.
   #Once you have made this count, then you need to find which counts are highest.
   #We can go through the dictionary using the x, y in dict.collections() method to view the values 
   #To determine which ones get returned, we have an array the size of k, then we input the values inside based on which values are bigger than the current values in the array

   
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        
        bucket = [[] for _ in range(len(nums) + 1)]

        
        top_nums = []
        #Fill dictionary with proper numbers.
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 0
            num_dict[num] += 1
        #Fill the bucket with the corresponding values
        for num, count in num_dict.items():
            bucket[count].append(num)
        
        for i in range(len(bucket)-1, -1, -1):
            for j in range(len(bucket[i])):
                if k <=0:
                    break
                top_nums.append(bucket[i][j])
                k-=1
        return top_nums