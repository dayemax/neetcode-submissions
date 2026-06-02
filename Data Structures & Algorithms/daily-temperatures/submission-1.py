#
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day_list = [0] * len(temperatures)
        index_stack = deque()
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            while index_stack and current_temp > temperatures[index_stack[-1]]:
                prev_index = index_stack.pop()
                day_list[prev_index] = i - prev_index
            index_stack.append(i)
        # for i in range(len(temperatures)):
        #     count = 0
        #     current_temp = temperatures[i]
        #     while count + i < len(temperatures):
        #         next_temp = temperatures[i + count]
        #         if next_temp > current_temp:
        #             day_list[i] = count
        #             break
        #         count += 1

        return day_list
