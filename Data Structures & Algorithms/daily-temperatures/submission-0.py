#

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day_list = [0] * len(temperatures)
        for i in range(len(temperatures)):
            count = 0
            current_temp = temperatures[i]
            while count + i < len(temperatures):
                next_temp = temperatures[i + count]
                if next_temp > current_temp:
                    day_list[i] = count
                    break
                count += 1
        return day_list
