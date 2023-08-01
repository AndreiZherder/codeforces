from os import path
from sys import stdin, stdout


if path.exists("input.txt"):
    stdin = open("input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    m, n = [int(num) for num in input().split()]
    t, z, y = [], [], []
    for i in range(n):
        a, b, c = [int(num) for num in input().split()]
        t.append(a)
        z.append(b)
        y.append(c)
    """
    FFFFTTTT
        |
    """
    def check(mid: int) -> bool:
        total = 0
        for i in range(n):
            time = mid
            a = time % (z[i] * t[i] + y[i])
            if a >= z[i] * t[i]:
                time = ceil(time, z[i] * t[i] + y[i]) * (z[i] * t[i] + y[i])
                contribution = time // (z[i] * t[i] + y[i]) * z[i]
            else:
                contribution = time // (z[i] * t[i] + y[i]) * z[i]
                contribution += a // t[i]
            total += contribution
            if total >= m:
                return True
        return False

    left = 0
    right = 10 ** 9
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    ans = [0 for i in range(n)]
    total = 0
    for i in range(n):
        time = left
        a = time % (z[i] * t[i] + y[i])
        if a >= z[i] * t[i]:
            time = ceil(time, z[i] * t[i] + y[i]) * (z[i] * t[i] + y[i])
            contribution = time // (z[i] * t[i] + y[i]) * z[i]
        else:
            contribution = time // (z[i] * t[i] + y[i]) * z[i]
            contribution += a // t[i]
        ans[i] = contribution
        total += contribution
        if total >= m:
            ans[i] -= total - m
            break
    print(left)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
