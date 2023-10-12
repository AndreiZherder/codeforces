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
    def dp(i: int) -> int:
        if i in cache:
            yield cache[i]
        if i > n:
            ans = 10 ** 20
        elif i == n:
            ans = 0
        else:
            ans1 = yield dp(i + nums[i] + 1)
            ans2 = 1 + (yield dp(i + 1))
            ans = min(ans1, ans2)
        cache[i] = ans
        yield ans

    n = int(input())
    nums = [int(num) for num in input().split()]
    cache = dict()
    print(dp(0))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
