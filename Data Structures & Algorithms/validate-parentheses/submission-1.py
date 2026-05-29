
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        inner_brackets = {'(', '[', '{'}
        bracket_dict = {']': '[', '}': '{', ')': '('}
        brack_stack = deque()
        for char in s:
            if char in inner_brackets:
                brack_stack.append(char)
            else:
                if not brack_stack or bracket_dict[char] != brack_stack[-1]:
                    return False
                else:
                    brack_stack.pop()
        return True if not brack_stack else False
