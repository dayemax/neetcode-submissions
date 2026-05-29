class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_pillar = 0
        max_water = 0




        # for i in range(len(heights)):
        #     if i == 0:
        #         continue
        #     #We are calcualting the minimum height between max pillar and the current pillar, and then mutliplying it with the distance between the two puillars
        #     min_height = min(heights[i], heights[max_pillar])
        #     current_water = (i-max_pillar) * min_height
        #     max_water = max(current_water, max_water)
        #     if heights[i] > heights[max_pillar]:
        #         max_pillar = i
        # return max_water
        front = 0
        back = len(heights)-1

        while front < back:
            min_height = min(heights[front], heights[back])
            current_water = (back - front) * min_height
            max_water = max(current_water,max_water)
            if min_height ==heights[front]:
                front+=1
            elif min_height == heights[back]:
                back -=1
        return max_water

    # current_water [0,1,2,10,16,28,15,36]