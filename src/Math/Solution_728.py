class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            if self.isSelfDividingNumber(i):
                res.append(i)
        return res

    def isSelfDividingNumber(self, number):
        num = number
        while num != 0:
            digit = num % 10
            if digit == 0 or number % digit != 0:
                return False
            num //= 10
        return True

if __name__ == '__main__':
    s = Solution()
    res = s.selfDividingNumbers(1, 22)
    print(len(res))
    for i in range(len(res)):
        print(res[i], end=' ')