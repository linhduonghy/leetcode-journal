from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        m = len(box)
        n = len(box[0])
        for row in box:
            blank_pos = n - 1
            for i in range(n - 1, -1, -1):
                if row[i] == '*':
                    blank_pos = i - 1
                elif row[i] == '#':
                    row[i] = '.'
                    row[blank_pos] = '#'
                    blank_pos -= 1
        return zip(*box[::-1])
