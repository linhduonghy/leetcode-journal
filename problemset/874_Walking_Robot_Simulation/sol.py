from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        x,y, direction = 0,0,0
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstaclesSet = set(map(tuple, obstacles))
        res = 0
        for command in commands:
            if command == -1:
                direction += 1
                if direction == 4:
                    direction = 0
            elif command == -2:
                direction -= 1
                if direction < 0:
                    direction += 4
            else:
                for _ in range(command):
                    tx = x + d[direction][0]
                    ty = y + d[direction][1]
                    if (tx, ty) in obstaclesSet:
                        break
                    x, y = tx, ty
                    res = max(res, x ** 2 + y ** 2)
        return  res