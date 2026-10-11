from typing import List
class Solution:

    def recursion(self, expression: str, index: List[int]) -> bool:
        cur_char = expression[index[0]]
        index[0] += 1
        if cur_char == 't':
            return True
        elif cur_char == 'f':
            return False

        if cur_char == '!':
            index[0] += 1
            result = not self.recursion(expression, index)
            index[0] += 1
            return result

        # for &, | operator
        values = []
        index[0] += 1
        while expression[index[0]] != ')':
            if expression[index[0]] != ',':
                values.append(self.recursion(expression, index))
            else:
                index[0] += 1
        index[0] += 1

        if cur_char == '&':
            return all(values)

        if cur_char == '|':
            return any(values)

        return False

    def parseBoolExpr(self, expression: str) -> bool:

        return self.recursion(expression, [0])


