from collections import Counter
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





def solution():
    def bsl(left: int, right: int) -> int:
        """
        FFFFTTTT
            |
        """

        def check(mid: int) -> bool:
            cur = Counter(s[:mid])
            if len(cur) == m:
                return True
            for i in range(mid, n):
                cur[s[i - mid]] -= 1
                if cur[s[i - mid]] == 0:
                    del cur[s[i - mid]]
                cur[s[i]] += 1
                if len(cur) == m:
                    return True
            return False

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    n = int(input())
    s = input()
    m = len(set(s))
    print(bsl(m, n))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
