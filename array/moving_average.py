# NOTE
# m.next() is OOP solution to add numbers along the process, while m.sequence is OPP solution with sequence input


class MovingAverage(object):
    """
    346. Moving Average from Data Stream
    Given a stream of integers and a window size,
    calculate the moving average of all integers in the sliding window.

    MovingAverage m = new MovingAverage(3);
    m.next(1) = 1
    m.next(10) = (1 + 10) / 2
    m.next(3) = (1 + 10 + 3) / 3
    m.next(5) = (10 + 3 + 5) / 3

    https://leetcode.com/problems/moving-average-from-data-stream

    Open access problem and solution at:
    https://nifannn.github.io/2018/10/01/Algorithm-Notes-Leetcode-346-Moving-Average-from-Data-Stream/#time-complexity-analysis

    """

    def __init__(self, size):

        self.size = size
        self._sum = 0
        self._list = []

    def next(self, val):

        if len(self._list) == self.size:
            first_val = self._list.pop(0)
        else:
            first_val = 0
        self._list.append(val)
        self._sum = self._sum + val - first_val
        return self._sum/len(self._list)

    def sequence(self, nums):

        s = 0
        arr = []
        for i, x in enumerate(nums):
            s += x
            if i < self.size:
                arr.append(s/(i+1))
            else:
                s -= nums[i - self.size]
                arr.append(s/self.size)

        return arr


if __name__ == '__main__':
    m = MovingAverage(3)
    print(m.next(1))
    print(m.next(10))
    print(m.next(3))
    print(m.next(5))

    print(m.sequence([1,10,3,5]))
