import operator
from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/RangeQuery.py
class RangeQuery:
    """
    Range queries on a static array
    """

    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]


def solution():
    def bsr(left: int, right: int) -> int:
        """
        TTTTFFFF
            |
        """

        def check(mid: int) -> bool:
            return rq.query(l, mid + 1) >= k

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left

    n = int(input())
    a = [int(num) for num in input().split()]
    rq = RangeQuery(a, operator.and_)
    q = int(input())
    ans = []
    while q:
        l, k = [int(num) for num in input().split()]
        l -= 1
        r = bsr(l, n - 1) - 1
        if r < l:
            ans.append(-1)
        else:
            ans.append(r + 1)
        q -= 1
    print(*ans)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
