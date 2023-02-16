import sys
from typing import List

input = sys.stdin.readline


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = (int(num) for num in input().split())
    s1 = list(input().rstrip())
    s2 = list(input().rstrip())

    def good(arr: List[str]) -> bool:
        n = len(arr)
        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                return False
        return True

    f1 = good(s1)
    f2 = good(s2)

    if f1 and f2:
        print('YES')
        return

    if (not f1) and (not f2):
        print('NO')
        return

    if not f2:
        s1, s2 = s2, s1

    while s1[-1] != s1[-2]:
        if s2[-1] != s1[-1]:
            s2.append(s1.pop())
        else:
            print('NO')
            return

    if s2[-1] != s1[-1]:
        s2.append(s1.pop())
    else:
        print('NO')
        return

    if good(s1) and good(s2):
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
