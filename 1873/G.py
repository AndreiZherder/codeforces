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
    def dp(i: int, c: str) -> int:
        if (i, c) in cache:
            ans = cache[(i, c)]
        else:
            if i >= n - 1:
                ans = 0
            else:
                if i + 1 < n:
                    x = s[i + 1]
                else:
                    x = '#'
                ans1 = yield dp(i + 1, x)

                ans2 = 0
                if c == 'A' and s[i + 1] == 'B':
                    if i + 2 < n:
                        x = s[i + 2]
                    else:
                        x = '#'
                    ans2 = (yield dp(i + 2, x)) + 1

                ans3 = 0
                if c == 'B' and s[i + 1] == 'A':
                    ans3 = (yield dp(i + 1, 'B')) + 1

                ans = max(ans1, ans2, ans3)

        cache[(i, c)] = ans
        yield ans

    s = input()
    n = len(s)
    cache = dict()
    ans1 = dp(0, s[0])
    cache = dict()
    s = s[::-1]
    ans2 = dp(0, s[0])
    print(max(ans1, ans2))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
