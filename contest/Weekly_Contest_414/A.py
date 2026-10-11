class Solution:
    def convertDateToBinary(self, date: str) -> str:

        arr = date.split('-')

        y = format(int(arr[0]), "12b")
        m = format(int(arr[1]), "4b")
        d = format(int(arr[2]), "5b")

        return str(int(y)) + '-' + str(int(m)) + '-' + str(int(d))