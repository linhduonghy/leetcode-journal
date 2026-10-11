class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 0
        cnt = 10
        while n > 0:
            if n < cnt:
                break
            n -= cnt
            cnt -= 1
            turn = 1 - turn

        return False if turn == 0 else True