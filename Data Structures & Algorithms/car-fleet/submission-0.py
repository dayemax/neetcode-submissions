from collections import defaultdict, deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_dict = defaultdict()
        for i in range(len(speed)):
           #Create a dictionary that keeps the speed and position locked together for after we sort the dictionary
           car_dict[position[i]] = speed[i] 
        position = sorted(position, reverse=True)


        fleets = 0
        #Time = Distance / Speed
        #Distance = target - position
       # if time of car at a lower position is less than or equal to time at a higher position, 
       #group them together as a car fleet
        stack = deque()
        for pos in position:
            s = car_dict[pos]
            time = (target - pos) / s
            #only append if there is a new car fleet
            if not stack or stack[-1] < time:
                stack.append(time)
        fleets = len(stack)



        return fleets