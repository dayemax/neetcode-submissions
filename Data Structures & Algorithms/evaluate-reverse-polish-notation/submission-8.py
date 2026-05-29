from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc_stack = deque()
        operator_set = {'+', '*', '-', '/'}

        for token in tokens:
            if token in operator_set:
                val = 0
                a = calc_stack.pop()
                b = calc_stack.pop()
                if token == '+':
                    val = a+b
                elif token == '-':
                    val = b-a
                elif token == '*':
                    val = a*b
                else:
                    val =  int(b/a)
                calc_stack.append(val)
            else:
                calc_stack.append(int(token))

        return calc_stack.pop()