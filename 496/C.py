from os import path
from sys import stdin, stdout
from types import GeneratorType

filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


def solution():
    @bootstrap
    def dp(j: int, prev: int) -> int:
        if (j, prev) in cache:
            yield cache[(j, prev)]
        if j == m:
            ans = 0
        else:
            ans = 10 ** 20
            for i in range(1, n):
                if a[i - 1][prev] == a[i][prev] and a[i][j] < a[i - 1][j]:
                    ans = min(ans, 1 + (yield dp(j + 1, prev)))
                    break
            else:
                ans = min(ans, 1 + (yield dp(j + 1, prev)))
                ans = min(ans, (yield dp(j + 1, j)))
        cache[(j, prev)] = ans
        yield ans

    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(input() + 'a')
    cache = dict()
    print(dp(0, -1))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
