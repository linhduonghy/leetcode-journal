import math
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractionList = re.split('[+-]', expression)
        signList = re.findall('[+-]', expression)

        if expression[0] == '-' or expression[0] == '+':
            fractionList = fractionList[1:]
        else:
            signList.insert(0, '+')

        sign = [1 if _ == '+' else -1 for _ in signList ]
        fraction = [f.split("/") for f in fractionList]
        n = len(sign)
        numerator, denominator = 0, 1

        for i in range(n):
            t = sign[i] * int(fraction[i][0])
            denominator *= int(fraction[i][1])
            for j in range(n):
                if i != j:
                    t *= int(fraction[j][1])
            numerator += t

        gcd = math.gcd(numerator, denominator)

        return str(numerator // gcd) + '/' + str(denominator // gcd)

if __name__ == '__main__':
    print(Solution().fractionAddition("9/4-5/3+7/2-9/5+10/6-1/7+1/8-2/9+2/10"))