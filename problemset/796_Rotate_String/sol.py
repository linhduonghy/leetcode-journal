def match(s: str, i: int, n: int, goal: str) -> bool:
    j = i + 1
    cnt = 1
    while cnt < n:
        if j == n:
            j = 0
        if s[j] != goal[cnt]:
            return False
        cnt += 1
        j += 1
    return True


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        n = len(s)
        for i in range(n):
            if s[i] == goal[0]:
                if match(s, i, n, goal):
                    return True

        return False
