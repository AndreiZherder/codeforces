import sys
from collections import defaultdict, Counter
from typing import List


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def count(a: List[int]) -> Counter:
        d = Counter()
        cur_num = 10 ** 20
        cur_len = 0
        for num in a:
            if num == cur_num:
                cur_len += 1
            else:
                cur_num = num
                cur_len = 1
            d[num] = max(d[num], cur_len)
        return d

    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    print(max((count(a) + count(b)).values()))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
