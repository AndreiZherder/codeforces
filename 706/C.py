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
    def dp(i: int, rotated: int) -> int:
        if (i, rotated) in cache:
            yield cache[(i, rotated)]
        if i == n:
            ans = 0
        else:
            ans = INF
            prev_s = s[i - 1]
            if rotated:
                prev_s = prev_s[::-1]
            if s[i] >= prev_s:
                ans = min(ans, (yield dp(i + 1, 0)))
            if s[i][::-1] >= prev_s:
                ans = min(ans, (yield dp(i + 1, 1)) + c[i])
        cache[(i, rotated)] = ans
        yield ans


    INF = 10 ** 20
    n = int(input())
    c = [int(num) for num in input().split()]
    s = []
    for i in range(n):
        s.append(input())
    s.append('')
    cache = dict()
    print(dp(0, 0) if dp(0, 0) != INF else -1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
