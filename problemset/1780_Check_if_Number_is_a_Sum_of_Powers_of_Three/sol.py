class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        def _try(power:int, n: int):
            if n == 0:
                return True
            if 3**power > n:
                return False

            take_power = _try(power + 1, n - 3**power)
            skip_power = _try(power + 1, n)

            return take_power or skip_power

        return _try(0, n)