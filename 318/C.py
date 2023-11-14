from functools import lru_cache
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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    @lru_cache(None)
    def fib(i: int) -> int:
        if i == 1 or i == 2:
            return 1
        return fib(i - 1) + fib(i - 2)

    x, y, m = [int(num) for num in input().split()]
    ans = 0
    if x >= m or y >= m:
        print(0)
        return
    elif x <= 0 and y <= 0:
        print(-1)
        return
    elif x < 0:
        if x + y < x:
            print(-1)
            return
        else:
            k = ceil(-x, y)
            x = x + k * y
            ans = k
    elif y < 0:
        if x + y < y:
            print(-1)
            return
        else:
            k = ceil(-y, x)
            y = y + k * x
            ans = k
    if y < x:
        x, y = y, x
    i = 1
    while x * fib(i) + y * fib(i + 1) < m:
        i += 1
    ans += i
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
