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
    def dp(i: int, color: int, k: int) -> int:
        if (i, color, k) in cache:
            yield cache[(i, color, k)]
        if i == n:
            if k == 0:
                ans = 0
            else:
                ans = 10 ** 20
        elif k <= 0:
            ans = 10 ** 20
        else:
            if c[i] != -1:
                if i == n - 1:
                    ans = yield dp(i + 1, 0, k - 1)
                elif c[i] == c[i + 1]:
                    ans = yield dp(i + 1, color, k)
                elif c[i + 1] != -1:
                    ans = yield dp(i + 1, color, k - 1)
                else:
                    ans = 10 ** 20
                    for j in range(m):
                        if j == color:
                            ans = min(ans, (yield dp(i + 1, color, k)))
                        else:
                            ans = min(ans, (yield dp(i + 1, j, k - 1)))
            else:
                if i == n - 1:
                    ans = (yield dp(i + 1, 0, k - 1)) + p[i][color]
                elif c[i + 1] != -1:
                    if c[i + 1] == color:
                        ans = (yield dp(i + 1, color, k)) + p[i][color]
                    else:
                        ans = (yield dp(i + 1, color, k - 1)) + p[i][color]
                else:
                    ans = 10 ** 20
                    for j in range(m):
                        if j == color:
                            ans = min(ans, (yield dp(i + 1, color, k)) + p[i][color])
                        else:
                            ans = min(ans, (yield dp(i + 1, j, k - 1)) + p[i][color])
        cache[(i, color, k)] = ans
        yield ans

    n, m, k = [int(num) for num in input().split()]
    c = [int(num) - 1 for num in input().split()]
    p = []
    for i in range(n):
        p.append([int(num) for num in input().split()])
    cache = dict()
    ans = 10 ** 20
    if c[0] != -1:
        ans = dp(0, c[0], k)
    else:
        for color in range(m):
            ans = min(ans, dp(0, color, k))
    print(ans if ans != 10 ** 20 else -1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
