import sys
from functools import lru_cache

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, k = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]
    cold = [int(num) for num in input().split()]
    hot = [int(num) for num in input().split()]

    @lru_cache(None)
    def f(i: int, prev_cpu1: int, prev_cpu2: int) -> int:
        if i >= n:
            return 0

        if prev_cpu1 == a[i]:
            ans1 = hot[a[i] - 1]
        else:
            ans1 = cold[a[i] - 1]

        if prev_cpu2 == a[i]:
            ans2 = hot[a[i] - 1]
        else:
            ans2 = cold[a[i] - 1]

        return min(f(i + 1, a[i], prev_cpu2) + ans1, f(i + 1, prev_cpu1, a[i]) + ans2)

    print(f(0, 0, 0))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
